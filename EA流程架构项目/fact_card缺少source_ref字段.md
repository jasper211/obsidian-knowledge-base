---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 非正式主题
entity_ref: fact_card溯源
extracted_at: 2026-07-16T12:07:24
---

# fact_card缺少source_ref字段

DIM_PROCESS有source_notes用于溯源，但fact_card没有。Phase 1批量灌数时希望标注派生来源（如policy_id）。选项：用entry_by+data_source+batch_id足够、新增source_ref字段、或用batch_id关联ETL_LOG表。

## 关联概念

- [[source_ref]]
- [[fact_card表]]
- [[batch_id]]

## 所属枢纽

- [[fact_card溯源]]
