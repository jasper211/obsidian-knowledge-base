---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529_修正版.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-批量导入时entry_by规则缺失
extracted_at: 2026-07-16T12:13:50
---

# 批量导入 entry_by 格式

当 data_source='批量导入' 时，entry_by 字段填写执行者标识，格式建议为 {NAME}_BATCH_ETL_YYYYMMDD，例如 'CARRIE_BATCH_ETL_20260528'，用于审计回查。

## 关联概念

- [[fact_card]]
