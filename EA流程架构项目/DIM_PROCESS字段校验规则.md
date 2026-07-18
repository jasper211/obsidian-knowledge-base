---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 流程维度SCD
extracted_at: 2026-07-16T11:45:22
---

# DIM_PROCESS字段校验规则

DIM_PROCESS各字段有严格校验规则，例如：l3_code格式为^L3-[A-Z]{2,6}$；l4_code格式为^L4-[A-Z]{2,6}-\d{2}[a-z]?$；agent_score_total须等于D1~D6之和；同一l4_code只能有一条is_current=TRUE。

## 关联概念

- [[DIM_PROCESS维度表]]

## 所属枢纽

- [[流程维度SCD]]
