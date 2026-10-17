# Chapter 13: bilingual review after the writing-rule update

Reviewer: AI assistant (Codex). Date: 2026-10-17. Human translation review and target-reader review remain pending.

- Source: [Chinese chapter](../../book/zh-CN/13-working-with-a-stuck-assistant.md), commit `0e5d7f367fcdf409335f369f2ac3676ed3e3e1ef`.
- Source SHA-256: `dd198c484168266ef5f40d490707b9ae85b232a7ad922c2c22f9ba47e141627f`.
- Translation: [English chapter](../../book/en/13-working-with-a-stuck-assistant.md).
- Translation SHA-256: `587ec304ea797857a23ae1f68f8f38f11ba4226353aaf6af1f5e662a2e8db56f`.
- Scope: all six sections, the sample tree, three prose request/report examples, the investigation table, and the handoff note. Compared with the previous English draft at `20f5c1c` and the revised Chinese source above.

## Findings and edits

| Passage | Problem in the previous draft | Revision |
| --- | --- | --- |
| Introduction | The definition put capabilities, permission, and execution location into one long sentence | Defined coding agent in plain English, followed by limits on tools, permissions, and setup; retained the full investigation, fix, and check task |
| Describe the problem | Advice to use copies came after the request to act | Moved preparation before the request; a smaller sample is separate from the original copies; explained automated tests before authorizing changes to them |
| Give the agent feedback | The installation paragraph mixed missing software, access, and permission, and could imply asking again for an already authorized action | Explained dependencies, then distinguished existing authorization from actions outside it |
| When it keeps failing | “Reverting restores files to an earlier state” treated different recovery methods as equivalent | Used ordinary undo/restore wording and required the agent to identify files, method, and affected work; retained backups of both code and data |
| Check the requirement | A failed test could mean a startup failure, and a count alone could hide the wrong files | Required failure for the missing-file reason and comparison of actual filenames with the independently prepared expectation |
| Handoff | The long list of handoff details was hard to follow and omitted edits outside saved history | Split the explanation into connected sentences and included edits not yet in version history |

## Meaning and beginner comprehension

The two versions now explain project, sample, reproduction, automated test, dependency, log, and regression check where needed. They preserve who does the work: the agent investigates, edits, and runs checks; the reader supplies requirements, sets access boundaries, and examines evidence. Neither version requires the reader to write the test or diagnose the filter first.

The English draft retains Chinese filenames and the explanatory English labels. These refer to the same files in both editions; labels are not filenames. The expected result remains the three specified PDFs with the PNG excluded. The investigation, completion report, and alternative stopping point in the handoff are still hypothetical, not a record of completed work.

Conditions were checked in both directions: permission is required for actions beyond existing authorization; a smaller sample must still show the problem; undoing changes requires a recoverable copy; a test must fail for the relevant reason; notes must be checked against current files. The examples still permit changes to project code and tests, preserve sample files, and exclude unrelated features.

The English version uses natural contractions and connected prose. It does not translate Chinese clause order literally or turn paragraphs into a sequence of commands. The sample's English labels remain the main language-specific addition. The revised Chinese source now includes the beginner explanations and comparison methods previously added only to English.

## Automated hints and manual scope

The writing checker flags the first uses of test, dependency, and log. Each is explained at that location; the flags are retained as review reminders. There are no sentence-length or paragraph-length hints in the scanned English prose for this revision. This does not establish readability: the checker skips quotations, tables, and code fences. Those sections were reviewed separately for meaning, filenames, permissions, and expected results. The longer request examples retain related conditions needed to define one task.

## Outcome and remaining limits

AI editorial review found no remaining blocking language or source-alignment issue in this version. The [Chinese reviews](../../book/workflow.json) retain the structural and factual limitations: no implemented teaching tool, author trial, or reader trial, and later chapters are not yet available for overlap review. Human translation and beginner comprehension checks remain pending. This is not STE certification or evidence of a working exercise.
