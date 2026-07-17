---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 00_治理与元模型/命名编码规范/00_治理与元模型_人机协作执行规范.md
authority_layer: 00_治理
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-RACI自动冲突检测
extracted_at: 2026-07-16T11:15:28
---

# RACI自动冲突检测

通过validate_raci.py脚本自动检测RACI冲突，规则包括：每个L3有且仅有1个A（Accountable）、每个L3至少有1个R（Responsible）、A和R不应是同一角色（除非团队<3人）、单人R超过10个L3则预警过载、协同框架中的R/A必须与RACI矩阵一致。

## 关联概念

- [[quality-gate.yaml]]
