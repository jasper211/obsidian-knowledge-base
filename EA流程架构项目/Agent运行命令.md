---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 01_原始材料-外部导入/M-04_项目工作区/04_项目工作区_流程团队成果与操作指引.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-Agent资产沉淀
extracted_at: 2026-07-16T13:19:33
---

# Agent运行命令

在mga-data-platform目录下，查看所有Agent状态用python -m agents.registry；跑佣金全链路用python -m agents.commission_agents；跑业绩全链路用python -m agents.performance_agents；跑产品校验用python -m agents.product_agents；可加--step参数只跑某一步。Agent失败时自动发企业微信告警。

## 关联概念

- [[数据中台组件]]
