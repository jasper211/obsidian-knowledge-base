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
entity_ref: CLUSTER-SLA时限提取规则
extracted_at: 2026-07-16T11:41:40
---

# SLA自动计算与历史保留

FACT_CARD中的sla_hours_actual字段在记录写入时从DIM_PROCESS.sla_hours自动复制，作为冗余字段保留历史标准。当DIM_PROCESS版本更新时，sla_hours_actual不随之变更，防止历史数据失真。sla_breach_flag为GENERATED ALWAYS字段，自动计算duration_hours > sla_hours_actual的结果，不允许手工修改。

## 关联概念

- [[FACT_CARD事实表]]
- [[DIM_PROCESS维度表]]
