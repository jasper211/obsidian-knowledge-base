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
entity_ref: CLUSTER-批量导入时entry_by规则缺失
extracted_at: 2026-07-16T12:07:24
---

# 批量导入时entry_by规则缺失

字典FC-035只覆盖了三种data_source的entry_by校验，未包含'批量导入'。建议批量导入时entry_by填写类似'CARRIE_BATCH_ETL_20260528'的标识（含时间戳），便于审计。

## 关联概念

- [[entry_by]]
- [[data_source]]
- [[fact_card表]]
