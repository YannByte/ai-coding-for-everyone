# Chapter 13: focused bilingual revision

Reviewer: AI assistant (Codex). Date: 2026-10-18. Human translation review and target-reader review remain pending.

- Source: [Chinese chapter](../../book/zh-CN/13-working-with-a-stuck-assistant.md), commit `c0668856ad738e66130b3463213538b1bc860123`.
- Source SHA-256: `eed921cd1bf7dc2674c9eb272dc7b38d1f050ef33d7d56d5adb1f67fe463dd34`.
- Translation: [English chapter](../../book/en/13-working-with-a-stuck-assistant.md).
- Translation SHA-256: `761cd44335f04f18a90138f748b219ec082d0b1f0d4a4c30e268273dace7f74f`.

## Scope and findings

Compared both editions against their previous versions at `c6ebd95`. Both now use four sections: describe the problem, investigate from results, intervene when fixes fail, and verify the requirement. Merged the log explanation with the investigation table commentary. Folded recovery and handoff into the intervention section, removing the separate handoff section and template. Consolidated test expectations without removing the exact filenames.

The sample, hypothetical filtering failure, permissions, and task boundaries remain aligned. Both distinguish agent checks, user checks, and pending work. Recovery still requires saving unrecorded edits and backing up data separately from code. Handoff retains the goal, sample, expected result, checks, failed attempts, next step, project location, run instructions, version, unrecorded edits, and result locations; the next conversation checks these against current files.

Tests must detect the missing file rather than fail to start. Neither edition allows quietly lowering expectations or checking only the count. Both require checking the normal entry point and existing features. English keeps the Chinese filenames with explanatory labels and explains project, sample, reproduction, test, dependency, log, and regression check. The prose follows natural English sentence structure; the condensed handoff is expressed as several sentences rather than one long Chinese-style list.

The paragraph-length hint led to removing a repeated sentence about a passing test while preserving the wrong-count example. Remaining terminology hints have explanations nearby.

## Remaining limits

No new observed outcome or product claim was added; existing source claims were not rechecked online in this edit. AI review found no blocking alignment or language issue. The scenario is untested and target-reader comprehension remains unverified. This is not STE certification or human translation review. Earlier review versions remain in Git history.
