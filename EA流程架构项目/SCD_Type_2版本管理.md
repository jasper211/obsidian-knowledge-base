---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V2_项目交付.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-流程维度SCD_Type2
extracted_at: 2026-07-16T11:41:39
---

# SCD Type 2版本管理

DIM_PROCESS维度表采用SCD Type 2策略管理L4定义的历史版本。每次L4定义变更（如里程碑升版）时新建一行，版本号+1，旧版valid_to设为新版生效日期，is_current设为FALSE。同一l4_code只能有一条is_current=TRUE的记录。

## 关联概念

- [[DIM_PROCESS维度表]]
- [[L4活动]]
