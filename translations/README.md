# Translation status / 翻译状态

| Language | Status |
| --- | --- |
| 简体中文 | Scope, provisional five-part, twenty-chapter outline and Chapters 6, 9, and 13 discussion drafts available; sample scenarios untested |
| English | Project introduction and Chapter 13 discussion draft available; AI translation revised for natural English and beginner comprehension; human review pending |
| Other languages | Planned; not yet selected |

中文正文称呼与英文概念按 [术语表](../docs/terminology.md) 对应，产品名保留官方写法。[中文样章](../book/zh-CN/13-working-with-a-stuck-assistant.md) 和 [英文译稿](../book/en/13-working-with-a-stuck-assistant.md) 已入库，教学情境尚未实测。英文样章用于讨论，原文仍在修订；完整多语言版本待原文与案例稳定后推进。译文需要解释当地工具、日期与数字格式、文件习惯和流程差异。

[第 6 章](../book/zh-CN/06-what-the-agent-knows.md) 与 [第 9 章](../book/zh-CN/09-choosing-libraries-with-an-agent.md) 中文样章已入库，尚无英文译稿。

## Chapter 13 source and review

| Item | Record |
| --- | --- |
| Translation | [When Repeated Fixes Don't Work](../book/en/13-working-with-a-stuck-assistant.md) |
| Source file | [book/zh-CN/13-working-with-a-stuck-assistant.md](../book/zh-CN/13-working-with-a-stuck-assistant.md) |
| Source commit | [`c0668856ad738e66130b3463213538b1bc860123`](https://github.com/YannByte/ai-coding-for-everyone/blob/c0668856ad738e66130b3463213538b1bc860123/book/zh-CN/13-working-with-a-stuck-assistant.md) |
| Review | AI bilingual review of the shortened drafts completed on October 18, 2026; human translation review and target-reader review pending |
| Review record | [Current concise-draft review](reviews/working-with-a-stuck-assistant-en-concise-2026-10-18.md) |

Both editions follow four sections: describe the problem, investigate from results, intervene when fixes fail, and verify the requirement. Recovery and handoff are condensed within the intervention section. File and folder names remain in Chinese, with English labels, so both editions refer to the same sample. The scenario, expected files, task boundaries, recovery conditions, and source links remain aligned. No runnable exercise or successful trial is implied.

Recheck the translation when the Chinese source changes. A repository check does not certify translation fidelity or reader understanding. The repository name is not a finalized English book title.

版本、文件哈希和人工审阅状态登记在 [翻译清单](manifest.json)，由统一检查入口核对。原文或译文变更后，先复核影响，再创建对应版本的审阅记录并更新清单。程序只能检查记录一致性，不能证明人工审阅已经发生。
