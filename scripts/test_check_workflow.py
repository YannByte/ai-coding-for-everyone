"""Writing gates fail on unsupported progress, missing evidence and stale reviews."""

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from check_workflow import audit_workflow, WORKFLOW, EVIDENCE


class WritingChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.files = set()
        self.write("book/plans/sample.md", "# Teaching plan\n")
        self.claim = {"id": "sample-design", "claim": "Teaching design, not observed success.",
                      "kind": "design", "status": "planned", "source": "book/plans/sample.md", "locator": "Teaching plan"}
        self.unit = {"id": "sample", "title": "Sample", "part": 2, "kind": "practice",
                     "case": "recurring-report", "status": "preparing", "brief": "book/plans/sample.md",
                     "manuscript": None, "claims": ["sample-design"], "reviews": [], "blockers": ["Prepare inputs"]}
        self.claims = [self.claim]
        self.units = [self.unit]

    def write(self, name, content):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        self.files.add(name)

    def errors(self):
        self.write(WORKFLOW, json.dumps({"version": 1, "units": self.units}))
        self.write(EVIDENCE, json.dumps({"version": 1, "claims": self.claims}))
        return audit_workflow(self.root, self.files)

    def manuscript(self):
        self.unit["manuscript"] = "book/zh-CN/sample.md"
        self.write(self.unit["manuscript"], "# A complete teaching passage\n")

    def review(self, kind):
        name = f"book/reviews/{kind}.md"
        self.write(name, "# Synthetic review fixture\nScope and limitations reviewed.\n")
        self.unit["reviews"].append({"kind": kind, "result": "pass", "report": name,
            "manuscript_sha256": hashlib.sha256((self.root / self.unit["manuscript"]).read_bytes()).hexdigest()})

    def ready(self):
        self.manuscript()
        self.write("book/reviews/observation.md", "# Recorded trial\n")
        self.claim.update(kind="observation", status="verified", source="book/reviews/observation.md", locator="Recorded trial")
        self.unit.update(status="ready", blockers=[])
        for kind in ["structure", "facts", "language", "author-trial", "reader-trial"]:
            self.review(kind)

    def test_preparing_is_valid_without_fabricated_manuscript_or_reviews(self):
        self.assertEqual(self.errors(), [])

    def test_missing_and_malformed_registers_fail(self):
        self.assertTrue(audit_workflow(self.root, self.files))
        self.errors()
        for text in ("{", "[]", '{"version": true, "units": []}'):
            with self.subTest(text=text):
                self.write(WORKFLOW, text)
                self.assertTrue(audit_workflow(self.root, self.files))

    def test_duplicate_ids_and_unknown_references_fail(self):
        self.units.append(dict(self.unit))
        self.claims.append(dict(self.claim))
        self.unit["claims"].append("unknown")
        errors = "\n".join(self.errors())
        self.assertIn("duplicate id", errors)
        self.assertIn("unknown claim", errors)

    def test_drafting_requires_manuscript_but_can_have_evidence_gaps(self):
        self.unit["status"] = "drafting"
        self.assertTrue(self.errors())
        self.manuscript()
        self.claim.update(kind="observation", status="pending", source=None, locator=None)
        self.assertEqual(self.errors(), [])

    def test_empty_manuscript_fails(self):
        self.manuscript()
        self.unit["status"] = "drafting"
        self.write(self.unit["manuscript"], "\n")
        self.assertIn("manuscript is empty", "\n".join(self.errors()))

    def test_invented_completion_stage_and_malformed_status_fail_cleanly(self):
        for stage in ("published", [], None):
            self.unit["status"] = stage
            self.assertTrue(self.errors())
        self.unit["status"] = "preparing"
        self.claim["status"] = []
        self.assertTrue(self.errors())

    def test_design_cannot_be_relabelled_as_verified(self):
        self.claim["status"] = "verified"
        self.assertIn("invalid evidence status", "\n".join(self.errors()))

    def test_verified_external_claim_needs_locator_and_url(self):
        self.claim.update(kind="external", status="verified", source="https://example.com/source", locator=None)
        self.assertTrue(self.errors())
        self.claim["locator"] = "Section 2"
        self.assertEqual(self.errors(), [])
        self.claim["source"] = "book/plans/sample.md"
        self.assertTrue(self.errors())

    def test_reader_testing_needs_author_trial_and_observation(self):
        self.manuscript()
        self.unit["status"] = "reader-testing"
        self.review("structure")
        self.review("facts")
        errors = "\n".join(self.errors())
        self.assertIn("author-trial", errors)
        self.assertIn("verified observation", errors)

    def test_ready_passes_with_version_bound_reviews(self):
        self.ready()
        self.assertEqual(self.errors(), [])

    def test_author_trial_cannot_replace_reader_trial(self):
        self.ready()
        self.unit["reviews"] = [r for r in self.unit["reviews"] if r["kind"] != "reader-trial"]
        self.assertIn("reader-trial", "\n".join(self.errors()))

    def test_manuscript_edit_invalidates_previous_reviews(self):
        self.ready()
        self.write(self.unit["manuscript"], "# Changed instructions\n")
        self.assertIn("stale", "\n".join(self.errors()))

    def test_missing_report_and_failed_review_do_not_pass(self):
        self.ready()
        self.files.remove(self.unit["reviews"][0]["report"])
        self.unit["reviews"][-1]["result"] = "needs-work"
        errors = "\n".join(self.errors())
        self.assertIn("report required", errors)
        self.assertIn("reader-trial", errors)

    def test_ready_rejects_remaining_work_and_pending_fact(self):
        self.ready()
        self.unit["blockers"] = ["Unresolved layout issue"]
        self.claim["status"] = "pending"
        errors = "\n".join(self.errors())
        self.assertIn("still has blockers", errors)
        self.assertIn("unresolved fact", errors)

    def test_outside_or_unpublished_sources_are_rejected(self):
        for source in ("../private.md", "/tmp/private.md", "book/unpublished.md"):
            with self.subTest(source=source):
                self.claim["source"] = source
                self.assertTrue(self.errors())

    def test_argument_requires_reader_review_not_practical_trial(self):
        self.manuscript()
        self.unit.update(kind="argument", case=None, status="ready", blockers=[])
        for kind in ["structure", "facts", "language", "reader-review"]:
            self.review(kind)
        self.assertEqual(self.errors(), [])


if __name__ == "__main__":
    unittest.main()
