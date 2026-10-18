"""Exercise publication failures with isolated, synthetic files."""

from pathlib import Path
import json
import subprocess
import tempfile
import unittest

from check_repo import audit, has_chinese_prose, tracked_and_new_files


class RepositoryChecks(unittest.TestCase):
    def test_chinese_style_check_skips_wholly_english_reports(self):
        self.assertFalse(has_chinese_prose('# Review\n“Check the files.”\n'))
        self.assertFalse(has_chinese_prose('English prose.\n```text\n中文样本\n```\n'))
        self.assertTrue(has_chinese_prose('## 审阅\n保留原意。\n'))

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.files = set()
        self.write("examples/materials.json", "[]\n")

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.files.add(name)

    def errors(self):
        return audit(self.root, self.files)

    def test_links_accept_published_unicode_paths_and_ignore_fences(self):
        self.write("book/示例 文件.md", "# 示例\n")
        self.write("README.md", '[book](<book/示例 文件.md>)\n[ref]: book/示例%20文件.md\n```md\n[not-a-link](missing.md)\n```\n[web](https://example.com)\n')
        self.assertEqual(self.errors(), [])

    def test_links_reject_missing_or_unpublished_files(self):
        (self.root / "local.md").write_text("not included")
        self.write("README.md", "[missing](gone.md)\n[private](local.md)\n[ref]: lost.md\n")
        self.assertEqual(sum("missing published" in e for e in self.errors()), 3)

    def test_link_cannot_escape_repository(self):
        self.write("README.md", "[outside](../other.md)\n")
        self.assertTrue(any("out-of-repository" in e for e in self.errors()))

    def test_forced_tracked_private_file_is_not_hidden_by_gitignore(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        self.write(".gitignore", "private/\n")
        self.write("private/notes.md", "private draft\n")
        subprocess.run(["git", "add", "-f", "private/notes.md"], cwd=self.root, check=True)
        files = tracked_and_new_files(self.root)
        self.assertIn("private/notes.md", files)
        self.assertTrue(any("must not be published" in e for e in audit(self.root, files)))

    def test_environment_template_is_allowed_but_real_config_is_not(self):
        self.write(".env.example", "TOKEN=\n")
        self.assertEqual(self.errors(), [])
        self.write(".env.local", "TOKEN=sample\n")
        self.assertTrue(any("must not be published" in e for e in self.errors()))

    def test_credentials_and_local_paths_are_reported_without_values(self):
        token = "ghp_" + "x" * 30
        home = "/" + "Users" + "/example/private/"
        self.write("README.md", token + "\n" + home + "\n")
        errors = self.errors()
        self.assertEqual(len(errors), 2)
        self.assertNotIn(token, "\n".join(errors))
        self.assertNotIn(home, "\n".join(errors))

    def test_agent_budget_does_not_limit_chapters(self):
        self.write("book/chapter.md", "文" * 6000)
        self.assertEqual(self.errors(), [])
        self.write("book/AGENTS.md", "文" * 2501)
        self.assertTrue(any("budget" in e for e in self.errors()))

    def test_text_with_nul_is_not_silently_treated_as_binary(self):
        self.write("README.md", "# Draft\n\x00")
        self.assertTrue(any("unexpected NUL" in e for e in self.errors()))

    def test_symlink_is_not_a_public_input(self):
        self.write("target.md", "# Target\n")
        (self.root / "linked.md").symlink_to(self.root / "target.md")
        self.files.add("linked.md")
        self.assertTrue(any("regular files" in e for e in self.errors()))

    def test_local_manifest_must_itself_be_published(self):
        self.files.remove("examples/materials.json")
        self.assertTrue(any("manifest must be included" in e for e in self.errors()))

    def test_original_asset_requires_manifest_and_can_pass(self):
        self.write("examples/sample-tool/input.csv", "month,count\nJanuary,3\n")
        self.assertTrue(any("register teaching" in e for e in self.errors()))
        self.write("examples/materials.json", json.dumps([{
            "path": "examples/sample-tool/input.csv", "origin": "original",
            "license": "CC-BY-SA-4.0", "description": "Synthetic teaching input",
        }]))
        self.assertEqual(self.errors(), [])

    def test_third_party_asset_needs_source(self):
        self.write("examples/sample.csv", "item\nexample\n")
        record = {"path": "examples/sample.csv", "origin": "third-party", "license": "CC0-1.0", "description": "Public sample"}
        self.write("examples/materials.json", json.dumps([record]))
        self.assertTrue(any("source URL" in e for e in self.errors()))
        record["source"] = "https://example.com/sample.csv"
        self.write("examples/materials.json", json.dumps([record]))
        self.assertEqual(self.errors(), [])

    def test_manifest_rejects_bad_shape_duplicate_and_missing_file(self):
        self.write("examples/materials.json", "{}")
        self.assertTrue(any("expected an array" in e for e in self.errors()))
        record = {"path": "examples/missing.csv", "origin": "original", "license": "CC-BY-SA-4.0", "description": "Missing"}
        self.write("examples/materials.json", json.dumps([record, record]))
        self.assertTrue(any("duplicate" in e for e in self.errors()))
        self.assertTrue(any("included example" in e for e in self.errors()))


if __name__ == "__main__":
    unittest.main()
