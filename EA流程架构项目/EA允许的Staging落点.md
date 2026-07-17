---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/EA_EEIE_接入冻结声明_v1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-EA内容不可直接写入EEIE_production
extracted_at: 2026-07-16T12:03:46
---

# EA允许的Staging落点

EA各对象仅允许写入指定的staging或pending表：D1入ea_value_node_staging(candidate)，D2入ea_value_node_l3_relation_staging(candidate)，D3入ea_change_event_staging(candidate)，T2入ie_rule_signal_staging(candidate)，T3入ie_interview_lead(pending)，T4入ie_action_item_pending(pending)，T6入ee_artifact_staging(candidate)，T7入ie_gap_candidate(candidate)，T8入ie_decision_pending(pending)。

## 关联概念

- [[Staging表]]
- [[Candidate状态]]
- [[Pending状态]]
