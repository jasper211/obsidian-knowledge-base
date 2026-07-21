---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:56:56
---

# DIM_ORG组织维度

DIM_ORG以岗位级为粒度，同一岗位族内可有多个岗位，同一岗位可有多个执行人（每人一行）。包含position_family、position_code、position_name、ep_count、headcount_target、mark_retained、executor_id、reports_to_family等字段。

## 关联概念

- [[岗位族]]
- [[FACT_CARD事实表]]
