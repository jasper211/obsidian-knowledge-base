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

# DIM_TIME字段校验规则

DIM_TIME各字段有严格校验规则，例如：time_key格式为YYYYMMDD 8位整数；quarter介于1-4；month介于1-12；week介于1-53；day_of_week 1=周一，7=周日。

## 关联概念

- [[DIM_TIME维度表]]
