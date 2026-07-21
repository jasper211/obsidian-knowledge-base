---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:57:01
---

# DIM_TIME时间维度

DIM_TIME由脚本生成，覆盖2024-01-01至2027-12-31，主键为YYYYMMDD格式整数。包含full_date、year、quarter、month、week（ISO周数）、day_of_week（1=周一）、day_of_year、is_weekday等字段，不处理节假日。

## 关联概念

- [[FACT_CARD事实表]]
- [[时间维度]]
