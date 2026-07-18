---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529_修正版.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: org_key处理
extracted_at: 2026-07-16T12:13:49
---

# org_key Phase 1 全 NULL

由于 dim_org 实际只有 8 行（岗位族级），粒度太粗无法直接映射到保单的 partner_code，且缺少 partner_code → org_key 对照表，因此 Phase 1 中 fact_card 的 org_key 全部设为 NULL，待 GAP-01 完成后统一补映射。

## 关联概念

- [[dim_org]]
- [[fact_card]]

## 所属枢纽

- [[org_key处理]]
