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
entity_ref: cross-field约束例外
extracted_at: 2026-07-16T12:13:50
---

# Phase 1 例外处理规则

对于字典中的跨字段约束与 Mark D1 默认值冲突的情况，Phase 1 允许例外处理：agent_assist_flag 在 agentifiability='Auto' 且已完成时可为 FALSE；end_date 在 execution_status='完成' 时可为 NULL。DB CHECK 约束不强制，由 ETL 做例外标记。

## 关联概念

- [[fact_card]]

## 所属枢纽

- [[cross-field约束例外]]
