---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-流程维度SCD_Type2
extracted_at: 2026-07-16T11:45:22
---

# DIM_VS字段校验规则

DIM_VS各字段有严格校验规则，例如：vs_stakeholder禁止填写内部角色；stage_sequence在同一vs_code内从1连续递增；l3_primary格式为^L3-[A-Z]{2,6}$且须存在于DIM_PROCESS。

## 关联概念

- [[DIM_VS维度表]]
