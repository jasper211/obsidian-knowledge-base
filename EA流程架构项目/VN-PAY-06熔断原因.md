---
type: concept_atom
concept_type: 背景说明
project: EA流程架构项目
source: 现行状态母对象=流程蓝图_L3-COM_佣金全链路管理_V1.0.md；现行事实对象=D2_价值节点_L3映射表_V2.19.csv、最终校验_D1_D2_20260612.log、kpi_registry_v2.4.csv；历史吸收对象=PAY域_价值节点信号提取基线_v1.0.md
authority_layer: 03_现行校准
domain: PAY
confidence: HIGH
confidence_reason: D2、校验日志与 KPI 注册表已共同锁定该节点的现行挂接与问题形态
decision_status: UNSTATED
as_of: 2026-08-14
entity_type: 判因
entity_ref: VN-PAY-06节点
status: 生效
extracted_at: 2026-07-24T10:39:21
---

# VN-PAY-06熔断原因

本页用于说明 `VN-PAY-06` 当前为何仍应按现行口径理解为高风险支付节点，而不是继续沿用旧版“协议参数未中心化”的单点描述。

`VN-PAY-06` 的现行对象是 `理财师综合应派计算清单`。从现行事实看，它同时挂接 `L3-COM` 与 `L3-STLM`，说明这个节点不是单一流程里的局部表格，而是跨佣金计算与激励结算口径的汇总出口。它的问题核心在于四类协议参数、挂数逻辑与追溯链路没有形成统一底座，导致 `理财师NPS` 与 `综合应派一次通过率` 虽然已被注册为节点 KPI，但实际无法稳定复盘“为什么这样算、按哪套规则算、改过哪些口径”。

因此，这里的熔断判因应理解为“清单可以被做出来，但不能被稳定证明正确”。一旦参数口径分散、归因链不闭合、跨 L3 挂接关系不清，节点就会持续停留在高风险状态。

## 关联概念

- [[VN-PAY-06节点]]
- [[L3-COM]]
- [[L3-STLM]]

## 所属枢纽

- [[VN-PAY-06节点]]
