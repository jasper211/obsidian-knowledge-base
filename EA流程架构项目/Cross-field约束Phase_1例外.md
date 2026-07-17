---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-cross-field约束与默认值冲突
extracted_at: 2026-07-16T13:52:28
---

# Cross-field约束Phase 1例外

字典层临时加注释'Phase 1例外，警告不阻断'。具体：agentifiability='Auto'且已完成时agent_assist_flag允许FALSE；execution_status='完成'但end_date缺失允许NULL。DB CHECK约束不加硬限制，只在ETL日志中输出警告。

## 关联概念

- [[fact_card]]
- [[agent_assist_flag]]
- [[end_date]]
- [[execution_status]]
