# 第 13 章样章第二轮审阅：facts

任务：`working-with-a-stuck-assistant`。
日期：2026 年 10 月 17 日。
审阅者：AI（Codex），不代表人工读者反馈。
正文：[中文样章](../zh-CN/13-working-with-a-stuck-assistant.md)。
正文 SHA-256：`dd198c484168266ef5f40d490707b9ae85b232a7ad922c2c22f9ba47e141627f`。
类型：`facts`。
结论：`needs-work`。

本轮依据完善后的写作规范与术语表，检查相对提交 `20f5c1c` 的改动及全文上下文。此前记录保留为历史。

## 问题与修改

「回退会把文件恢复到之前的状态」混合了不同恢复操作的效果。已去掉统一效果断言，要求先明确方法、文件和受影响工作，不补写未经验证的 Git 命令。

预期保持三份指定 PDF、一份被排除的 PNG；文件名与目录层级未改变。新增「只核对数量不足」「无法启动不等于检出遗漏」是对本情境验收逻辑的说明，不是新增运行观察。示例表格、报告与交接记录仍明确属于教学设定。

## 来源核对

2026 年 10 月 17 日重新阅读 [Claude Code 官方最佳实践](https://code.claude.com/docs/en/best-practices) 的 Give Claude a way to verify its work，以及 [Anthropic 长任务工程文章](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) 的 Incremental progress、Getting up to speed。正文只用它们支撑可执行检查、结果证据及交接记录的实践建议，没有把产品经验扩大为所有工具的能力或本书的成效。

基础概念按 [术语表](../../docs/terminology.md) 中的官方出处与适用范围核对。本轮没有新增数字、时间承诺、成功率或实测结果；原证据条目的状态仍适用。

## 尚需验证

文件清单工具没有实现，未选定产品与版本，也没有运行记录、作者试做或读者试做。尚不能验证界面操作、筛选故障及修复过程是否符合真实案例。保留 needs-work；本轮事实审阅不代替实践验证。
