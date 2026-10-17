# Chinese writing helper provenance

These standalone Python helpers come from [Fenng/tech-doc-style-chinese](https://github.com/Fenng/tech-doc-style-chinese), copyright © 2026 Fenng, under the retained [MIT license](../../LICENSES/Chinese-Writing-MIT.txt).

The installed source snapshot was imported on 2026-10-11. Its upstream commit is unknown; this is not a claim to track upstream HEAD. Only the two helper scripts and their behavioral tests are retained here. The scripts and copy-checker tests are unchanged. One paragraph-helper test now uses a self-contained Markdown example instead of the removed upstream README; it still verifies that a documented ignore marker does not exempt the document from processing. This directory has no skill entry or invocation metadata.

## Import baseline and SHA-256

| File | SHA-256 |
| --- | --- |
| `scripts/lint_copy_rules.py` | `1171782dcaba2d0e153613afe47dd720aab18704aaa9cdcb4fdc73f765e793c2` |
| `scripts/unwrap_md_paragraphs.py` | `6afb09d660aa7cb9042abb8c82123de5df9545aefd1a445fe6b54238d1ec8636` |
| `tests/test_lint_copy_rules.py` | `8711a87cec6f28f579143ad9cc0e2e277f80c1e7e244ac39154639e721803ef9` |
| `tests/test_unwrap_md_paragraphs.py` | `5fd9c5cadcebbcc9b60064a6a413cb2aecdaca1da6229ca30cf953253762dcc2` |

The hashes record the import baseline, before the test adaptation described above. Keep the license and provenance when updating. Review source changes before replacing the helpers. The repository check runs both test files and the copy checker; paragraph unwrapping remains an optional operation.
