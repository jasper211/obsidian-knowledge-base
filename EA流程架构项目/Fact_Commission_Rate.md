---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/Agent规划与搭建/L3-COM_佣金全链路管理Agent/04_佣金数据表全景.md
authority_layer: 02_草稿
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: L3流程
entity_ref: L3-COM
extracted_at: 2026-07-16T20:29:36
---

# Fact_Commission_Rate

佣金费率事实表，物理名Fact_Commission_Rate，属于L4 COM-01/02，存储每季度全量更新的佣金费率数据，是下游结算的源头。治理状态为准三权合一，但实地验证发现应收侧数据不全（Q1/Q2缺口），仅对数据完整的保司子集可用。

## 关联概念

- [[数据表就绪度评估]]
- [[CONFIG_PRODUCT_COMMISSION_FORMULA]]

## 所属枢纽

- [[L3-COM]]
