---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:56:40
---

# FACT_CARD事实表

FACT_CARD是流程运行事实表，每行对应一次L4活动的完整执行实例。包含主键fact_id、维度代理键外键、自然键冗余字段、执行度量（状态、时长、SLA、返工次数等）、质量度量、Agent介入度量、价值度量及审计字段。

## 关联概念

- [[FACT_CARD星型模型]]
- [[DIM_PROCESS]]
- [[DIM_TIME]]
