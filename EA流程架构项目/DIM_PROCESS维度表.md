---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 流程维度SCD
extracted_at: 2026-07-16T11:45:18
---

# DIM_PROCESS维度表

DIM_PROCESS是流程维度表，覆盖L1至L5完整层级，包含Agent化6维评分（D1-D6，总分0-18）。采用SCD Type 2策略，保留历史版本。主键为process_key（自增序列）。

## 关联概念

- [[FACT_CARD事实表]]
- [[Agent化6维评分]]

## 所属枢纽

- [[流程维度SCD]]
