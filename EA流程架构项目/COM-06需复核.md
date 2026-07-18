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
extracted_at: 2026-07-16T20:27:49
---

# COM-06税务处理按Aug设计

COM-06税务处理的Tier判定存在争议（旧版评为Auto但人介入点写的是常规签字）。处理策略：在Skill设计时按Aug（保留人工签字）设计，因为资金/税务类Agent的安全原则是宁可多留一个关卡。Agent框架支持将签字环节从Aug降级为Auto，比反过来改容易。

## 关联概念

- [[COM-06税务处理]]
- [[Tier判定争议]]

## 所属枢纽

- [[L3-COM]]
