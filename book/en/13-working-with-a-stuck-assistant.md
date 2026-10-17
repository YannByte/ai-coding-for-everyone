# Chapter 13: When Repeated Fixes Don't Work

> Discussion draft, under revision. The file-listing tool, agent actions, and feedback below are teaching scenarios that have not been tested. This example has not been selected as the book's main project.
>
> AI-translated from the [Chinese chapter](../zh-CN/13-working-with-a-stuck-assistant.md) at source commit [`8583912`](https://github.com/YannByte/ai-coding-for-everyone/blob/8583912a01fcbc2a2da651b5acc41f11bf9d7d6f/book/zh-CN/13-working-with-a-stuck-assistant.md). Human translation review is pending. See [translation status](../../translations/README.md).

Your AI coding agent has tried several fixes, but files are still missing from the list. You tell it, “It still doesn't work.” It reads the code again and makes another change.

First, check whether it has run the program with the files that caused the problem.

If all it has done is read code, explain possible causes, and edit files, it is missing feedback from a running program. Asking it to keep fixing the problem may produce more changes that nobody has checked.

You can ask an AI coding agent to read the project, investigate the cause, change the code, and run checks as one task. For that to work, it needs a clear description of the problem, access to the relevant files, a way to run the program, and an agreed way to tell when the work is done. If it gets stuck, use the record of what it has done to decide how to intervene.

We'll follow that process with a tool that lists files.

## Describe the problem before choosing a cause

The tool has a straightforward job: list the PDFs in a chosen folder and all its subfolders. A file exists, but it is missing from the list.

It is tempting to say, “Maybe you're not scanning subfolders. Make the scan recursive.” Without evidence, that instruction picks a direction too early. The agent may then focus on implementing the change you suggested.

Start with what you know: which file is missing, what the result should contain, and where to find the project and sample files. Finding the relevant code, understanding how it works, and investigating the cause can be the agent's job.

Suppose the project contains this sample folder:

```text
测试资料/
├── 使用说明.pdf
├── 申请表.pdf
├── 封面.png
└── 往年资料/
    └── 旧版说明.pdf
```

These names are kept from the Chinese edition so that both versions refer to the same files. The folder `测试资料` means “test files.” It contains an instructions PDF (`使用说明.pdf`), an application form (`申请表.pdf`), a cover image (`封面.png`), and a “previous years” subfolder (`往年资料`) containing an older instructions PDF (`旧版说明.pdf`).

The correct list contains three PDFs and excludes the PNG image. The current list shows only the two PDFs at the top level and misses `旧版说明.pdf` in the subfolder. “Top level” here means directly inside `测试资料`.

You could give the agent this task:

> This tool should list the PDFs in a chosen folder and all its subfolders. At the moment, `测试资料/往年资料/旧版说明.pdf` is missing from the list. Read the current project, find out how to run it, and reproduce the problem with this sample. Then investigate the cause, fix it, and verify the result. All three PDFs should appear, and the PNG should be excluded. You may change this project's code and tests. Leave the sample files unchanged and don't add other features for now. If you can't run the program or reproduce the problem, explain what is blocking you.

When using this approach, give the agent the locations of the project and sample files. Use copies of your documents. If there are too many files to work with easily, ask the agent to prepare a smaller sample from the copies that still reproduces the omission. Check the expected result yourself.

This request gives the agent a goal, materials, boundaries, and a way to judge completion. It can investigate within those boundaries without you first mapping out the program or directing it to open each file in turn.

## Give the agent a way to get feedback

After handing over the task, check whether the agent can access the environment where the problem occurs.

It may have found the code but not the sample that fails. It may have read the startup instructions but lack the software needed to run the program. Or it may be able to run the file scan without being able to operate the application's interface. Each situation needs a different response.

Ask it to identify the specific obstacle. Naming the missing runtime and showing the startup error is more useful than saying “there's an environment problem.” If it needs to install dependencies, access files outside the project, or change permissions, it should explain why and what would be affected so you can decide whether to allow it. It can continue reading, running, and checking wherever the necessary conditions are already in place.

If the agent can run the program, let it run checks, read the output, and use the results to continue investigating. It needn't stop after every edit and wait for you to copy an error message back into the conversation.

If it can check only part of the process, arrange a way to check the rest. For example, it might be able to inspect the scan results but unable to operate the interface. Let it complete the checks it can run, then give you specific steps for checking the interface. Run those steps and report what happened. The completion record should still distinguish what the agent checked, what you checked, and what remains unverified.

Claude Code's official guidance recommends giving the agent checks it can run and examining the verification results. In this example, the sample files and expected list make that check concrete. [Claude Code best practices](https://code.claude.com/docs/en/best-practices)

## Let it investigate, and look at the evidence

The agent should now read the relevant code and trace how a file moves from the input folder to the displayed list. If tests already exist, it should see whether they cover this omission. If the available records aren't enough to locate the problem, it can add temporary logs: records written while the program runs.

You don't need to prescribe each of these steps. You do need to know what evidence supports the agent's diagnosis.

For this example, the agent might examine three stages: scanning folders, filtering for PDFs, and displaying the list. It can then check where the file disappears. One possible investigation would look like this:

| What the agent does | Evidence it finds | What that suggests checking next |
| --- | --- | --- |
| Runs the current program with the sample files | The list contains only two PDFs; the omission is reproduced | Investigate how files are processed |
| Inspects the file list produced by the scan | The PDF in the subfolder is already present | Inspect what happens after scanning |
| Compares the lists before and after filtering and reads the relevant code | A filter condition excludes files in subfolders | Check why the condition exists and determine the scope of the fix |
| Corrects the filter condition and runs the program again | All three PDFs appear; the PNG is excluded | Check existing behavior and a copy of the files that originally failed |

In this hypothetical investigation, the scan was complete all along. Asking the agent to rewrite it at the outset could have sent it to the wrong part of the program. A real project may produce different evidence; follow what the runs reveal.

You can also distinguish different kinds of report. “It might be the filter” is a guess. “There is a filter condition in the code” is a finding from reading the code. “Running the program confirms that this PDF is removed during filtering” connects the finding to the problem you are trying to solve.

Ask the agent to identify the relevant files, the checks it actually ran, and where the results are saved. If it cannot run the program, its conclusion should be marked as an inference. A detailed explanation cannot substitute for a check that has not happened.

## When it keeps failing, change the task

An agent's ability to keep working does not guarantee that it will find a useful direction. If repeated changes do not help, find out where it is stuck.

If it has not reproduced the omission, ask it to pause the fixes and confirm that it is using the same sample and running the program the same way. Checking different inputs from the ones that fail can keep the investigation pointed at the wrong problem.

If it has reproduced the problem but keeps retrying old approaches, you could say:

> Stop making changes for now. Summarize the checks you have actually run and their results. Separate causes you have ruled out from guesses you have not tested. Check whether recent edits introduced new problems, then propose a check that can distinguish between the remaining possible causes. If you want to retry an approach that already failed, explain what new evidence justifies another attempt.

You have changed the immediate task to organizing the evidence before deciding what to do next. The agent should be able to give a concrete result, such as “The scan found every file, so I'll inspect the filtering stage next.” If it only promises to “check again” or “analyze more deeply,” ask it to specify what it will inspect and how it will interpret the result.

If the changes keep spreading and break something that used to work, ask the agent to compare the versions before and after its edits. Have it identify which changes relate to the current problem, then decide which to keep or revert. Reverting restores files to an earlier state. Before doing that, save the current changes and specify what should be restored. Keep separate backups of the project code and the data the program processes; restoring code will not recover overwritten data.

Missing files, an unusable runtime, and repeated guesses need different interventions. Supply the files, make the program runnable, or reorganize the investigation as appropriate. Knowing where the agent is stuck gives your next instruction a purpose.

## Check that passing tests still means meeting the requirement

The agent may write both the implementation and its tests. Check whether the tests' expected results still come from the original requirement.

In this example, all three PDFs must appear. If the agent writes a test that checks only the two top-level PDFs and reports “tests passed,” the omission is still there. If it changes the expected count from three to two to make a failing test pass, it has made the check accept the wrong result.

Agree on the sample and expected result before the fix. The agent can add checks and propose corrections to existing tests when they are wrong, but it should not quietly relax the requirement. When a test and the requirement conflict, compare the test, the program's actual behavior, and the original requirement together.

You can also ask the agent to turn the sample into an automated check that can be run again. It should detect the omission in the faulty version and pass after the fix. The agent writes and runs the check; you review the requirement it expresses. The next time the related code changes, the agent can reuse that check.

After the fix, you could ask for a completion report like this:

> I reproduced the original problem and confirmed that the PDF in the subfolder was excluded during filtering. I corrected the relevant condition. Running the sample again produces a list with all three PDFs and no PNG. The top-level PDFs still appear as before. I also checked a copy of the files that originally failed, and the file known to be missing now appears. I have not checked every file individually.

This is an example report. A real report should also identify the changes and include the check records so you can verify its claims.

You can then open the sample that previously failed and go through your normal workflow yourself. Check whether the files you need appear, whether existing features still work, and whether anything the agent left unverified affects your use of the tool.

## Hand over the work when you change conversations

If you need to start a new conversation, switch models, or ask a developer to take over, have the current agent record its progress first. “Tried many times; still broken” gives the next person or agent very little to work with.

Suppose you stop after reproducing the omission but before finding its cause. The handoff could read:

```text
Goal: List the PDFs in a chosen folder and all its subfolders.
Sample: The 测试资料 folder. Expect three PDFs and no PNG.
Executed: Ran the current program and confirmed that the PDF in the subfolder is missing from the list.
Confirmed: The sample reproduces the omission.
Unknown: Whether the omission occurs during scanning, filtering, or display.
Next: Read the relevant code and inspect intermediate results to locate where the file is lost.
```

When saving the handoff, add the project location, how to run it, the current version, failed attempts, and the location of the check records. Ask the next agent to read those materials and verify the current files before continuing. Progress notes help it recover the task context, but still need to be checked against the project as it stands. [Anthropic's engineering guidance for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

You can begin the new conversation with: “Read the handoff and verify the current project state, then continue investigating where the file goes missing. Reuse the existing checks. If the notes and the actual files disagree, point that out first.”
