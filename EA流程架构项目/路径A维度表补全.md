---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/AI上下文/上下文_METHOD_流程架构落地工作方法论_V1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T11:50:21
---

# 路径A维度表补全

路径A利用调研数据（L4交付物调研、付款调研）填充DIM_PROCESS和DIM_ORG字段，包括角色、岗位族、SLA、执行人等。角色需标准化为position_family枚举值，SLA频率折算为小时数。操作步骤包括生成角色映射CSV、批量UPDATE维度表、与HR基线数据合并等。

## 关联概念

- [[角色岗位族映射]]
- [[SLA折算规则]]
