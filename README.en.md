# Using Coding Agents Effectively

[简体中文（默认）](README.md) · [Start reading](#start-reading) · [Book outline (Chinese)](book/zh-CN/README.md) · [Contributing](CONTRIBUTING.md)

A book in preparation for people with or without programming experience who want to use AI to build, check, and maintain software they need. The title is provisional.

Start with a problem you want to solve. Explain the goal, let the agent investigate, act, and check its work, then judge whether the result meets your needs. When work stalls or goes off course, use the evidence to adjust the task and save useful methods for next time.

> Four Chinese discussion drafts are available, all under revision. The teaching scenarios remain untested. No chapter is final, and no runnable exercise or reader trial is complete.

## How AI is used in writing this book

AI is part of the writing process, including organizing material, drafting, and rewriting the text. If you prefer not to read a book written this way, you can choose to skip it.

Many of the ideas, principles, and cautions in this book come from my everyday practice. Sometimes I have only a brief observation or a short note about an experience. My main reason for using AI is to explain the reasoning and conditions behind those notes so readers can understand and apply them.

I remain responsible for editorial decisions, fact-checking, and revisions. Personal experience, teaching scenarios, and external sources are identified separately, and unverified content is marked as such. See the [writing method (Chinese)](docs/writing-method.md#ai-怎样参与本书写作) for the division of work.

## Start reading

The [English sample chapter, When Repeated Fixes Don't Work](book/en/13-working-with-a-stuck-assistant.md), discusses how to guide an investigation when repeated fixes fail. It is a translation of Chapter 13 and awaits human review.

If you read Chinese, start with Chapter 1 or choose a question you are facing:

| Question | Chinese discussion draft |
| --- | --- |
| How do I start without programming experience? | [Chapter 1: Start with your problem](book/zh-CN/01-start-with-your-problem.md) |
| Why did the agent miss a requirement I already gave it? | [Chapter 6: What the agent knows and forgets](book/zh-CN/06-what-the-agent-knows.md) |
| How do I decide whether existing open source code fits? | [Chapter 9: Reuse established code, then fill the gaps](book/zh-CN/09-choosing-libraries-with-an-agent.md) |
| What can I do when repeated fixes fail? | [Chapter 13: Working with a stuck agent](book/zh-CN/13-working-with-a-stuck-assistant.md) |

Chinese is the default language for the book and repository; English is supplementary. A complete English edition is not yet available. See [translation status](translations/README.md) for the source revision and review limits.

## What the book covers

A coding agent is an AI tool that can read project files, edit code, and run programs within its permissions. It uses the results to continue working on a task. Examples include Codex and Claude Code; capabilities depend on the product, version, and environment. The book focuses on using existing agents for software work; building agent systems is outside its scope.

The provisional outline has five parts and nineteen chapters. It moves from a first working version through agent behavior, project organization, changes and delivery, and reusable working methods. Programming concepts are explained as tasks require them; experienced readers can skip the basics. See the [full outline (Chinese)](book/zh-CN/README.md).

Effectiveness includes correctness, maintainability, human effort, waiting, rework, and model usage. Generation speed and token counts are only part of that picture.

## Project status and contributions

The audience and purpose are established; the outline remains an editorial draft. The teaching project and coding tools are undecided, and the repository retains its original name. See [project scope](docs/project.md) for decisions and open questions, [work status](book/workflow.json) for chapter revisions, and [case status](examples/README.md) for exercise materials.

Feedback on unclear passages, practical questions, and problems that can be reproduced with public materials is welcome. See [Contributing](CONTRIBUTING.md) for how to share feedback and propose changes. For writing and fact-checking, these documents explain the approach in Chinese:

- [Writing method](docs/writing-method.md): explaining decisions, actions, and checks.
- [Production workflow](docs/production.md): preparing material, reviewing drafts, and testing exercises.
- [Sources and limits](docs/sources.md): references and the claims they support.

## License

Unless a file states otherwise, original prose, documentation, translations, and non-code teaching assets use [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt), and original code uses [MIT](LICENSES/MIT.txt). Third-party works retain their own terms. See [LICENSE.md](LICENSE.md) for scope and attribution requirements.
