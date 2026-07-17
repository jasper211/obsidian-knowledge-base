---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/项目规划/模板_流程数据库FACT_Card_V1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-FACT_CARD字段数据来源
extracted_at: 2026-07-16T11:55:25
---

# FACT_CARD事实表

FACT_CARD是流程数据库星型模型的核心事实表，每一行代表一次流程活动的运行记录（L3或L4级别），包含流程、价值流、组织、时间、Agent、战略、KPI、交付物等维度外键，以及执行状态、耗时、SLA、返工次数、交接次数、错误标志、升级标志、Agent介入标志、APE贡献、人效得分等度量字段。

## 关联概念

- [[流程星型模型]]
- [[DIM_PROCESS]]
- [[DIM_VS]]
- [[DIM_ORG]]
- [[DIM_KPI]]
- [[DIM_AGENT]]
- [[DIM_TIME]]
- [[DIM_DELIVERABLE]]
- [[DIM_STRATEGY]]
