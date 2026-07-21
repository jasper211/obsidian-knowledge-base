---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/三大主Agent体系架构_v1.2.md
extracted_at: 2026-07-20T12:22:28
---

# PTA两条能力线

PTA（项目任务协同Agent）包含两条独立但共享底层工具的能力线：①被动执行（Think-Act-Observe主循环），响应自然语言指令，包含意图解析、执行编排、进度追踪、归档复盘，仅显式--sync时执行git push；②主动巡检（daily_sensing），独立入口--daily-scan，每天定时自动运行，通过本地文件sha256 diff和LLM关系分析建议任务铸造，执行前需人工确认。

## 关联概念

- [[PTA]]
- [[daily_sensing]]
- [[Think-Act-Observe]]


---
⚠️ **待复核**：源文档「05_Agent库/草稿/三大主Agent体系架构_v1.2.md」已被删除（标记时间：2026-07-21T02:00:44）
