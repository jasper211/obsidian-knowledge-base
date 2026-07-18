---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 非正式主题
entity_ref: 映射缺失与规则
extracted_at: 2026-07-16T12:07:21
---

# FACT_POLICY到l4_code映射缺失

字典FC-012说l4_code从DIM_PROCESS复制，但FACT_POLICY（保单）与DIM_PROCESS（L4）的映射规则未定义。例如，保单签约对应哪个L4-COM-???。需要制定(policy_status, business_category)到l4_code的映射表，由Terresa或Mark负责。

## 关联概念

- [[FACT_POLICY表]]
- [[dim_process表]]
- [[l4_code]]

## 所属枢纽

- [[映射缺失与规则]]
