---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/EA_Post_Interview_Writeback_Runbook_v1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-EA内容不可直接写入EEIE_production
extracted_at: 2026-07-16T12:06:54
---

# EE和IE写入包分离

EE和IE写入包不能混成一个表。EE包含value node/asset/fact/evidence对象写入包；IE包含workflow/gate/action/decision/backlog写入包。EE是对象事实，IE是流程治理。

## 关联概念

- [[EE/IE写入包生成]]
