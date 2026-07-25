---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/05_SOP/SOP_VN-PAY-01_市场佣金制作产出包_v0.2.md
authority_layer: 02_定稿
domain: PAY
confidence: HIGH
confidence_reason: 原文明确区分误差阈值和处置流程，无歧义
decision_status: UNSTATED
as_of: 未知
entity_type: SOP
entity_ref: Fact表校验
status: 生效
extracted_at: 2026-07-24T10:25:53
---

# Fact表校验差额处理

用Fact_Commission_Rate校验时，若计算Total与实际Total差额≤0.0001且符合四舍五入规则，可备注说明；否则必须返回步骤2/3逐行排查直至归零。

## 关联概念

- [[Fact_Commission_Rate]]
- [[四舍五入误差]]
- [[交叉校验]]

## 所属枢纽

- [[Fact表校验]]
