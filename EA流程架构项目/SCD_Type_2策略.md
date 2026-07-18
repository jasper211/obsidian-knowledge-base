---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 流程维度SCD
extracted_at: 2026-07-16T11:45:19
---

# SCD Type 2策略

DIM_PROCESS表采用SCD Type 2策略：L4定义变更时新建一行，版本号+1，旧行is_current设为FALSE，新行is_current=TRUE。同一l4_code只能有一条is_current=TRUE的记录。

## 关联概念

- [[DIM_PROCESS维度表]]
- [[version字段]]

## 所属枢纽

- [[流程维度SCD]]
