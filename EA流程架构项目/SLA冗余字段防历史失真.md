---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: SLA时限管理
extracted_at: 2026-07-16T11:45:19
---

# SLA冗余字段防历史失真

FACT_CARD中sla_hours_actual字段在记录写入时从DIM_PROCESS.sla_hours复制，之后DIM_PROCESS版本更新时该字段不随之变更，以保留历史SLA标准，防止历史数据失真。

## 关联概念

- [[FACT_CARD事实表]]
- [[DIM_PROCESS维度表]]

## 所属枢纽

- [[SLA时限管理]]
