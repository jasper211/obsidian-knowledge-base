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
entity_ref: CLUSTER-org_key_Phase_1处理
extracted_at: 2026-07-16T13:52:27
---

# org_key Phase 1处理

Phase 1中org_key全部NULL，等GAP-01完成后统一补映射。理由：dim_org实际粒度为岗位族级（8行），无法直接映射到保单的partner_code，精确映射需要一张partner_code→org_key对照表，目前不存在。

## 关联概念

- [[org_key]]
- [[dim_org]]
- [[fact_card]]
