# Chapter 13: When Repeated Fixes Don't Work

> Discussion draft, under revision. The file-listing tool, agent actions, and feedback below are teaching scenarios that have not been tested. This example has not been selected as the book's main project.
>
> AI-translated from the [Chinese chapter](../zh-CN/13-working-with-a-stuck-assistant.md) at source commit [`8583912`](https://github.com/YannByte/ai-coding-for-everyone/blob/8583912a01fcbc2a2da651b5acc41f11bf9d7d6f/book/zh-CN/13-working-with-a-stuck-assistant.md). Edited for English readers, with added explanations for beginners. Human translation review is pending. See [translation status](../../translations/README.md).

You asked a coding agent to fix a tool that lists PDF files. It has tried several fixes, but a file is still missing. You tell it, “It still doesn't work.” It reads the code again and makes another change.

First, check whether it has run the program with the files that caused the problem.

If all it has done is read code, explain possible causes, and edit files, it is missing feedback from a running program. Asking it to keep fixing the problem may produce more changes that nobody has checked.

A coding agent is an AI tool that can, with your permission, read and edit program files and run commands on your computer or in a separate environment. Its access depends on the tool and how it is set up. You can ask it to investigate a problem, fix the code, and check the result as one task.

To do that, it needs a clear description of the problem, access to the relevant files, a way to run the program, and an agreed way to tell when the work is done. If it gets stuck, look at what it has tried and what happened before deciding how to help.

We'll follow that process with a tool that lists files.

## Describe the problem before choosing a cause

The tool has a straightforward job: list the PDFs in a chosen folder and all its subfolders. A file exists, but it is missing from the list.

It is tempting to say, “Maybe you're only looking in the main folder. Change the scan so it searches every folder inside it too.” Without evidence, that instruction picks a direction too early. The agent may then focus on implementing the change you suggested.

Start with what you know: which file is missing, what the list should contain, and where to find the project and sample files. Here, the project is the folder containing the tool's code and instructions. The sample files are copies of documents you will use to check it. The agent can find the relevant code and investigate the cause.

Suppose you have the sample folder below. The English labels explain the Chinese names used in the original chapter; the indentation shows which files are inside each folder.

```text
测试资料/                  (test files)
├── 使用说明.pdf           (instructions)
├── 申请表.pdf             (application form)
├── 封面.png               (cover image)
└── 往年资料/              (previous years)
    └── 旧版说明.pdf       (older instructions)
```

The labels in parentheses are explanations, not part of the filenames. You do not need to read Chinese to follow the example: the missing file is the older instructions PDF, inside the “previous years” folder.

The correct list contains all three PDFs and leaves out the PNG image. The current list shows only the two PDFs directly inside the main folder, often called the top level. It misses the older instructions PDF in the subfolder.

Ask the agent to reproduce the problem: run the program with the same files and see whether the same file is missing. You can also allow it to change tests, which are small pieces of code that check whether a program produces an expected result. A request could read:

> This tool should list the PDFs in a chosen folder and all its subfolders. At the moment, `测试资料/往年资料/旧版说明.pdf` is missing from the list. Read the project files, find out how to run the tool, and check that this sample produces the same missing-file problem. Then find the cause, fix it, and run the same check again. All three PDFs should appear, and the PNG should be excluded. You may change this project's code and tests. Leave the sample files unchanged and don't add other features for now. If you can't run the program or get the same problem to happen, explain what is blocking you.

When using this approach, give the agent the locations of the project and sample files. Use copies of your documents. If there are too many files to work with easily, ask the agent to prepare a smaller sample from the copies that still shows the missing-file problem. Check which files should appear in the resulting list yourself.

The agent now knows what to fix, which files to use, what it may change, and how to check its work. You can leave it to investigate without first mapping out the program or directing it to open each file in turn.

## Give the agent a way to get feedback

Once the agent starts, check whether it can open the sample files and run the tool that has the problem.

It may have found the code but not the files that reveal the problem. It may have read the startup instructions but lack the software needed to run the program. Or it may be able to run the file scan without being able to operate the application's interface. Each situation needs a different response.

Ask it to name what is missing and show the error it received. “There's an environment problem” tells you too little to act on. It might need to install dependencies, the software packages your program relies on, or access files outside the project. Before installing anything or changing its access permissions, it should explain why and what would be affected so you can decide whether to allow it. It can continue any checks that its current tools and permissions allow.

If the agent can run the program, let it run checks, read the output, and use the results to continue investigating. It needn't stop after every edit and wait for you to copy an error message back into the conversation.

If it can check only part of the process, arrange a way to check the rest. For example, it might be able to inspect the scan results but unable to operate the interface. Let it complete the checks it can run, then give you specific steps for checking the interface. Run those steps and report what happened. In its final report, the agent should say which checks it ran, which you ran, and which still need to be done.

Claude Code's official guidance recommends giving the agent checks it can run and looking at the results of those checks. In this example, the sample files and expected list make that check concrete. [Claude Code best practices](https://code.claude.com/docs/en/best-practices)

## Let it investigate, and look at the evidence

The agent should now read the relevant code and trace how the program builds its list from the files in the folder. If tests already exist, it should see whether they would catch this missing file. If the available records aren't enough to locate the problem, it can add temporary logs: records written while the program runs.

You can leave those steps to the agent. When it says it has found the cause, ask it to show the result that led it there.

For this example, the agent might examine three stages: scanning folders to find files, filtering that list to keep only PDFs, and displaying the result. It can then check where the file disappears from the list. One possible investigation would look like this:

| What the agent does | Evidence it finds | What that suggests checking next |
| --- | --- | --- |
| Runs the current program with the sample files | The list contains only two PDFs; the same file is missing | Investigate how files are processed |
| Inspects the file list produced by the scan | The PDF in the subfolder is already present | Inspect what happens after scanning |
| Compares the lists before and after filtering and reads the relevant code | A rule used to select PDFs also removes files in subfolders from the list | Check why that rule exists and what needs to change |
| Corrects the rule and runs the program again | All three PDFs appear; the PNG is excluded | Check that older features still work, then check a copy of the original files |

In this hypothetical investigation, the scan was complete all along. Asking the agent to rewrite it at the outset could have sent it to the wrong part of the program. Your project may have a different cause. Use the results of each check to decide where to look next.

You can also distinguish different kinds of report. “It might be the filter” is a guess. “The code has a rule for filtering files” is a finding from reading the code. “When I ran the program, this PDF was in the scan results but missing after filtering” connects the finding to the problem you are trying to solve.

Ask the agent to identify the relevant code files, the checks it actually ran, and where the results are saved. If the output is hard to read, ask it to point out where the missing PDF appears before filtering and where it disappears afterward. You can check that comparison without understanding every line of code. If the agent cannot run the program, it should say that its explanation is still untested.

## When it keeps failing, change the task

An agent can keep working without getting closer to a fix. If repeated changes do not help, find out where it is stuck.

If it has not seen the same file go missing, ask it to pause the fixes. Have it confirm that it is using the same sample and running the program the same way you did. It could be trying to fix a different problem.

If it has reproduced the problem but keeps retrying old approaches, you could say:

> Stop making changes for now. Summarize the checks you have actually run and their results. Separate causes you have ruled out from guesses you have not tested. Check whether recent edits introduced new problems, then suggest what to check next and explain how each possible result would help narrow down the cause. If you want to retry an approach that already failed, explain what new evidence justifies another attempt.

The agent's next job is to review what it has learned before making another edit. It should be able to explain its next step, such as “The scan found every file, so I'll inspect the filtering stage next.” If it only promises to “check again” or “analyze more deeply,” ask it to specify what it will inspect and how it will interpret the result.

If it keeps changing more parts of the program and breaks something that used to work, ask the agent to compare the versions before and after its edits. Have it identify which changes relate to the current problem, then decide which to keep or revert. Reverting restores files to an earlier state. Before doing that, save the current changes and specify what should be restored. Keep separate backups of the project code and the data the program processes; restoring code will not recover overwritten data.

What you ask next depends on where it is stuck. It may need the sample files, help getting the program to run, or a review of what it has already tried.

## Check that passing tests still means meeting the requirement

The agent may write both the program and the tests that check it. Those tests are useful only if they check what you need the program to do.

In this example, all three PDFs must appear. If the agent writes a test that checks only the two top-level PDFs and reports “tests passed,” it has not checked the PDF in the subfolder. If it changes the expected count from three to two to make a failing test pass, it has made the check accept the wrong result.

Agree on the sample and expected result before the fix. The agent can add checks and propose corrections to existing tests when they are wrong, but it should not quietly relax the requirement. When a test and the requirement conflict, compare the test, the program's actual behavior, and the original requirement together.

You can also ask the agent to turn the sample into an automated check that can be run again. The check should fail when run against the faulty version and pass after the fix. Ask the agent to write and run the check, then explain what would make it pass or fail. Ask it to show the expected and actual filenames side by side. Compare them with the list you expect: all three named PDFs, with the PNG left out. You do not need to write the test yourself. The next time the related code changes, the agent can reuse that check.

After the fix, you could ask for a completion report like this:

> I ran the program and saw the same missing-file problem. The scan found the PDF in the subfolder, but a filtering rule removed it from the list. I corrected that rule. Running the sample again produces a list with all three PDFs and no PNG. The top-level PDFs still appear as before. I also checked a copy of the files that originally failed, and the file known to be missing now appears. I have not checked every file individually.

This is an example report. A real report should also identify the changes and include the saved results so you can check what it reports.

You can then open the sample that previously failed and go through your normal workflow yourself. Check whether the files you need appear, whether existing features still work, and whether anything the agent left unverified affects your use of the tool.

## Hand over the work when you change conversations

If you need to start a new conversation, switch models, or ask a developer to take over, have the current agent record its progress first. “Tried many times; still broken” gives the next person or agent very little to work with.

Suppose the agent has run the program and seen the same problem, but you stop before it finds the cause. The handoff could read:

```text
Goal: List the PDFs in a chosen folder and all its subfolders.
Sample: The 测试资料 folder. Expect three PDFs and no PNG.
Executed: Ran the current program and confirmed that the PDF in the subfolder is missing from the list.
Confirmed: Running the sample shows the same missing-file problem.
Unknown: Whether the file is left out during scanning, filtering, or display.
Next: Read the relevant code and check the file list at each stage to find where the PDF disappears.
```

Save these notes in a file the next agent can open. Include the project folder's location, how to run the program, which saved version you were working on, what did not work, and where the check results are stored. Ask the next agent to read the notes and compare them with the files before continuing. The notes help it pick up the work, but they may be out of date. [Anthropic's engineering guidance for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

In the new conversation, give the agent the location of the notes and say: “Read these notes and check that they match the files we have now. Then continue investigating where the PDF disappears from the list. Reuse the existing checks. If the notes and files disagree, tell me before continuing.”
