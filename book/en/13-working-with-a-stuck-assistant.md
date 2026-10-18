# Chapter 13: When Repeated Fixes Don't Work

> Discussion draft. The tool, agent actions, and feedback are untested teaching scenarios. This example has not been selected as the book's main project.
>
> AI-translated from the [Chinese chapter](../zh-CN/13-working-with-a-stuck-assistant.md) at source commit [`190b17d`](https://github.com/YannByte/ai-coding-for-everyone/blob/190b17dc9f2bc8f402cd2f7b88368ab656a515af/book/zh-CN/13-working-with-a-stuck-assistant.md). Edited for English readers; human review is pending. See [translation status](../../translations/README.md).

A coding agent has tried several fixes, but your file list still misses a PDF. You say, “It still doesn't work.” It reads the code again and makes another change.

First, check whether it has run the program with the files that caused the problem. If it has only read and edited code, it is missing feedback from a running program.

A coding agent is an AI tool that can read project files, edit code, run programs, and use the results to continue working. Its abilities depend on its tools, permissions, and setup. You can ask it to investigate, fix, and verify a problem as one task. Provide the goal and files, then use evidence to redirect it when it gets stuck.

## Describe the problem before prescribing a fix

The tool should list the PDFs in a chosen folder and all its subfolders. A file exists but is missing from the list. Asking the agent to “change the scan to include subfolders” chooses a cause before checking it.

Start by giving it the locations of the project and sample. The project folder holds the code and instructions. The sample contains copies of documents used to check the problem:

```text
测试资料/                  (test files)
├── 使用说明.pdf           (instructions)
├── 申请表.pdf             (application form)
├── 封面.png               (cover image)
└── 往年资料/              (previous years)
    └── 旧版说明.pdf       (older instructions)
```

The English labels explain the names; they are not part of the filenames. Both editions use the same names. The correct list contains all three PDFs and no PNG. The current list contains only the two PDFs directly in the main folder. It misses `往年资料/旧版说明.pdf`, the older instructions in the subfolder.

Have the agent run the program with this sample to see whether the same file goes missing. This is called reproducing the problem. If the original set is large, it can make a separate, smaller sample that still shows the problem. Keep the original copies and check what the smaller sample's list should contain.

You could ask:

> Read the project and reproduce the missing-file problem with this sample. Find the cause, fix it, and check the result. All three PDFs should appear, and the PNG should be excluded. You may change project code and tests. Leave the sample unchanged and don't add other features. If you can't run the program or reproduce the problem, explain what is missing.

A test gives a program an input and checks its response against an expected result. The agent can write and run tests and find the relevant code. You don't need to direct it through each file.

## Let results guide the investigation

Access to code does not guarantee that the agent can check the problem. It may lack the sample or software needed to run the program. It may be able to run the scan but unable to operate the interface. Ask it to identify the missing requirements and show any errors.

Installing dependencies, meaning other software packages the program needs, must stay within your authorization. So must opening files outside the project and changing permissions. For anything beyond that scope, the agent should explain the purpose and impact before you decide. Checks already allowed can continue.

Once it can run the program, let it check the output and choose its next step. Claude Code's documentation describes this cycle of gathering information, acting, and verifying. It also recommends giving the agent checks it can run. [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop), [best practices](https://code.claude.com/docs/en/best-practices)

Here is a hypothetical investigation:

| What the agent checks | What it finds | Next step |
| --- | --- | --- |
| Runs the program with the sample | Only two PDFs appear | Trace how the file list is built |
| Inspects the scan results | The PDF in the subfolder is present | Check what happens after scanning |
| Compares lists before and after filtering and reads the relevant code | A rule excludes files in subfolders | Check the rule's purpose, then fix it |
| Corrects the rule and runs the program again | All three PDFs appear; the PNG is excluded | Check existing features and copies of the files that originally failed |

In this scenario, the scan was complete all along. Rewriting it could have changed the wrong part of the program. Your investigation may find a different cause; follow the results.

The agent can add temporary logs, records written while the program runs, if needed. Look for evidence connecting its explanation to the failure. “It might be the filter” is a guess. “This file disappears after filtering when the program runs” gives you something to check. Ask it to save the results and identify the relevant code. If the output is hard to read, have it show the file lists before and after filtering side by side.

If it cannot operate the interface, let it finish the checks it can run and give you specific steps for the rest. Run those steps and report what happened. The final report should distinguish checks run by the agent, checks run by you, and checks still pending. An explanation that has not been tested by running the program should be labeled as an inference.

## Pause edits when repeated fixes fail

If the agent keeps editing without reproducing the failure, have it check the sample and how it runs the program first. If it has reproduced the problem but keeps retrying old approaches, change the task to reviewing evidence. Have it list completed checks, ruled-out causes, remaining guesses, and what the next check would distinguish. Retrying a failed approach needs new evidence.

Check whether its conclusion uses the latest result. If the scan list includes `旧版说明.pdf` but the agent still says it did not scan the subfolder, point out the contradiction. A specific result gives it more to work with than “think harder.”

If edits spread and break existing features, ask the agent to compare the versions before and after its changes. Identify which edits relate to the problem, then decide which to keep or undo.

Before undoing anything, save a recoverable version, including edits not yet recorded in version history. Ask which files would change, how they would be restored, and what other work might be affected. Restoring selected files and undoing a recorded set of changes can have different effects. Keep separate backups of code and data: restoring code will not recover overwritten data.

## Check that tests still express the requirement

The agent may write both the program and its tests, and both may accept the same mistake. This example needs three PDFs. A test might check only the two PDFs in the main folder, or lower the expected count from three to two. It could then pass while the file is still missing.

Agree on the sample and expected result before the fix. The agent can add checks and propose corrections to faulty tests, but it should not quietly relax the requirement. Resolve conflicts by comparing the test, actual behavior, and original requirement.

Ask for a reusable automated test using this sample. It should fail because the file is missing in the faulty version, then pass after the fix. Failure because the program cannot start does not show that the test detects the missing file.

Compare the expected and actual lists:

- `使用说明.pdf`, `申请表.pdf`, and `往年资料/旧版说明.pdf` must all appear.
- `封面.png` must be absent.

A count of three is not enough; they must be the right files. The agent writes and runs the test, while you check the requirement it expresses. Running it after later changes to check that existing behavior still works is one form of a regression check.

The completion report should identify the cause, code changes, checks actually run, saved results, and anything left unverified. Then use your normal workflow to check the formerly missing file and existing features. Decide whether any remaining gaps affect your use of the tool.

## Leave notes before changing conversations

Before starting a new conversation, switching models, or asking a developer to take over, have the agent save its progress in a file. If it has reproduced the problem but not found the cause, the note could read:

```text
Goal: List the PDFs in a chosen folder and all its subfolders.
Sample: 测试资料; expect three PDFs and no PNG.
Executed: Ran the current program and confirmed that the PDF in the subfolder is missing from the list.
Unknown: Whether the file disappears during scanning, filtering, or display.
Next: Read the relevant code and inspect the file list at each stage.
```

Add the project location, how to run it, the saved version, edits not yet in version history, failed attempts, and where to find check results. Progress notes and version history can help the next conversation pick up the work. [Anthropic's guidance for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

In the new conversation, provide the note's location. Ask the agent to check that it matches the current files before continuing the unfinished investigation.
