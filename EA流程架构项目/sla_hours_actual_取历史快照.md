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
entity_ref: sla_hours_actual复制
extracted_at: 2026-07-16T12:13:49
---

# sla_hours_actual 取历史快照

fact_card 的 sla_hours_actual 字段在 DIM_PROCESS 版本更新时不随之变更，应取历史快照：按 valid_from <= record_date < valid_to 条件获取对应版本的 SLA 值。Phase 1 回填历史保单时使用历史 SLA 版本。

## 关联概念

- [[fact_card]]
- [[dim_process]]

## 所属枢纽

- [[sla_hours_actual复制]]
