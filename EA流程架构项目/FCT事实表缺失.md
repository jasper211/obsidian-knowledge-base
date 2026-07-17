---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Carrie回执_W8C_spotcheck_20260524.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-24
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:11:46
---

# FCT事实表缺失

PG数据库中所有schema均不存在FCT_开头的事实表（已全面确认非schema问题），导致AG07实际计算KPI时无法出数。DIM_KPI补字段本身已完成，但依赖FCT_表的ETL建表计划待主thread确认。

## 关联概念

- [[DIM_KPI补字段完成]]
