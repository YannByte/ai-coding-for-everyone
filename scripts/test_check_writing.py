"""Check enforcement boundaries and false-positive protection with synthetic text."""

import copy
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import check_writing
from check_writing import lint_prose, prose_blocks, sentences, translation_records, vocabulary_rules


SPELLING = {
    "id": "product", "language": "all", "kind": "spelling", "level": "error",
    "forms": ["Github"], "message": "Use GitHub.",
    "source": {"url": "https://docs.github.com/en", "locator": "Product name", "checked": "2026-10-17"},
}
PREFERENCE = {**SPELLING, "id": "plain", "kind": "preference", "level": "advice", "forms": ["utilize"]}
FIRST_USE = {**SPELLING, "id": "first", "kind": "first-use", "level": "advice", "forms": ["test", "tests"]}


class ProseChecks(unittest.TestCase):
    def lint(self, text, rules=None, language="en"):
        return lint_prose("sample.md", text, language, rules or [SPELLING])

    def test_spelling_is_case_sensitive_and_whole_word(self):
        findings = self.lint("Use GitHub, Github and GithubEnterprise.")
        self.assertEqual([(f.rule, f.level) for f in findings], [("product", "error")])

    def test_code_quotes_links_frontmatter_and_tables_are_protected(self):
        text = '''---
title: Github
---
# Github

```text
Github
```
~~~
Github
~~~
    Github

> Github
lazy Github continuation

| Github | example |
| --- | --- |
[Github](https://example.com/Github)
[Github][source]
[source]: https://example.com/Github
<!-- Github -->
<!--
Github
-->
`Github` and ``a `Github` value`` and “Github” and "Github" and 「Github」.
https://example.com/Github
docs/Github.md
'''
        self.assertEqual(self.lint(text), [])

    def test_fence_close_must_match_open_fence(self):
        self.assertEqual(self.lint("````\n```\nGithub\n````\n"), [])

    def test_advice_does_not_become_error_and_first_use_only_once(self):
        findings = self.lint("Utilize a test.\n\nRun more tests.", [PREFERENCE, FIRST_USE])
        self.assertEqual([f.level for f in findings], ["advice", "advice"])
        self.assertEqual([f.rule for f in findings], ["plain", "first"])

    def test_first_use_in_quote_does_not_hide_first_use_in_prose(self):
        findings = self.lint('> test\n\nRun a test.', [FIRST_USE])
        self.assertEqual([(f.rule, f.line) for f in findings], [("first", 3)])

    def test_sentence_length_boundaries_are_only_hints(self):
        words = lambda n: " ".join(["word"] * n) + "."
        self.assertEqual(self.lint(words(25)), [])
        self.assertEqual(self.lint(words(26))[0].level, "advice")
        self.assertEqual(self.lint("1. " + words(20)), [])
        self.assertEqual(self.lint("1. " + words(21))[0].rule, "sentence-length")
        self.assertEqual(self.lint(words(30), language="zh-CN"), [])

    def test_paragraph_counts_soft_wrapped_lines_and_reports_start(self):
        text = "# Title\n\nOne sentence.\n" + "Another sentence. " * 6
        self.assertEqual([(f.rule, f.line) for f in self.lint(text)], [("paragraph-length", 3)])

    def test_abbreviations_and_decimals_do_not_split_sentences(self):
        self.assertEqual(len(sentences("Dr. Lee uses v3.11, e.g. for tests. It takes 1.5 seconds.")), 2)

    def test_chinese_forms_do_not_need_english_word_boundaries(self):
        rule = {**PREFERENCE, "language": "zh-CN", "forms": ["优化一下"]}
        self.assertEqual(len(self.lint("请优化一下程序。", [rule], "zh-CN")), 1)
        self.assertEqual(self.lint("请优化一下程序。", [rule], "en"), [])


class RecordChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.files = set()
        self.source = "book/zh-CN/13-sample.md"
        self.translation = "book/en/13-sample.md"
        self.report = "translations/reviews/sample.md"
        self.write(self.source, "中文正文")
        self.write(self.translation, "English prose.")
        self.record = {
            "language": "en", "source": self.source, "translation": self.translation,
            "review": self.report, "source_commit": "a" * 40, "human_review": "pending",
            "source_sha256": self.digest(self.source), "translation_sha256": self.digest(self.translation),
        }
        self.write(self.report, self.record["source_sha256"] + "\n" + self.record["translation_sha256"])
        self.manifest()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.files.add(name)

    def digest(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def manifest(self, rows=None):
        self.write("translations/manifest.json", json.dumps({"version": 1, "translations": [self.record] if rows is None else rows}))

    def errors(self):
        return translation_records(self.root, self.files)[1]

    def test_matching_translation_passes_without_git_history(self):
        self.assertEqual(self.errors(), [])

    def test_changed_source_and_translation_each_invalidate_review(self):
        for path in (self.source, self.translation):
            with self.subTest(path=path):
                original = (self.root / path).read_text()
                self.write(path, original + " changed")
                self.assertTrue(any("stale" in e for e in self.errors()))
                self.write(path, original)

    def test_updating_digest_alone_does_not_refresh_review(self):
        self.write(self.translation, "Revised English.")
        self.record["translation_sha256"] = self.digest(self.translation)
        self.manifest()
        self.assertTrue(any("review does not identify" in e for e in self.errors()))

    def test_missing_manifest_unregistered_and_duplicate_translations_fail(self):
        self.manifest([])
        self.assertTrue(any("missing from" in e for e in self.errors()))
        self.manifest([self.record, self.record])
        self.assertTrue(any("duplicate" in e for e in self.errors()))
        self.files.remove("translations/manifest.json")
        self.assertTrue(any("must be included" in e for e in self.errors()))

    def test_missing_review_escape_and_symlink_are_rejected(self):
        self.files.remove(self.report)
        self.assertTrue(self.errors())
        self.files.add(self.report)
        self.record["review"] = "../elsewhere.md"
        self.manifest()
        self.assertTrue(self.errors())
        self.record["review"] = self.report
        self.manifest()
        (self.root / self.report).unlink()
        (self.root / self.report).symlink_to(self.root / self.source)
        self.assertTrue(self.errors())

    def test_human_completion_requires_report_and_commit_must_be_full(self):
        self.record.update(human_review="completed", source_commit="abc1234")
        self.manifest()
        self.assertTrue(any("human review" in e for e in self.errors()))
        self.assertTrue(any("full source commit" in e for e in self.errors()))

    def test_malformed_record_is_reported(self):
        self.manifest([None, {"source": []}])
        self.assertTrue(self.errors())

    def test_vocabulary_requires_sources_and_cannot_make_advice_fatal(self):
        for row in (SPELLING, PREFERENCE, FIRST_USE):
            self.write("docs/vocabulary.json", json.dumps({"version": 1, "rules": [row]}))
            self.assertEqual(vocabulary_rules(self.root, self.files)[1], [])
        bad = copy.deepcopy(PREFERENCE)
        bad["level"] = "error"
        del bad["source"]["locator"]
        self.write("docs/vocabulary.json", json.dumps({"version": 1, "rules": [bad]}))
        rules, errors = vocabulary_rules(self.root, self.files)
        self.assertEqual(rules, [])
        self.assertEqual(len(errors), 2)

    def test_vocabulary_bad_json_shape_and_duplicates_fail(self):
        for value in ("broken", "[]", json.dumps({"version": 1, "rules": [None, SPELLING, SPELLING]})):
            self.write("docs/vocabulary.json", value)
            self.assertTrue(vocabulary_rules(self.root, self.files)[1])

    def test_nonexistent_check_date_fails(self):
        row = copy.deepcopy(SPELLING)
        row["source"]["checked"] = "2026-02-30"
        self.write("docs/vocabulary.json", json.dumps({"version": 1, "rules": [row]}))
        self.assertTrue(vocabulary_rules(self.root, self.files)[1])

    def test_human_report_must_be_separate_and_current(self):
        self.record.update(human_review="completed", human_review_report=self.report)
        self.manifest()
        self.assertTrue(self.errors())
        human = "translations/reviews/human.md"
        self.write(human, "Reviewed a different version.")
        self.record["human_review_report"] = human
        self.manifest()
        self.assertTrue(any("not bound" in e for e in self.errors()))
        self.write(human, (self.root / self.report).read_text())
        self.assertEqual(self.errors(), [])

    def test_entrypoint_returns_failure_for_errors_but_not_advice(self):
        self.write("docs/vocabulary.json", json.dumps({"version": 1, "rules": [SPELLING, PREFERENCE]}))
        self.write("book/workflow.json", json.dumps({"version": 1, "units": []}))
        self.write("README.zh-CN.md", "# 中文入口\n")
        for text, code in (("Utilize the tool.", 0), ("Use Github.", 1)):
            self.write("README.md", text)
            with patch.object(check_writing, "ROOT", self.root), patch.object(check_writing, "tracked_and_new_files", return_value=self.files), redirect_stdout(io.StringIO()):
                self.assertEqual(check_writing.main([]), code)


if __name__ == "__main__":
    unittest.main()
