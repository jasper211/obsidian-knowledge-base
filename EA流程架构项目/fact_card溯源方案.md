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
entity_ref: CLUSTER-fact_card_不新增_source_notes
extracted_at: 2026-07-16T13:52:29
---

# fact_card溯源方案

不使用source_notes字段，而是用batch_id关联etl_batch_detail辅助表实现溯源。etl_batch_detail包含batch_id、target_table、target_card_id、source_table、source_key、etl_time字段。避免事实表膨胀。

## 关联概念

- [[fact_card]]
- [[batch_id]]
- [[etl_batch_detail]]
