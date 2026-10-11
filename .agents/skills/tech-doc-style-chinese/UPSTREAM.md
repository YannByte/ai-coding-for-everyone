# Upstream provenance and local changes

- Project: [Fenng/tech-doc-style-chinese](https://github.com/Fenng/tech-doc-style-chinese)
- Original author and copyright holder: Fenng
- Upstream license: [MIT](LICENSE)
- Imported: 2026-10-11, from the installed skill snapshot available during repository setup. The upstream commit of that snapshot is not known; this is not a claim to track upstream HEAD.
- Included: skill entry, upstream README and public explanation, agent metadata, four reference documents, two helper scripts, and three test files.
- Excluded: upstream GitHub automation; this repository owns its CI.

[upstream-files.json](upstream-files.json) records the original SHA-256 values of the 14 imported files. It describes the import baseline, not the current hash of a locally modified file.

## Repository adaptation

On 2026-10-11, YannByte and contributors integrated the book writing method into this Chinese writing skill:

- `SKILL.md`: expanded the task description and added the book workflow entry. This adapted file remains MIT-licensed, including these local changes.
- `agents/openai.yaml`: updated the display name and invocation prompt. This adapted file and its changes remain MIT-licensed.
- [Book workflow](references/book-workflow.md), [writing guide](references/book-writing-guide.md), and [review guide](references/book-review-guide.md): original project documentation under the repository's CC BY-SA 4.0 license. These are local additions, not upstream files or copies of the ASD-STE100 standard.

The other 12 imported files remain unchanged, including the upstream license, reference guides, helper scripts, and tests. The upstream README describes the original skill; use SKILL.md for this repository's integrated entry.

Book-specific voice choices remain in [Chinese writing overrides](../../../docs/chinese-writing.md). Preserve attribution and licenses when updating. Review upstream changes against the recorded baseline, retain or deliberately revise the local integration, and run repository checks. Do not replace this adapted skill with an unreviewed upstream download.
