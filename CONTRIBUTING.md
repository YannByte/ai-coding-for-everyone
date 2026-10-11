# Contributing / 参与贡献

The book is in preparation. Feedback on everyday work problems, unclear explanations, and case requirements is welcome in Chinese or English.

欢迎通过 Issue 提出具体工作问题、纠错和阅读反馈。说明原来怎样处理、哪里反复费力、期望什么结果，以及已有软件为什么没有满足要求。

不要提交个人、客户或单位的非公开材料。需要样例时，使用明确标注的自制数据，保留问题的结构即可。

修改文档可提交 Pull Request，说明修改原因。较大的案例扩展或整章翻译，建议先通过 Issue 讨论，避免与正在变化的书稿重复劳动。

贡献须为你有权提交的内容。引用外部作品请注明来源与许可。被接纳的书稿、文档和教学素材遵循 CC BY-SA 4.0，代码遵循 MIT；第三方内容保留适用的原许可。

By contributing, you agree to license your contribution under the applicable terms described in [LICENSE.md](LICENSE.md). Do not submit material you lack permission to share.

## 仓库协作与检查

协作规则从 [AGENTS.md](AGENTS.md) 按任务读取。书稿、案例和翻译各有范围内的说明，公共材料政策见 [公开内容范围](docs/publication-scope.md)。

中文撰写、改写与审阅使用仓库内的 [中文写作技能](.agents/skills/tech-doc-style-chinese/SKILL.md) 和 [本书覆盖说明](docs/chinese-writing.md)，无需另行安装全局技能。上游技能保留原 MIT 许可，本书的语气和案例要求在覆盖说明中维护。

书稿、案例和练习按 [本书的写作方法](docs/writing-method.md) 起草与审阅，用 [术语表](docs/terminology.md) 保持概念一致。提交正文修改时，说明影响的读者判断或操作；涉及试读、试做时，记录验证范围和仍未解决的问题。

修改现有仓库使用独立分支，只提交本次任务文件。提交前在仓库根目录运行：

```sh
python3 scripts/check_repo.py
git diff --check
```

检查需要 Git 与 Python 3.11 或以上版本，无需安装第三方依赖。它检查文件链接、指令篇幅、常见私人路径和凭据标记，以及案例素材登记，并运行检查器自身的回归测试。CI 使用同一入口。

链接检查覆盖 Markdown 行内链接及引用定义中的相对文件目标，忽略代码围栏；不检查远程网址、页内锚点或 HTML 链接。自动检查不能判断事实、许可有效性、写作质量或实际使用效果，发布前仍需按任务审阅。
