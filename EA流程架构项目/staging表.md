---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/任务状态/EA综合审计与EEIE接入计划_v0.1_2026-06-26.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-06-26
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-EA内容不可直接写入EEIE_production
extracted_at: 2026-07-16T12:10:41
---

# staging表

EA数据在未通过接入门前，先进入staging表而非production truth。staging表包括：ea_value_node_staging、ea_value_node_l3_relation_staging、ea_change_event_staging、ie_rule_signal_staging、ie_interview_lead、ie_gap_candidate、ie_action_item_pending、ie_decision_pending、ee_artifact_staging。

## 关联概念

- [[EE/IE接入原则]]
- [[晋升门控]]
