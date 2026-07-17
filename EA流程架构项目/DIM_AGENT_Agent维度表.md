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
entity_ref: CLUSTER-dim_process.agentifiability字段不可信
extracted_at: 2026-07-16T11:45:18
---

# DIM_AGENT Agent维度表

DIM_AGENT是Agent维度表，记录Agent的编码、名称、处理模式（Auto/Aug/Hybrid）、建设状态等。主键为agent_key（自增序列）。

## 关联概念

- [[FACT_CARD事实表]]
- [[Agent化6维评分]]
