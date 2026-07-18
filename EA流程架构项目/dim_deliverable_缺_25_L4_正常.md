---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529_修正版.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: dim_deliverable缺L4
extracted_at: 2026-07-16T12:13:48
---

# dim_deliverable 缺 25 L4 正常

dim_process 有 425 个 L4，但 dim_deliverable 只有 400 行，缺失 25 个 L4 的交付物记录是正常过渡状态，因为 L3/L4 定义仍在演进。Phase 1 允许这 25 个 L4 的 deliverable_key 留 NULL，不需要先补足 dim_deliverable 再灌 fact_card。

## 关联概念

- [[dim_deliverable]]
- [[dim_process]]
- [[fact_card]]

## 所属枢纽

- [[dim_deliverable缺L4]]
