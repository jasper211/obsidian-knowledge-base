---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 01_原始材料-外部导入/M-77_跨部门输入/数据模型设计v2.2.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-权益兑现负责人同步
extracted_at: 2026-07-16T12:37:07
---

# 权益激励档位与Hold机制

权益激励按合同档位结算，匹配维度包括业务细分、市场分层、KEY ACCOUNT、机构、合作伙伴。触发档位需同时满足折标保费门槛和累积使用服务价值阈值。当服务价值不足时，激励金被hold，状态变为'待结算'或'部分结算'。每半月从权益部门更新服务价值后自动重算可派发金额。

## 关联概念

- [[权益激励]]
- [[Hold状态]]
- [[服务价值]]
