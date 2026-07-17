---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/S2_真KPI数据建设/00_推动手册与规划/数据底座_MGA_PLATFORM数据库现状评估_v1.0.md
authority_layer: 02_草稿
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-T02弱数据基础
extracted_at: 2026-07-17T03:46:30
---

# dim_partner维度表局限

dim_partner是SCD维度表，记录当前状态而非周新增事件，无法直接用于T02周度新增统计，只能通过first_contact_date筛选本周记录。

## 关联概念

- [[dim_partner]]
- [[T02]]
