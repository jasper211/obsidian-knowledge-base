---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/项目规划/数据字典_流程数据库数据字典_V1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: SLA时限管理
extracted_at: 2026-07-16T12:34:44
---

# SLA违规自动计算

FACT_CARD 的 sla_breach_flag 为 GENERATED ALWAYS AS (duration_hours > sla_hours_actual) STORED，不允许手工修改；任一值为 NULL 时结果也为 NULL。

## 关联概念

- [[FACT_CARD]]

## 所属枢纽

- [[SLA时限管理]]
