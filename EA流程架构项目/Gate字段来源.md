---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 03_发布成果-交付物/权威数据/T1_nodes_全域_v2.0_校验报告.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 熔断判定
extracted_at: 2026-07-16T11:38:02
---

# Gate字段来源

所有gate字段（gate1_linked、gate2_grounded、gate3_traceable、gate_overall）均从Registry v1直接映射，不再手填。Gate计算逻辑：PASS为四属性全通过且三Gate全通过；PARTIAL为有任意Gate为PARTIAL且无FAIL；FAIL为任意Gate为FAIL。

## 关联概念

- [[staging_status分类]]
- [[旧T1变化]]

