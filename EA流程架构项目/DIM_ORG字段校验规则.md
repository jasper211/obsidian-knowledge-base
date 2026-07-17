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
extracted_at: 2026-07-16T11:45:23
---

# DIM_ORG字段校验规则

DIM_ORG各字段有严格校验规则，例如：position_family枚举值为A/B/C/D/E/F/G/职能；headcount_target_min≤headcount_target_max；全公司mark_retained=TRUE的岗位不超过11条。

## 关联概念

- [[DIM_ORG维度表]]
