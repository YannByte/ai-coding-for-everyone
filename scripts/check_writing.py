"""Offline vocabulary, readability hints, and translation-version checks.

This is a deliberately limited Markdown reader, not an STE compliance checker.
It never rewrites prose or treats a readability hint as a failure.
"""

import argparse
from dataclasses import dataclass
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

from check_repo import tracked_and_new_files
from check_workflow import local_file, public_url, read_rows

ROOT = Path(__file__).resolve().parents[1]
VOCABULARY = "docs/vocabulary.json"
TRANSLATIONS = "translations/manifest.json"


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    level: str
    rule: str
    message: str

    def __str__(self):
        return f"{self.path}:{self.line}: {self.level} [{self.rule}] {self.message}"


def vocabulary_rules(root, files):
    errors = []
    rows = read_rows(root, files, VOCABULARY, "rules", errors)
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            errors.append(f"{VOCABULARY}: expected rule objects")
            continue
        key = row.get("id")
        valid_id = isinstance(key, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key)
        if not valid_id or key in seen:
            errors.append(f"{VOCABULARY}: invalid or duplicate rule id")
        if valid_id:
            seen.add(key)
        forms = row.get("forms")
        if not isinstance(forms, list) or not forms or any(not isinstance(s, str) or not s.strip() for s in forms):
            errors.append(f"{VOCABULARY}: {key}: nonempty forms required")
        if row.get("language") not in ("en", "zh-CN", "all"):
            errors.append(f"{VOCABULARY}: {key}: unsupported language")
        if row.get("kind") not in ("spelling", "preference", "first-use"):
            errors.append(f"{VOCABULARY}: {key}: invalid rule kind")
        if row.get("level") not in ("error", "advice") or (row.get("level") == "error" and row.get("kind") != "spelling"):
            errors.append(f"{VOCABULARY}: {key}: only spelling rules may fail")
        if not isinstance(row.get("message"), str) or not row["message"].strip():
            errors.append(f"{VOCABULARY}: {key}: message required")
        source = row.get("source")
        try:
            checked = source.get("checked", "") if isinstance(source, dict) else ""
            valid_date = isinstance(checked, str) and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked))
            if valid_date:
                date.fromisoformat(checked)
        except ValueError:
            valid_date = False
        if not isinstance(source, dict) or not public_url(source.get("url")) or not isinstance(source.get("locator"), str) or not source["locator"].strip() or not valid_date:
            errors.append(f"{VOCABULARY}: {key}: source URL, locator and check date required")
    return ([] if errors else rows), errors


def clean_inline(text):
    # Preserve original files. Exclude literals, source titles/links and quotations.
    text = re.sub(r"(`+).*?\1", " ", text)
    text = re.sub(r'!?\[[^\]]*\]\([^\n]*?\)', " ", text)
    text = re.sub(r'!?\[[^\]]*\]\[[^\]]*\]', " ", text)
    text = re.sub(r'https?://\S+|<[^>]*>', " ", text)
    text = re.sub(r'(?<!\w)(?:[\w.~-]+/)+[\w./~-]+', " ", text)
    text = re.sub(r'“[^”]*”|「[^」]*」|『[^』]*』|"[^"]*"', " ", text)
    return re.sub(r"[*_]", "", text)


def prose_blocks(text):
    """Yield (first line, prose, numbered step); exclude protected Markdown.

    Tables, headings, quoted blocks (including lazy continuations), fenced and
    indented code, comments, reference definitions and front matter are skipped.
    """
    buffer, start, numbered = [], 0, False
    fence, comment, quote, front = None, False, False, False
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        skip = False
        if number == 1 and stripped == "---":
            front = True
            skip = True
        elif front:
            skip = True
            if stripped in ("---", "..."):
                front = False
        elif comment:
            skip = True
            comment = "-->" not in line
        elif "<!--" in line:
            skip = True
            comment = "-->" not in line.split("<!--", 1)[1]
        else:
            marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if marker:
                token, rest = marker.groups()
                skip = True
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence) and not rest.strip():
                    fence = None
            elif fence:
                skip = True
            elif stripped.startswith(">"):
                quote, skip = True, True
            elif quote and stripped and not re.match(r"^(#{1,6}\s|[-*+]\s|\d+[.)]\s)", stripped):
                skip = True
            else:
                quote = False
                skip = (line.startswith(("    ", "\t")) or bool(re.match(r"^(#{1,6}\s|\[[^]]+\]:|[-*_]{3,}$)", stripped)) or "|" in line)
        item = re.match(r"^ {0,3}(\d+[.)]|[-*+])\s+", line)
        if skip or not stripped or item:
            if buffer:
                yield start, " ".join(buffer), numbered
                buffer = []
            if skip or not stripped:
                continue
        if not buffer:
            start = number
            numbered = bool(item and item.group(1)[0].isdigit())
        buffer.append(clean_inline(line[item.end():] if item else line))
    if buffer:
        yield start, " ".join(buffer), numbered


def sentences(text):
    # Keep common abbreviations, decimals and version numbers intact.
    text = re.sub(r"\b(?:e\.g\.|i\.e\.|Mr\.|Mrs\.|Dr\.|vs\.)", lambda m: m[0].replace(".", "\u2024"), text)
    return [s.strip() for s in re.split(r"[.!?]+(?=\s|$)", text) if s.strip()]


def form_pattern(form):
    if form.isascii():
        return r"(?<![A-Za-z0-9_])" + re.escape(form) + r"(?![A-Za-z0-9_])"
    return re.escape(form)


def lint_prose(name, text, language, rules):
    found, seen = [], set()
    for line, paragraph, step in prose_blocks(text):
        for rule in rules:
            if rule["language"] not in (language, "all"):
                continue
            flags = 0 if rule["kind"] == "spelling" else re.IGNORECASE
            if any(re.search(form_pattern(form), paragraph, flags) for form in rule["forms"]):
                if rule["kind"] == "first-use" and rule["id"] in seen:
                    continue
                seen.add(rule["id"])
                found.append(Finding(name, line, rule["level"], rule["id"], rule["message"]))
        if language != "en":
            continue
        parts = sentences(paragraph)
        limit = 20 if step else 25
        for sentence in parts:
            count = len(re.findall(r"[A-Za-z0-9]+(?:['’.-][A-Za-z0-9]+)*", sentence))
            if count > limit:
                found.append(Finding(name, line, "advice", "sentence-length", f"About {count} words (review threshold {limit}); keep conditions and meaning if splitting."))
        if len(parts) > 6:
            found.append(Finding(name, line, "advice", "paragraph-length", f"About {len(parts)} sentences; check that the paragraph develops one topic."))
    return found


def translation_records(root, files):
    errors, targets, seen = [], {}, set()
    rows = read_rows(root, files, TRANSLATIONS, "translations", errors)
    for row in rows:
        if not isinstance(row, dict):
            errors.append(f"{TRANSLATIONS}: expected translation objects")
            continue
        source, translated, report = (row.get(k) for k in ("source", "translation", "review"))
        label = f"{TRANSLATIONS}: {translated}"
        if any(not local_file(root, files, p, ".md") for p in (source, translated, report)):
            errors.append(f"{label}: source, translation and review must be included Markdown files")
            continue
        language = row.get("language")
        if (language != "en" or not source.startswith("book/zh-CN/") or not translated.startswith("book/en/") or Path(source).name != Path(translated).name or report in (source, translated)):
            errors.append(f"{label}: invalid language, chapter identifier or review path")
            continue
        if translated in seen:
            errors.append(f"{label}: duplicate translation")
        seen.add(translated)
        targets[translated] = language
        if not re.fullmatch(r"[0-9a-f]{40}", str(row.get("source_commit", ""))):
            errors.append(f"{label}: full source commit required")
        if row.get("human_review") not in ("pending", "completed"):
            errors.append(f"{label}: explicit human review status required")
        if row.get("human_review") == "completed":
            human = row.get("human_review_report")
            if not local_file(root, files, human, ".md") or human in (source, translated, report):
                errors.append(f"{label}: completed human review requires a separate report")
            else:
                human_text = (root / human).read_text(encoding="utf-8")
                if any(hashlib.sha256((root / p).read_bytes()).hexdigest() not in human_text for p in (source, translated)):
                    errors.append(f"{label}: human review is not bound to current files")
        report_text = (root / report).read_text(encoding="utf-8")
        for key, path in (("source_sha256", source), ("translation_sha256", translated)):
            digest = hashlib.sha256((root / path).read_bytes()).hexdigest()
            if row.get(key) != digest:
                errors.append(f"{label}: stale {key}; review changes before updating the record")
            if digest not in report_text:
                errors.append(f"{label}: review does not identify the current {key}")
    for name in files:
        if re.fullmatch(r"book/en/\d+[^/]*\.md", name) and name not in seen:
            errors.append(f"{name}: translated chapter missing from {TRANSLATIONS}")
    return targets, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Optional repository-relative Markdown files to lint")
    parser.add_argument("--language", choices=("en", "zh-CN"), help="Language for explicit paths")
    args = parser.parse_args(argv)
    try:
        files = tracked_and_new_files(ROOT)
        rules, errors = vocabulary_rules(ROOT, files)
        targets, translation_errors = translation_records(ROOT, files)
        errors.extend(translation_errors)
        units = read_rows(ROOT, files, "book/workflow.json", "units", errors)
        targets.update({"README.md": "en", "README.zh-CN.md": "zh-CN"})
        for unit in units:
            if isinstance(unit, dict) and isinstance(unit.get("manuscript"), str) and unit["manuscript"]:
                targets[unit["manuscript"]] = "zh-CN"
        if args.paths:
            if not args.language:
                parser.error("--language is required with explicit paths")
            targets = {p: args.language for p in args.paths}
        for name in targets:
            if not local_file(ROOT, files, name, ".md"):
                errors.append(f"{name}: lint target must be included Markdown")
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        findings = []
        for name, language in sorted(targets.items()):
            findings.extend(lint_prose(name, (ROOT / name).read_text(encoding="utf-8"), language, rules))
        for finding in findings:
            print(finding)
        failures = sum(f.level == "error" for f in findings)
        print(f"Writing checks: {failures} errors, {len(findings) - failures} review hints. No STE certification or reader validation implied.")
        return int(bool(failures))
    except (OSError, ValueError, UnicodeError, subprocess.SubprocessError) as exc:
        print(f"Writing check could not complete: {type(exc).__name__}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
