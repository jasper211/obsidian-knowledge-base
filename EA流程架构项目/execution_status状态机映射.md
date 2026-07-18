---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: 续保账单状态归并
extracted_at: 2026-07-16T13:52:26
---

# execution_status状态机映射

建议的映射：生效→完成，取消投保→阻断，退保→阻断，尚欠保费→进行中，已签单→完成，排期→进行中，pending→进行中，搁置受保→阻断，待批核→进行中，NULL→进行中（默认）。需Mark确认后写入字典V2.0。

## 关联概念

- [[execution_status]]
- [[FACT_POLICY]]
- [[fact_card字典V2.0]]

## 所属枢纽

- [[续保账单状态归并]]
