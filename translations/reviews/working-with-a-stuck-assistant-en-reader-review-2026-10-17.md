# Chapter 13: English readability and beginner review

Date: 2026-10-17. Reviewer: AI assistant. Scope: English idiom, translation stiffness, and the knowledge needed to understand the sample chapter. This is an editorial assessment, not feedback from a human English speaker or a beginner who attempted the task.

- Reviewed input: [first English draft at commit 743a2a3](https://github.com/YannByte/ai-coding-for-everyone/blob/743a2a37f015f081df2ece73541ee506b5d6a431/book/en/13-working-with-a-stuck-assistant.md).
- Revised manuscript: [English Chapter 13](../../book/en/13-working-with-a-stuck-assistant.md).
- Revised manuscript SHA-256: `72ac72195ba9942926077c3e6776a3516de24e57eff63024d08c3987ea9698e5`.
- Chinese source commit: `8583912a01fcbc2a2da651b5acc41f11bf9d7d6f`.
- Chinese source SHA-256: `ce71901338417536423c2496a3b7140e79b58415bf69753b387238b5543615bd`.
- Status: revised discussion draft; human bilingual review, beginner reader review, and practical trials pending.

## Assessment

The first draft was grammatical and kept the original argument, but sometimes sounded like an engineering report. The larger barrier for a beginner was assumed knowledge: the text asked readers to review tests and execution evidence without always explaining what those were or what the reader should look for. Readers also had to match unfamiliar Chinese filenames to a separate English paragraph.

The revision keeps the opening problem, six sections, investigation table, prompts, and source references. It explains necessary terms where they first matter and turns abstract checks into things a reader can ask the agent to show. It does not add a runnable exercise or claim that a beginner has completed the scenario.

## Findings and changes

| Location in the chapter | Original wording or gap | Likely reader difficulty | Applied change |
| --- | --- | --- | --- |
| Opening | “Your AI coding agent has tried several fixes” and “files are still missing from the list” | A reader arriving directly at the sample does not yet know which list or what the agent can do | Introduced the PDF-listing tool immediately; added a short, qualified explanation of an AI coding agent's file and execution access |
| Describe the problem | “Make the scan recursive,” “reproduce the problem,” and permission to change “tests” | Technical terms appear before the reader knows what action they describe | Replaced recursive scanning with searching folders inside the main folder; explained reproduction and automated tests before the prompt |
| Sample folder | Chinese filename tree followed by a paragraph translating every name | Readers must repeatedly match names across two places | Put English labels beside the unchanged names; explained indentation and identified the missing file by its English role; stated that labels are not part of filenames |
| Give the agent a way to get feedback | “Naming the missing runtime,” “install dependencies,” “completion record” | Assumes knowledge of software setup and uses report-like nouns | Asked for the missing software and its error; explained dependencies; used “final report” with explicit responsibility for each check |
| Let it investigate | “trace how a file moves” and “its conclusion should be marked as an inference” | Could imply physical file movement; tells beginners to classify evidence without showing how | Described building a list; explained scanning and filtering; asked the agent to point to the PDF before and after filtering; used “still untested” |
| Repeated failures | “reproduced the omission” and “organizing the evidence” | Abstract wording hides what should happen next | Used the same missing-file problem and reviewing what the agent has learned before editing again |
| Passing tests | “both the implementation and its tests” and “you review the requirement it expresses” | A beginner may assume they must read test code to judge it | Used “program”; asked for a plain explanation of pass/fail and expected versus actual filenames side by side; kept failure before the fix and success after it |
| Handoff | “verify the current project state” and “recover the task context” | Unclear what to save, where to put it, or what the next agent should do | Specified a notes file the next agent can open and asked it to compare the notes with current files before continuing |

## Source alignment and editorial additions

The Chinese manuscript is unchanged. The English edition now includes explanatory additions for its intended readers: a brief definition of the agent and project, explanations of tests and dependencies, labels beside the sample names, and concrete ways to request readable check results and handoff notes. These additions are disclosed in the chapter's status note. They clarify existing tasks rather than introduce a new case, tool, result, or promise of success.

The sample still has three PDFs and one PNG, including one PDF in a subfolder. File and folder names and the path in the task prompt are unchanged. The hypothetical scan/filter diagnosis, permission boundaries, unchanged sample files, separate code/data backups, check of the original files, and unverified results remain. Both external references retain their original scope. No measured benefit or firsthand experience has been added.

## What still needs reader validation

An English-speaking beginner should be able to explain which file is missing, what to give the agent, what to do if it cannot run the tool, why a passing test might be inadequate, and what to save before changing conversations. Ask them to point to the sentences that answer these questions and record where they hesitate; these are proposed review questions, not completed results.

The chapter still assumes that the reader can find a project folder and has access to an installed coding agent. Earlier planned chapters are intended to provide that preparation, but are not yet available. This sample explains how to guide an investigation; it does not supply a working PDF tool, sample attachments, installation steps, or product-specific execution records. Understanding the argument and completing an exercise must be evaluated separately. A real trial remains necessary before presenting this as a verified beginner walkthrough.
