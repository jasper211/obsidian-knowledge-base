---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/EA_Confirmation_Interview_Pack_v1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 字段补齐
extracted_at: 2026-07-16T12:14:53
---

# reviewed draft写入底线

只要reviewed_draft_requires_user_confirmation还存在，就不能将数据写入EE/IE production truth。只要VN-JOPD-01仍有replacement_node_requires_field_backfill，THBOB/JOPD合并就只能停留在reviewed draft。

## 关联概念

- [[reviewed_draft_requires_user_confirmation]]
- [[VN-JOPD-01]]
- [[replacement_node_requires_field_backfill]]

## 所属枢纽

- [[字段补齐]]
