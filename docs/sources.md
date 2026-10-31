# 参考来源

以下资料来自此前的方向研究，不能替代本书实验或目标读者验证。当前方向为有无编程经验的读者使用 AI 编程助手；Agent 系统开发书籍仅保留为背景对照，不再据此组织全书。具体产品的使用文档与实践来源须在选定任务和工具后补充核对。书籍核对范围为公开目录与介绍，教程和工程文章参考公开内容；尚未复现配套代码。

| 来源 | 当前用途 | 证据边界 |
| --- | --- | --- |
| [子木：AI 工具站 SEO 小册子](https://github.com/JeffLi1993/saas-seo-playbook) | 明确读者、按做事顺序组织章节、兼顾顺序阅读和问题查阅 | 参考已公开前言、章节与大纲；后续章节仍在补全，不代表效果验证 |
| [Tw93：你不知道的 AI Coding：非技术人的上手、场景与实战](https://tw93.fun/2026-04-26/ai-coding.html) | 2026 年 10 月 18 日核读；参考「做一个只给你一个人用的软件」「怎么确认它真的做对了」及排版实例，从手头材料进入对话、试做和核对 | 作者经验与示例，未复现；本书从对话逐步澄清需求，不要求新手预先写出技术规格，不采用固定完成时间或必定正确的表述 |
| [AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | 对照评估与 AI 系统工程范围 | 公开目录与介绍，不宣称已通读 |
| [AI Agents in Action 第二版](https://www.manning.com/books/ai-agents-in-action-second-edition) | 对照从实现到评估的教学安排 | 公开内容，不证明本书需要重复其结构 |
| [Multi-Agent AI Engineering](https://www.oreilly.com/library/view/multi-agent-ai-engineering/9781806690879/) | 对照评估、可观测性与改进的重合范围 | 对照目录；多 Agent 的结论需判断是否适用 |
| [Hello-Agents](https://github.com/datawhalechina/hello-agents) | 对照中文原理、实践和评估教程 | 阅读公开目录和评估章节，未运行代码 |
| [Hugging Face 观察与评估实践](https://huggingface.co/learn/agents-course/en/bonus-unit2/monitoring-and-evaluating-agents-notebook) | 研究观察与评估练习的组织方式 | 未复现实验 |
| [Anthropic：Agent 评估](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | 任务、轨迹、最终结果、重复运行与回归 | 团队实践与方法说明，不保证对所有项目有效 |
| [Anthropic：工具设计与评估](https://www.anthropic.com/engineering/writing-tools-for-agents) | 工具契约、返回内容与独立评估 | 来源报告的实验不转写成本书亲历 |
| [Engineering Reliable Coding Agents](https://arxiv.org/abs/2608.13867) | 编程 Agent 的系统可靠性研究线索 | 公开研究专著，需逐项核对证据和适用范围 |

章节起草时将实际引用的说法、具体定位和核实状态登记到证据清单，不能仅凭列入本页就标记 verified。引用第三方代码或素材另行核对许可。

## 当前样章来源

第 1 章从不会编程的读者找培训通知的情境进入，文件和对话均为未实测教学设计。起步组织参考上述 Tw93 文章；工具执行与反馈依据 [Claude Code 工作方式](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop) 的 The agentic loop、Tools 部分（2026 年 10 月 18 日核读），不推断所有产品具有相同访问范围或文件处理能力。

第 6 章讨论当前上下文、按需读取、对话压缩和冲突规则。2026 年 10 月 18 日核对以下来源；同名文件情境仍为未实测的教学设计。

| 来源 | 使用位置 | 限制 |
| --- | --- | --- |
| [Anthropic：上下文工程](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 当前信息、按需读取、压缩与持久记录 | 不断言全部工具采用同一方式，不给出效果承诺 |
| [Git commit](https://git-scm.com/docs/git-commit)、[Git restore](https://git-scm.com/docs/git-restore) | 用提交保留历史，从当前项目移除过期文档 | 仅能据保留的历史找回已记录内容，不覆盖未提交的新文件或修改 |
| [Lost in the Middle](https://arxiv.org/abs/2307.03172) | 可容纳信息不等于能稳定使用 | 核读 2023 年论文摘要；多文档问答与键值检索，不推断当前编程故障原因 |
| [Claude Code：项目记忆](https://code.claude.com/docs/en/memory) | 规则与记忆加载、过期要求和非强制执行性质 | 产品实践说明；清理与验证办法为编辑建议，具体加载行为另按版本检查 |

第 13 章讨论让助手完成调查、修复、验证，以及根据执行反馈调整任务和交接。来源只支持相应实践建议，不证明教学情境已经运行成功。具体说法与核实范围登记在 [证据清单](../book/evidence.json)。

| 来源 | 使用位置 | 限制 |
| --- | --- | --- |
| [Claude Code 官方最佳实践](https://code.claude.com/docs/en/best-practices) | 可执行检查与验证结果 | 产品实践指导，不能推定所有助手具备相同条件 |
| [Anthropic：长任务工程实践](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 进度记录、版本历史与跨会话交接 | 特定工程实验，不是本书读者效果证据 |

第 9 章讨论为什么复杂能力应优先复用成熟开源实现，再由助手补齐需求。区分生成、执行反馈与项目测试积累，解释复用的依据和局限。以下资料用于核对能力与概念，不代表已完成本项目选型或试做。核对日期：2026 年 10 月 18 日。

| 来源 | 使用位置 | 限制 |
| --- | --- | --- |
| [Chen 等：代码模型研究，第 2 节](https://arxiv.org/html/2107.03374v2) | 区分代码生成与通过运行测试评价功能 | 2021 年研究，不据其成绩评价当前工具 |
| [Anthropic：上下文工程](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 当前信息、主动检索与上下文管理 | 工程指导，不直接证明教学情境中的错误原因 |
| [pypdf 测试文档](https://pypdf.readthedocs.io/en/stable/dev/testing.html) | 样本测试与旧问题编号关联 | 未运行项目测试，不证明所有输入已覆盖 |
| [GitHub：仓库许可](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) | 区分公开可见与许可授权 | 不能替代具体项目许可核查 |
| [pypdf 官方介绍](https://pypdf.readthedocs.io/en/stable/) | 将文字提取库列入调查候选 | 不等于完成维护、兼容性或许可审查 |
| [pypdf 文字提取说明](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) | 文字层、扫描图像与 OCR 的边界 | 未在教学样本上运行，不作效果承诺 |
| [PyPA 依赖规范](https://packaging.python.org/en/latest/specifications/dependency-specifiers/) | 依赖的版本与环境要求 | 保存配置本身不保证可重复运行 |

两篇样章另参考 [Claude Code 工作方式](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop) 的工具反馈过程（2026 年 10 月 18 日核对）。用于说明助手怎样根据执行结果继续工作，不代表本书完成了行为实测。

## 现代编程助手的工作方式

2026 年 10 月 18 日核读以下官方资料，用于校正全书的对话与执行分工。文档描述的能力受产品、运行模式、工具和权限限制，不代表本书案例已实测，也不推断所有助手支持相同功能。

| 来源与定位 | 写作用途 |
| --- | --- |
| [Claude Code：工作方式](https://code.claude.com/docs/en/how-claude-code-works)，The agentic loop、Tools、It's a conversation、Delegate, don't dictate | 一次请求包含多轮工具调用；助手收集上下文、执行、检查，读者给出目标并按需要补充信息，不必预先设计全部步骤 |
| [Cursor：Agent 概览](https://cursor.com/docs/agent/overview)，Tools；[浏览器工具](https://cursor.com/docs/agent/tools/browser) | 助手可通过文件、终端及浏览器工具调查和验证；具备相应工具时，可使用页面操作、截图、控制台和网络记录检查结果 |
| [GitHub：Copilot agents](https://docs.github.com/en/copilot/concepts/agent-capabilities/about-agents/about-github-copilot-agents)，工作方式与运行形式 | 区分对话入口与任务执行；协作、异步和自动触发等形式，不要求读者始终在线逐步指挥 |

## 项目规则、文档与 Skill

2026 年 10 月 18 日核对以下公开资料，用于补强第 10、17 章，并衔接已有的上下文、交接和效果复盘内容。共同的教学取舍是：从实际工作提炼必要记录，用后续任务检验，再合并或删除无效内容。尚未完成本书练习或读者验证；章节起草时再登记具体引用的证据。

| 来源与定位 | 用途 | 证据边界 |
| --- | --- | --- |
| [OpenAI：Best practices](https://learn.chatgpt.com/guides/best-practices)，AGENTS.md 与持续改进部分 | 根据反复出现的问题修正规则，短入口引用专门文档 | 产品实践建议，不把每次纠正都升级为长期规则 |
| [OpenAI：AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)，指令发现与合并部分；[Claude Code：最佳实践](https://code.claude.com/docs/en/best-practices)，Write an effective CLAUDE.md | 核对文件名、作用范围及加载方式；区分长期约定与详细资料 | 分别适用于对应产品；不假设任意文件名会自动加载，修改后须核对是否生效 |
| [OpenAI：Harness engineering](https://openai.com/index/harness-engineering/)，We made repository knowledge the system of record | 简短规则入口、按需查阅文档、用程序检查可明确判断的要求 | 团队工程实践；只借鉴按需组织知识的办法，不照搬其工程规模 |
| [Agent Skills：Best practices](https://agentskills.io/skill-creation/best-practices)，从实际任务提取与渐进改进部分 | 从成功步骤、纠正记录和项目资料提炼 Skill，保留必要知识 | 规范项目的实践指南，不证明本书读者必然受益 |
| [Agent Skills：Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills)，Designing test cases、Running evals、Iterating on the skill | 新会话中换输入验证，比较使用与不使用或新旧版本的结果，按失败证据改进 | 方法参考；少量练习不能证明普遍有效，客观检查仍需人工核对适用性 |
| [Agent Skills：Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)，Designing trigger eval queries | 分别检查该调用与不该调用的任务，区分选用正确与执行成功 | 触发机制依客户端而异；不照搬建议次数和阈值作为读者门槛 |
| [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988v3)，v3 摘要；[On the Impact of AGENTS.md Files](https://arxiv.org/abs/2601.20404v2)，v2 摘要 | 提醒作者区分任务成功、执行时间与成本，用实际任务验证规则价值 | 仅核读摘要，未复现实验；研究的任务、配置和指标不同，不合并为统一效果，也不据此宣称规则必然有效或无效 |

## 写作规范与术语来源

ASD-STE100 的核对版本、范围和本书取舍见 [对照记录](ste100-review.md)。编程术语按 [术语表](terminology.md) 中逐项列出的官方资料核对；其中的新手解释为本项目改写，不冒充官方原文。机器词表保留来源定位，定期随产品与正文变化复核。
