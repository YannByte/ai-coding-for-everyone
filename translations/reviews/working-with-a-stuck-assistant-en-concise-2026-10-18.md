# Chapter 13: concise bilingual revision

Reviewer: AI assistant (Codex). Date: 2026-10-18. Human translation review and target-reader review remain pending.

- Source: [Chinese chapter](../../book/zh-CN/13-working-with-a-stuck-assistant.md), commit `190b17dc9f2bc8f402cd2f7b88368ab656a515af`.
- Source SHA-256: `65de42b130c75228cd7af3f2d972c9e27c3721e1abf7a681681556ad281a685c`.
- Translation: [English chapter](../../book/en/13-working-with-a-stuck-assistant.md).
- Translation SHA-256: `6226e68c44b8d30268b07aefd0880ba1ffb1d585cd4275a726b133b5d7488788`.

## Scope and findings

Compared all six sections with the shortened Chinese source and the previous English draft. Removed repeated explanations, the sample completion report, and long intervention and handoff prompts in both editions. Retained the sample tree, evidence table, exact expected filenames, and handoff note.

Conditions remain aligned: preserve samples, follow existing authorization, distinguish agent checks from user checks and pending work, save unrecorded edits before recovery, and back up code separately from data. Tests must detect the omission rather than merely fail to start; the expected count cannot be relaxed, and filenames must be checked as well as totals. The next conversation must compare notes with current files.

The teaching scenario, official source links, and uncertainty remain unchanged. No executed result or new product capability has been added. English retains explanatory labels beside the Chinese filenames and explains project, sample, test, dependency, log, and regression check where needed. Headings and sentences use natural English rather than following Chinese word order.

The length review prompted two final edits: combine a string of short questions into one request, and split a sentence about a test accepting the wrong count. Conditions and meaning remain aligned. First-use terminology hints were checked against the nearby explanations.

## Remaining limits

AI review found no blocking alignment or language issue. The scenario is untested, and no target reader has validated comprehension. This record does not certify translation quality or STE compliance. Earlier review records remain historical.
