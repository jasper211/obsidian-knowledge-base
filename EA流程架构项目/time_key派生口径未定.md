---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 非正式主题
entity_ref: time_key派生口径_time_key派生口径
extracted_at: 2026-07-16T12:07:22
---

# time_key派生口径未定

字典FC-006说time_key按start_date自动转换，但FC-017 start_date是手工录入，Phase 1批量回填时start_date可能缺失。需要确定fallback：使用record_date、FACT_POLICY的某个日期，或允许NULL（但FC-006校验要求必须存在于DIM_TIME，暗示NOT NULL）。

## 关联概念

- [[time_key]]
- [[start_date]]
- [[dim_time表]]

## 所属枢纽

- [[time_key派生口径]]
