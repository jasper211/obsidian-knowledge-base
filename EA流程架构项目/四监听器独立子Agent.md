---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/Agent规划与搭建/L3-COM_佣金全链路管理Agent/01_规划分析.md
authority_layer: 02_草稿
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: L3流程
entity_ref: L3-COM
extracted_at: 2026-07-16T20:28:11
---

# 四监听器独立子Agent

COM-05追溯、COM-07争议、COM-09异常、COM-17合规四个监听器建议做成独立子Agent，而非主Agent内部的interrupt handler。因为它们的触发频率、验证标准、持久化需求与主链不同，且符合生成器/评估器分离原则。主Agent负责收到中断信号后暂停主链、等待子Agent处理完毕、决定继续或回退。

## 关联概念

- [[中断监听器]]
- [[三级串联检查链]]

## 所属枢纽

- [[L3-COM]]
