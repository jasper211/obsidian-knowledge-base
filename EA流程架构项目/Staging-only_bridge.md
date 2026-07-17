---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/EA_to_EEIE_Staging_Data_Contract_v1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-EA内容不可直接写入EEIE_production
extracted_at: 2026-07-16T12:09:12
---

# Staging-only bridge

EA to EE/IE data contract defines a staging-only bridge from EA value-node content to EE/IE. It does not authorize production truth writes. Import scripts must write only staging tables until a separate promotion manifest is signed off.

## 关联概念

- [[Promotion gates]]
- [[Node promotion status]]
