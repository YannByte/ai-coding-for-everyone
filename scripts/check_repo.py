"""Offline repository checks; content judgment remains with reviewers."""

from pathlib import Path
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MATERIALS = "examples/materials.json"
ATTACHMENTS = {
    ".csv", ".tsv", ".xls", ".xlsx", ".ppt", ".pptx", ".doc", ".docx",
    ".pdf", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".zip",
    ".mp3", ".mp4", ".wav", ".jsonl",
}
TEXT_TYPES = {".md", ".py", ".json", ".yml", ".yaml", ".txt", ".toml"}
PRIVATE_DIRS = {"private", "internal", "downloads", ".codex", ".idea", ".vscode"}
CONTENT_PATTERNS = [
    (re.compile(r"/(?:Users|home)/[\w.-]+/|[A-Za-z]:\\Users\\[^\\\s]+\\"), "local home path"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b"), "credential marker"),
    (re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"), "private key marker"),
]


def tracked_and_new_files(root):
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root, check=True, capture_output=True, timeout=20,
    )
    return set(result.stdout.decode("utf-8").rstrip("\0").split("\0")) - {""}


def prose_only(text):
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, rest = marker.groups()
            if fence is None:
                fence = token
                continue
            if token[0] == fence[0] and len(token) >= len(fence) and not rest.strip():
                fence = None
                continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def link_targets(text):
    prose = prose_only(text)
    inline = re.findall(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[^)]+)?\)", prose)
    references = re.findall(r"^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", prose, re.MULTILINE)
    return [target.strip("<>") for target in inline + references]


def material_errors(root, files):
    errors = []
    if MATERIALS not in files:
        return [f"{MATERIALS}: manifest must be included in the repository"]
    try:
        rows = json.loads((root / MATERIALS).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"{MATERIALS}: unreadable manifest ({type(exc).__name__})"]
    if not isinstance(rows, list):
        return [f"{MATERIALS}: expected an array"]
    registered = set()
    for index, row in enumerate(rows):
        label = f"{MATERIALS}: entry {index + 1}"
        required = ("path", "origin", "license", "description")
        if not isinstance(row, dict) or any(not isinstance(row.get(k), str) or not row[k].strip() for k in required):
            errors.append(f"{label}: missing non-empty path, origin, license, or description")
            continue
        name = row["path"]
        if name in registered:
            errors.append(f"{label}: duplicate material path")
        registered.add(name)
        if not name.startswith("examples/") or ".." in Path(name).parts or name not in files or name == MATERIALS:
            errors.append(f"{label}: material must be an included example file")
        if row["origin"] not in {"original", "third-party"}:
            errors.append(f"{label}: invalid origin")
        if row["origin"] == "third-party":
            source = row.get("source", "")
            try:
                url = urlsplit(source) if isinstance(source, str) else None
            except ValueError:
                url = None
            if not url or url.scheme not in {"https", "http"} or not url.netloc:
                errors.append(f"{label}: third-party material needs a public source URL")
    for name in sorted(files):
        if name.startswith("examples/") and Path(name).suffix.lower() in ATTACHMENTS and name not in registered:
            errors.append(f"{name}: register teaching material in {MATERIALS}")
    return errors


def audit(root, files):
    root = root.resolve()
    errors = []
    for name in sorted(files):
        path = root / name
        parts = Path(name).parts
        base = path.name
        if any(part in PRIVATE_DIRS for part in parts) or base in {".npmrc", "settings.local.json"} or path.suffix in {".pem", ".key"} or (base.startswith(".env") and base != ".env.example"):
            errors.append(f"{name}: private/local file must not be published")
        if not path.resolve().is_relative_to(root) or path.is_symlink():
            errors.append(f"{name}: public files must be regular files inside the repository")
            continue
        if not path.is_file():
            errors.append(f"{name}: listed file is missing")
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            if path.suffix in TEXT_TYPES:
                errors.append(f"{name}: expected UTF-8 text")
            continue
        if "\x00" in text:
            if path.suffix in TEXT_TYPES:
                errors.append(f"{name}: unexpected NUL in text file")
            continue
        for pattern, reason in CONTENT_PATTERNS:
            if pattern.search(text):
                errors.append(f"{name}: contains {reason}; inspect locally")
        if base == "AGENTS.md":
            limit = 5000 if name == "AGENTS.md" else 2500
            if len(re.sub(r"\s", "", text)) > limit:
                errors.append(f"{name}: instruction budget exceeds {limit} non-whitespace characters")
        if path.suffix != ".md":
            continue
        for target in link_targets(text):
            try:
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                destination = (path.parent / unquote(url.path)).resolve()
                relative = destination.relative_to(root).as_posix()
            except ValueError:
                errors.append(f"{name}: invalid or out-of-repository file link")
                continue
            included = relative in files or (destination.is_dir() and any(f.startswith(relative + "/") for f in files))
            if not destination.exists() or not included:
                errors.append(f"{name}: missing published link target {target}")
    errors.extend(material_errors(root, files))
    return errors


def main():
    try:
        files = tracked_and_new_files(ROOT)
        errors = audit(ROOT, files)
    except (OSError, subprocess.SubprocessError, UnicodeError) as exc:
        print(f"Repository check could not complete: {type(exc).__name__}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    copy_tools = "tools/chinese-writing"
    prose = [
        name for name in sorted(files)
        if name.endswith(".md") and not name.endswith("AGENTS.md")
        and (name == "README.zh-CN.md" or name == "CONTRIBUTING.md"
             or name.startswith(("book/zh-CN/", "book/plans/", "docs/", "examples/", "translations/")))
    ]
    commands = [
        [sys.executable, "-B", "scripts/check_workflow.py"],
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "scripts", "-p", "test_*.py"],
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", f"{copy_tools}/tests", "-p", "test_*.py"],
        [sys.executable, "-B", f"{copy_tools}/scripts/lint_copy_rules.py", *prose],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, timeout=60)
        if result.returncode:
            return result.returncode
    print(f"Repository checks passed for {len(files)} files. Content and visual review remain manual.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
