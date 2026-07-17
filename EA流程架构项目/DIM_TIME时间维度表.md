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
entity_ref: CLUSTER-时间维度表待生成
extracted_at: 2026-07-16T11:45:18
---

# DIM_TIME时间维度表

DIM_TIME是时间维度表，由脚本自动生成，覆盖2024-01-01至2027-12-31（约1461行）。主键为time_key（YYYYMMDD整数格式），包含年、季、月、周、星期几等字段。

## 关联概念

- [[FACT_CARD事实表]]
