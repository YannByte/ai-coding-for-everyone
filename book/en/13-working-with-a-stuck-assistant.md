# Chapter 13: When Repeated Fixes Don't Work

> Discussion draft. The tool, agent actions, and feedback are untested teaching scenarios. This example has not been selected as the book's main project.
>
> AI-translated from the [Chinese chapter](../zh-CN/13-working-with-a-stuck-assistant.md) at source commit [`c066885`](https://github.com/YannByte/ai-coding-for-everyone/blob/c0668856ad738e66130b3463213538b1bc860123/book/zh-CN/13-working-with-a-stuck-assistant.md). Edited for English readers; human review is pending. See [translation status](../../translations/README.md).

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

If the agent cannot run the program, have it identify missing sample files or software and show any errors. Then address those gaps.

Installing dependencies, meaning other software packages the program needs, must stay within your authorization. So must opening files outside the project and changing permissions. For anything beyond that scope, the agent should explain the purpose and impact before you decide. Checks already allowed can continue.

Once it can run the program, let it check the output and choose its next step. Claude Code's documentation describes this cycle of gathering information, acting, and verifying. It also recommends giving the agent checks it can run. [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop), [best practices](https://code.claude.com/docs/en/best-practices)

Here is a hypothetical investigation:

| What the agent checks | What it finds | Next step |
| --- | --- | --- |
| Runs the program with the sample | Only two PDFs appear | Trace how the file list is built |
| Inspects the scan results | The PDF in the subfolder is present | Check what happens after scanning |
| Compares lists before and after filtering and reads the relevant code | A rule excludes files in subfolders | Check the rule's purpose, then fix it |
| Corrects the rule and runs the program again | All three PDFs appear; the PNG is excluded | Check existing features and copies of the files that originally failed |

In this scenario, the scan was complete all along. Rewriting it could have changed the wrong part of the program. Your investigation may find a different cause. If needed, have the agent add logs: records written while the program runs. Ask it to save the results and identify the relevant code. If the output is hard to read, have it show the lists side by side to explain where the file disappears.

If it cannot operate the interface, let it finish the checks it can run and give you specific steps for the rest. Run those steps and report what happened. The final report should distinguish checks run by the agent, checks run by you, and checks still pending. An explanation that has not been tested by running the program should be labeled as an inference.

## Pause edits when repeated fixes fail

If the agent keeps editing without reproducing the failure, have it check the sample and how it runs the program first. If it has reproduced the problem but keeps retrying old approaches, change the task to reviewing evidence. Have it list completed checks, ruled-out causes, remaining guesses, and what the next check would distinguish. Retrying a failed approach needs new evidence.

For example, if the scan list includes `旧版说明.pdf` but the agent still says it did not scan the subfolder, point out the contradiction. Have it revise its explanation using the result it just obtained.

If edits spread and break existing features, have the agent compare versions and identify changes related to the failure. Ask which files it proposes to restore, how, and what else would be affected. You decide whether to proceed. First save a recoverable version, including edits not yet recorded in version history. Keep separate backups of code and data: restoring code will not recover overwritten data.

If you need a new conversation, another model, or a developer to take over, have the agent save a note. Include the goal, sample and expected result, completed checks, failed attempts, and next step. Add the project location, how to run it, the current version, edits not yet in version history, and where to find check results. In the new conversation, have the agent compare the note with the current files before continuing. [Anthropic’s guidance for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

## Check that tests still express the requirement

The agent may write both the program and its tests, and both may accept the same mistake. This example needs three PDFs, but a test could pass while checking only the two in the main folder. Lowering the expected count to two would also hide the omission. Keep the sample and expected result agreed before the fix. If the agent proposes corrections to a faulty test, judge them against the actual behavior and original requirement. It should not quietly relax that requirement.

Ask for a reusable automated test using this sample. It should fail because the file is missing in the faulty version, then pass after the fix. Failure because the program cannot start does not show that the test detects the missing file.

Check the requirement expressed by the test, then compare the expected and actual lists file by file. `使用说明.pdf`, `申请表.pdf`, and `往年资料/旧版说明.pdf` must all appear; `封面.png` must be absent. A count of three is not enough. Running the same check after later changes to confirm that existing behavior still works is one form of a regression check.

The completion report should identify the cause, code changes, checks actually run, saved results, and anything left unverified. Then use your normal workflow to check the formerly missing file and existing features. Decide whether any remaining gaps affect your use of the tool.
