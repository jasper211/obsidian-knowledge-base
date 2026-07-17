---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-缺L4的deliverable_key处理
extracted_at: 2026-07-16T12:07:20
---

# dim_deliverable缺25个L4

dim_process 有425个L4，但 dim_deliverable 只有400行，对应400个distinct L4，即25个L4没有对应的交付物记录。这与字典“一L4一deliverable”原则矛盾。Phase 1 灌 fact_card 时，这25个L4的 deliverable_key 可留NULL（字典FC-010允许），或先补全 dim_deliverable。

## 关联概念

- [[dim_deliverable表]]
- [[dim_process表]]
- [[L4交付物原则]]
