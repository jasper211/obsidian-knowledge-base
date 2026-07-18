---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 00_治理与元模型/治理日志/治理审计报告_2026-06-25.md
authority_layer: 00_治理
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-06-25
entity_type: 非正式主题
entity_ref: 知识衰减问题
extracted_at: 2026-07-16T11:18:21
---

# valid_until 字段缺失

全库 02/03 层 frontmatter 中 valid_until 字段出现 0 次，导致无法自动识别过期文档，衰减治理无信号。应强制填写 valid_until，并在校验脚本中增加过期检测规则。

## 关联概念

- [[衰减治理]]
- [[元数据治理]]

## 所属枢纽

- [[知识衰减问题]]
