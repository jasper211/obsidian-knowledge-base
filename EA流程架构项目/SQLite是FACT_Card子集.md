---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/项目规划/规划分析_Teresa文档评估_与项目融合分析.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T11:58:30
---

# SQLite是FACT_Card子集

当前SQLite底座是Teresa设计的PostgreSQL FACT_Card的子集，覆盖了维度层（DIM表）的大部分，但完全没有度量层（运行数据）。这是设计上合理的——SQLite做静态知识底座，FACT_Card做动态运行记录。

## 关联概念

- [[FACT_Card数据模型]]
- [[SQLite底座]]
