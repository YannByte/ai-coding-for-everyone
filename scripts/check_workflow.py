"""Check writing records and version-bound reviews, not editorial truth."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = "book/workflow.json"
EVIDENCE = "book/evidence.json"
STAGES = {
    "preparing": "准备材料", "drafting": "起草", "revising": "修改与审阅",
    "reader-testing": "读者验证", "ready": "本轮可交付",
}
REVIEW_KINDS = {"structure", "facts", "language", "author-trial", "reader-trial", "reader-review"}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def local_file(root, files, value, suffix=None):
    if not nonempty(value):
        return False
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or value not in files:
        return False
    full = root / path
    return (full.resolve().is_relative_to(root.resolve()) and not full.is_symlink()
            and full.is_file() and (suffix is None or full.suffix == suffix))


def public_url(value):
    if not nonempty(value):
        return False
    try:
        parsed = urlsplit(value)
        return parsed.scheme in {"https", "http"} and bool(parsed.netloc)
    except ValueError:
        return False


def read_rows(root, files, name, field, errors):
    if name not in files:
        errors.append(f"{name}: record file must be included")
        return []
    try:
        data = json.loads((root / name).read_text(encoding="utf-8"))
    except (OSError, ValueError, UnicodeError):
        errors.append(f"{name}: cannot read JSON record")
        return []
    if (not isinstance(data, dict) or type(data.get("version")) is not int
            or data["version"] != 1 or not isinstance(data.get(field), list)):
        errors.append(f"{name}: expected version 1 and a {field} array")
        return []
    return data[field]


def indexed(rows, label, errors):
    result = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", row["id"]):
            errors.append(f"{label}: each entry needs a stable lowercase id")
            continue
        if row["id"] in result:
            errors.append(f"{label}: duplicate id {row['id']}")
            continue
        result[row["id"]] = row
    return result


def audit_workflow(root, files):
    errors = []
    claims = indexed(read_rows(root, files, EVIDENCE, "claims", errors), EVIDENCE, errors)
    units = indexed(read_rows(root, files, WORKFLOW, "units", errors), WORKFLOW, errors)
    for key, claim in claims.items():
        label = f"{EVIDENCE}: {key}"
        kind, status = claim.get("kind"), claim.get("status")
        if not nonempty(claim.get("claim")):
            errors.append(f"{label}: claim text required")
        if not isinstance(kind, str) or kind not in {"design", "external", "observation"}:
            errors.append(f"{label}: invalid evidence kind")
            continue
        allowed = {"planned"} if kind == "design" else {"pending", "verified"}
        if not isinstance(status, str) or status not in allowed:
            errors.append(f"{label}: invalid evidence status")
            continue
        source = claim.get("source")
        source_ok = public_url(source) if kind == "external" else local_file(root, files, source)
        if source is not None and not source_ok:
            errors.append(f"{label}: source must be an included local file or an external URL for external evidence")
        if status in {"planned", "verified"} and (not source_ok or not nonempty(claim.get("locator"))):
            errors.append(f"{label}: resolved evidence needs source and locator")
    for key, unit in units.items():
        label = f"{WORKFLOW}: {key}"
        stage, kind = unit.get("status"), unit.get("kind")
        if not isinstance(stage, str) or stage not in STAGES:
            errors.append(f"{label}: invalid stage")
            continue
        if not isinstance(kind, str) or kind not in {"practice", "argument"}:
            errors.append(f"{label}: invalid unit kind")
            continue
        case = unit.get("case")
        if case is not None and (not isinstance(case, str)
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case)
                or not local_file(root, files, f"examples/{case}/README.md", ".md")):
            errors.append(f"{label}: case needs a lowercase id and an included examples/<id>/README.md")
        if kind == "practice" and unit.get("case") is None:
            errors.append(f"{label}: practice unit needs a case")
        if type(unit.get("part")) is not int or unit["part"] not in range(1, 6):
            errors.append(f"{label}: part must be 1 through 5")
        if not nonempty(unit.get("title")) or not local_file(root, files, unit.get("brief"), ".md"):
            errors.append(f"{label}: title and included Markdown brief required")
        blockers = unit.get("blockers")
        if not isinstance(blockers, list) or any(not nonempty(b) for b in blockers):
            errors.append(f"{label}: blockers must be a text array")
        elif stage == "ready" and blockers:
            errors.append(f"{label}: ready unit still has blockers")
        refs = unit.get("claims")
        if not isinstance(refs, list) or any(not isinstance(r, str) for r in refs):
            errors.append(f"{label}: claims must be an id array")
            refs = []
        if len(set(refs)) != len(refs) or any(r not in claims for r in refs):
            errors.append(f"{label}: duplicate or unknown claim reference")
        if kind == "practice" and not refs:
            errors.append(f"{label}: practice unit needs evidence references")
        if stage in {"reader-testing", "ready"}:
            if kind == "practice" and not any(claims.get(ref, {}).get("kind") == "observation" and claims[ref].get("status") == "verified" for ref in refs):
                errors.append(f"{label}: practice unit needs verified observation evidence")
            for ref in refs:
                claim = claims.get(ref, {})
                if claim.get("kind") != "design" and claim.get("status") != "verified":
                    errors.append(f"{label}: unresolved fact evidence {ref}")
        manuscript = unit.get("manuscript")
        digest = None
        if manuscript is not None or stage != "preparing":
            if not local_file(root, files, manuscript, ".md") or not manuscript.startswith("book/zh-CN/"):
                errors.append(f"{label}: included Chinese manuscript required")
            else:
                raw = (root / manuscript).read_bytes()
                if not raw.strip():
                    errors.append(f"{label}: manuscript is empty")
                digest = hashlib.sha256(raw).hexdigest()
        reviews = unit.get("reviews")
        if not isinstance(reviews, list):
            errors.append(f"{label}: reviews must be an array")
            reviews = []
        passed, seen = set(), set()
        for review in reviews:
            if not isinstance(review, dict):
                errors.append(f"{label}: invalid review record")
                continue
            review_kind = review.get("kind")
            if not isinstance(review_kind, str) or review_kind not in REVIEW_KINDS or review_kind in seen:
                errors.append(f"{label}: invalid or duplicate review kind")
                continue
            seen.add(review_kind)
            if review.get("result") not in ("pass", "needs-work"):
                errors.append(f"{label}: invalid review result")
            report = review.get("report")
            if not local_file(root, files, report, ".md") or report in (manuscript, unit.get("brief")):
                errors.append(f"{label}: separate included Markdown review report required")
            elif not (root / report).read_text(encoding="utf-8").strip():
                errors.append(f"{label}: review report is empty")
            if digest is None or review.get("manuscript_sha256") != digest:
                errors.append(f"{label}: stale or missing manuscript digest for {review_kind}")
            if review.get("result") == "pass":
                passed.add(review_kind)
        required = set()
        if stage in {"reader-testing", "ready"}:
            required.update({"structure", "facts"})
            if kind == "practice":
                required.add("author-trial")
        if stage == "ready":
            required.update({"language", "reader-trial" if kind == "practice" else "reader-review"})
        if required - passed:
            errors.append(f"{label}: missing passing reviews: {', '.join(sorted(required - passed))}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", action="store_true", help="Show current writing stages and gaps")
    args = parser.parse_args()
    from check_repo import tracked_and_new_files
    try:
        errors = audit_workflow(ROOT, tracked_and_new_files(ROOT))
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        if args.status:
            data = json.loads((ROOT / WORKFLOW).read_text(encoding="utf-8"))
            for unit in data["units"]:
                print(f"{unit['id']} | {STAGES[unit['status']]} | {unit['title']}")
                for blocker in unit["blockers"]:
                    print(f"  待完成：{blocker}")
        else:
            print("Writing records passed. Evidence quality and reader outcomes need human review.")
    except (OSError, ValueError) as exc:
        print(f"Writing check could not complete: {type(exc).__name__}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
