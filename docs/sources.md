# 参考来源

以下资料来自此前的方向研究，不能替代本书实验或目标读者验证。当前方向为有无编程经验的读者使用 AI 编程助手；Agent 系统开发书籍仅保留为背景对照，不再据此组织全书。具体产品的使用文档与实践来源须在选定任务和工具后补充核对。书籍核对范围为公开目录与介绍，教程和工程文章参考公开内容；尚未复现配套代码。旧办公案例的来源保留在 [历史来源索引](sources-2026-10-11.md)。

| 来源 | 当前用途 | 证据边界 |
| --- | --- | --- |
| [子木：AI 工具站 SEO 小册子](https://github.com/JeffLi1993/saas-seo-playbook) | 明确读者、按做事顺序组织章节、兼顾顺序阅读和问题查阅 | 参考已公开前言、章节与大纲；后续章节仍在补全，不代表效果验证 |
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

第 13 章讨论完整委托、执行反馈与交接。来源只支持相应实践建议，不证明教学情境已经运行成功。具体说法与核实范围登记在 [证据清单](../book/evidence.json)。

| 来源 | 使用位置 | 限制 |
| --- | --- | --- |
| [Claude Code 官方最佳实践](https://code.claude.com/docs/en/best-practices) | 可执行检查与验证结果 | 产品实践指导，不能推定所有助手具备相同条件 |
| [Anthropic：长任务工程实践](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 进度记录、版本历史与跨会话交接 | 特定工程实验，不是本书读者效果证据 |

第 9 章讨论由助手调查候选库、验证能力边界，再决定是否接入项目。以下资料用于核对能力与概念，不代表已完成本项目选型或试做。核对日期：2026 年 10 月 18 日。

| 来源 | 使用位置 | 限制 |
| --- | --- | --- |
| [Python pathlib](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob) | 先检查标准库已有能力 | 只说明文件遍历能力，不证明 PDF 全文搜索可用 |
| [pypdf 官方介绍](https://pypdf.readthedocs.io/en/stable/) | 将文字提取库列入调查候选 | 不等于完成维护、兼容性或许可审查 |
| [pypdf 文字提取说明](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) | 文字层、扫描图像与 OCR 的边界 | 未在教学样本上运行，不作效果承诺 |
| [PyPA 依赖规范](https://packaging.python.org/en/latest/specifications/dependency-specifiers/) | 依赖的版本与环境要求 | 保存配置本身不保证可重复运行 |

## 写作规范与术语来源

ASD-STE100 的核对版本、范围和本书取舍见 [对照记录](ste100-review.md)。编程术语按 [术语表](terminology.md) 中逐项列出的官方资料核对；其中的新手解释为本项目改写，不冒充官方原文。机器词表保留来源定位，定期随产品与正文变化复核。
