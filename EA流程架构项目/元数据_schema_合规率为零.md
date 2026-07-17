---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 00_治理与元模型/治理日志/治理审计报告_2026-06-25.md
authority_layer: 00_治理
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-06-25
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-治理性发现非技术问题
extracted_at: 2026-07-16T11:18:19
---

# 元数据 schema 合规率为零

官方 doc-meta-schema.yaml 规定的 8 个英文必填字段（owner/status/source/valid_until 等）在全库 02/03 层合规率为 0%，实际使用三套中文键方言，valid_until 字段出现 0 次，导致衰减治理无信号。应统一 schema 并同步校验逻辑。

## 关联概念

- [[元数据治理]]
- [[衰减治理]]
