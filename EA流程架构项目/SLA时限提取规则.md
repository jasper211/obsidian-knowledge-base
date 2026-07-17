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
entity_ref: CLUSTER-SLA时限提取规则
extracted_at: 2026-07-16T11:45:20
---

# SLA时限提取规则

DIM_PROCESS.sla_hours从L3协同框架.txt中提取，须注明来源段落。若协同框架未定义SLA，允许为NULL（初始化阶段），此时FACT_CARD的sla_breach_flag自动为NULL。

## 关联概念

- [[DIM_PROCESS维度表]]
- [[sla_hours字段]]
