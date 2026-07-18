---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: sla_hours_actual复制
extracted_at: 2026-07-16T13:52:28
---

# sla_hours_actual复制时机

sla_hours_actual按valid_from <= record_date < valid_to取历史快照，而非当前最新版。字典FC-020备注已明确此意图。Phase 1回填2026 Q1-Q2历史保单时，取历史SLA版本。

## 关联概念

- [[sla_hours_actual]]
- [[dim_process]]
- [[fact_card]]

## 所属枢纽

- [[sla_hours_actual复制]]
