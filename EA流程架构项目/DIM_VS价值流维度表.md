---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-流程维度SCD_Type2
extracted_at: 2026-07-16T11:45:18
---

# DIM_VS价值流维度表

DIM_VS是价值流维度表，每行对应一个价值流（VS）的一个价值阶段（Stage），粒度为VS×Stage。包含价值流编码、阶段编码、退出条件、关联L3等字段。主键为vs_key（自增序列）。

## 关联概念

- [[FACT_CARD事实表]]
- [[DIM_PROCESS维度表]]
