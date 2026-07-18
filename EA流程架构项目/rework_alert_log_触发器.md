---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529_修正版.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: 返工预警表
extracted_at: 2026-07-16T12:13:48
---

# rework_alert_log 触发器

rework_alert_log 表由触发器 trg_rework_alert 在 fact_card 表 AFTER INSERT OR UPDATE 时行级触发，当 rework_count >= 3 时插入告警记录。该触发器非幂等，但 Phase 1 中 rework_count 全为 0，不会触发。

## 关联概念

- [[fact_card]]
- [[rework_alert_log]]

## 所属枢纽

- [[返工预警表]]
