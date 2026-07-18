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
entity_ref: cross-field约束例外
extracted_at: 2026-07-16T12:07:23
---

# cross-field约束与默认值冲突

字典FC-028要求agentifiability='Auto'且活动完成时agent_assist_flag须为TRUE，但Mark D1让G段全FALSE默认。Phase 1需处理此冲突：临时注释例外、DB CHECK不强制、或用data_source='批量导入'触发例外分支。类似冲突还有FC-007与FC-028联动、FC-018与FC-016联动。

## 关联概念

- [[agent_assist_flag]]
- [[agentifiability]]
- [[data_source]]

## 所属枢纽

- [[cross-field约束例外]]
