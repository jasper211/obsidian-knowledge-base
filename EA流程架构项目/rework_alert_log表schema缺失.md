---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 非正式主题
entity_ref: 返工预警表
extracted_at: 2026-07-16T12:07:21
---

# rework_alert_log表schema缺失

字典FC-022提到rework_count>=3时自动触发预警并写入rework_alert_log表，但该表的字段集和触发器DDL未在字典中定义。需要明确表schema、触发器类型（BEFORE/AFTER INSERT、行级/语句级）以及批量UPSERT时的触发行为。Phase 1 默认rework_count为0，不会触发，但仍需确认对象正确。

## 关联概念

- [[rework_alert_log表]]
- [[trg_rework_alert触发器]]
- [[fact_card表]]

## 所属枢纽

- [[返工预警表]]
