# 本书术语表

本表维护写作和翻译使用的关键概念。同一概念保持同一表达；日常词语不作机械替换。英文栏为翻译对应词，不是英文书名或 ASD-STE100 批准词表。

| 中文首选词 | 英文对应词 | 本书中的含义与边界 |
| --- | --- | --- |
| AI 编程助手 | coding agent | 本书所讨论的编程工具：可在授权范围内读取项目、修改代码、运行程序，并根据结果继续处理任务；具体能力与权限以产品、版本和运行环境为准。英文以 coding agent 为首选，首次解释它是 AI 工具；不把所有 coding assistants 都归为本书讨论的执行型工具 |
| Agent | agent | 根据任务与中间结果选择行动、调用工具并更新状态的系统；不等同于模型本身 |
| 执行轨迹 | execution trace | 一次任务中可观察的调用、返回和状态变化记录；可能存在缺口 |
| 评估 | evaluation | 用明确任务与判定方法检查能力或变化；单次成功不能代表稳定效果 |
| 回归检查 | regression check | 检查修改是否破坏已有能力 |
| AI 编程 | AI-assisted programming | 借助 AI 制作和修改程序，并由使用者核对是否满足需要 |
| 工作工具 | work tool | 帮助读者完成具体电脑工作的成果，可以采用脚本、skill 或小软件等形式 |
| 教学案例 | teaching case | 为解释方法而组织的工作情境；不能仅凭这个名称推断它是真实用户记录 |
| 教学数据 | teaching data | 为练习制作或整理的数据；要注明来源与加工性质 |
| 输入文件 | input file | 某次运行读取的文件；提到多个文件时使用具体文件名 |
| 输出文件 | output file | 某次运行生成的文件；生成成功不等于内容正确 |
| 预期结果 | expected result | 操作前确定、可用于核对的结果；不能称为已取得的成果 |
| 实际结果 | actual result | 某次运行中观察到的结果；说明材料和环境等必要条件 |
| 对照结果 | reference result | 经独立核对、供练习比较的结果；不能只取程序输出作为正确答案 |
| 试做 | author trial | 作者按案例操作并核对结果；不能替代目标读者验证 |
| 试读 | reader review | 符合定位的读者阅读并反馈理解情况；不表示执行过操作 |
| 读者试做 | reader trial | 符合定位的读者动手完成案例；记录是否获得帮助 |
| 开源软件 | open source software | 按许可允许使用、修改和分发的软件；公开可见代码不等于获得任意使用授权，也不保证成熟度。依据 [GitHub 仓库许可说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)，2026 年 10 月 18 日核对 |
| 库 | library | 程序可以复用的现成代码；首次出现时结合所解决的工作解释 |
| skill | skill | 供 AI 工具按任务使用的指令及配套资源；具体用途和支持环境随案例说明 |

## 面向读者的称呼

- 中文正文以「AI 编程助手」为主要称呼。上下文明确后可简称「助手」或用「它」指代；有多个助手或可能与人类助手混淆时，写明对象。
- 首次介绍时解释执行能力，并提供英文检索入口：本书使用的 AI 编程助手，可以在授权范围内读取项目、修改代码、运行程序，并根据结果继续处理任务。英文使用 coding agent，例如 Codex 和 Claude Code。后文不反复堆叠中英文全称。
- 解释工作机制、工具调用或多 Agent 协作时，可以使用「Agent」，首次出现时说明含义；需要中文术语对照时使用「智能体」。不要为了换词，在普通叙述中交替使用「代理」「智能体」「编程 Agent」。
- 涉及某款产品的操作、界面和实测记录时，使用具体产品名，如 Codex、Claude Code。涉及 Claude Code 的操作不简称为 Claude；「Claude」在模型或其他产品语境中按实际含义保留。不能把某款工具的能力推广为所有助手的能力。
- 教学情境没有指定或实测工具时，使用通用称呼，不擅自补上产品名。概念、产品与模型应区分；「使用 AI 编程助手」不等于「开发 Agent 系统」。
- 翻译按概念对应，英文正文主要使用 coding agent，上下文明确后可用 agent。句中采用普通名词的小写形式，标题可按标题格式写 Coding Agent。首次解释 AI 属性；需要强调 AI 属性时可用 AI coding agent，不把这一变体判为错误。正式书名另定。

描述人与助手的任务关系时，按具体动作写「交给助手」「说明任务」「请它调查」「调整任务」。不把「委托」设为本书的核心术语，也不把调查、执行与验证统称为「写提示词」。固定引用和历史记录保留原样。

这些是本书的编辑约定，不是行业统一译名。以下来源于 2026 年 10 月 17 日核对：

| 一手资料 | 实际用法与本书取舍 |
| --- | --- |
| [OpenAI：Code generation](https://developers.openai.com/api/docs/guides/code-generation#use-codex) | 将 Codex 称为 coding agent；支持本书采用这个常用名称，不能据此断言它是唯一标准术语 |
| [Claude Code：Overview](https://code.claude.com/docs/en/overview) | 同页使用 agentic coding tool 和 AI-powered coding assistant；官方也存在不同描述，不把 assistant 一概判错 |
| [Anthropic：Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | 使用 coding agents，并讨论工具执行与环境反馈；本书据此区分 agent、模型和单次回答 |
| [GitHub：coding agent 与 agent mode](https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot/) | 2025 年的官方文章区分两种产品使用方式；说明概念通称不能替代具体功能名，写操作时须重新核对当前产品文档 |

## 编程术语的来源与边界

以下为依据一手资料改写的简明解释，不是逐字摘录或通用标准定义。来源中的语言或产品范围必须保留；首次写进正文时结合当前任务解释。核对日期为 2026 年 10 月 17 日。

| 中文与英文 | 面向本书读者的解释与易混点 | 一手依据 |
| --- | --- | --- |
| 自动测试、测试用例 / automated test, test case | 给程序指定输入，核对它是否产生预期响应；自动测试由代码执行，不等于所有人工检查 | [Python unittest：test case、Basic example](https://docs.python.org/3/library/unittest.html) |
| 依赖 / dependency | 项目需要的其他软件包，可附带版本和适用环境等要求；不能把库、工具和运行环境都当成同一对象 | [PyPA：Dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)；该来源具体讨论 Python 包依赖 |
| 运行环境 / runtime environment | 执行程序所需的软件环境，例如 Node.js 执行 JavaScript；runtime 也可能指「运行时」阶段，需要按语境区分 | [Node.js 官方介绍](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)；这里用产品实例辅助解释，不冒充其通用词典定义 |
| 标准库 / standard library | 随语言官方实现提供的模块等组件；第三方库另行获取，库与包不是在所有语境中都可互换 | [Python glossary：standard library](https://docs.python.org/3/glossary.html#term-standard-library)；组成以具体语言和发行版本为准 |
| 仓库 / repository | 在 Git 中保存版本对象和引用等信息；不能把任意项目文件夹都称为 Git 仓库 | [Git glossary：repository](https://git-scm.com/docs/gitglossary#def_repository) |
| 提交 / commit | 将本次选定的项目状态记录为 Git 历史中的一个版本；本地提交不等于上传、部署或发布 | [Git glossary：commit](https://git-scm.com/docs/gitglossary#def_commit) |
| 工作目录 / working tree | 当前可查看、编辑的项目文件；它与 Git 已记录的历史不同 | [Git glossary：working tree](https://git-scm.com/docs/gitglossary#def_working_tree) |
| 日志 / log | 程序在运行时记录的事件与信息，可用于调查；有日志不等于已经定位原因 | [Python Logging HOWTO：Basic Logging Tutorial](https://docs.python.org/3/howto/logging.html#basic-logging-tutorial) |
| 回归测试 / regression test | 修改后再次检查已有行为，帮助发现新改动造成的破坏；本书「回归检查」还可以包含人工核对 | [Python doctest：Regression testing](https://docs.python.org/3/library/doctest.html#regression-testing)；这是对该实践用途的解释 |
| 撤销提交 / git revert | Git 通过新提交抵消已有提交引入的改动；不等于把全部文件恢复到某个旧版本 | [Git revert：DESCRIPTION](https://git-scm.com/docs/git-revert#_description)；普通叙述中的「回退」须另写具体对象与恢复方式 |

第 9 章新增术语（2026 年 10 月 18 日核对）：光学字符识别 / optical character recognition，简称 OCR，指从图像中识别文字。首次解释时说明用途，后文可使用 OCR；不要与读取 PDF 已有文字层混用。依据 [pypdf 官方文档：OCR vs. Text Extraction](https://pypdf.readthedocs.io/en/stable/user/extract-text.html#ocr-vs-text-extraction)。这是能力类别，不能据此推定某个库支持 OCR。

第 6 章新增概念（2026 年 10 月 18 日核对）：上下文 / context 指模型生成时可用的信息；上下文窗口 / context window 指一次可容纳信息的范围；对话压缩 / compaction 指把旧信息整理压缩后继续使用，摘要可能遗漏细节。依据 [Anthropic 上下文工程](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 的定义、长任务与 Compaction 段落。以上解释不表示项目全部文件已加载，也不表示所有产品有相同压缩与持久记录机制。

## 词汇约束与程序检查

[机器词表](vocabulary.json) 只维护匹配形式、提示等级、语境说明和来源，概念定义以本页为准。没有列入词表的词不自动成为禁词。普通词汇参考 STE，编程术语优先使用相关标准组织或项目的官方资料；找不到可靠依据时标记待核对，不把模型自拟解释登记为权威定义。

| 层次 | 本书规则 | 程序行为 |
| --- | --- | --- |
| 产品固定拼写 | 保留 Claude Code、GitHub 等实际名称；不处理引用与机器标识 | 已登记的明确误拼报错 |
| 概念名称 | 同一对象保持首选称呼，区分产品名、概念与模型 | 变体仅提示核对语境，不自动替换 |
| 初次使用的专业词 | 在读者需要时解释用途、对象和结果，避免循环解释 | 定位首次可见用例；人工判断附近解释是否充分 |
| 普通常用词 | 优先熟悉且意思准确的词，少用空泛动作 | 根据精选词项给建议，保留原义与例外 |

STE Issue 9 词典中的少量选词可供本书借鉴：utilize 对应 use，commence 对应 start，terminate 在表示停止动作时可考虑 stop。词表保留来源条目标识，示例和解释由本项目编写；不收录标准词典全文、定义或例句集。进程、协议、法律术语以及代码标识中的 terminate 不做无条件替换。

词性限制也有取舍。STE 对 check 和 verify 的动词用法另给替代，但本书允许自然的 check the result；重要的是交代检查对象与依据。commit、token、runtime 等专业含义也不能为迁就普通词表而改变。没有核对专业含义的词，暂不增加替换规则。

词表新增条目必须带来源网址、定位、核对日期和适用条件。把表达偏好升级为报错前，必须说明为何无需语境即可判断，并补充正常句、反例和代码/引用保护测试。检查范围与使用方法见 [写作检查](writing-checks.md)。

## 维护范围

新增术语时，先确认它是否表示新概念。需要改名时，检查当前正文、大纲、项目说明、写作规则、案例说明、入口页与译文。历史稿、来源标题、固定引用、界面原文和机器可读标识符保留原样，必要时在旁边解释差异。教学项目选定后另行维护项目名称与标识。
