---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:57:35
---

# SLA违规计算规则

FACT_CARD中sla_breach_flag为生成列，当duration_hours > sla_hours_actual时置为TRUE，否则FALSE。若duration_hours或sla_hours_actual为NULL则返回NULL。sla_hours_actual在写入时从DIM_PROCESS复制，防止历史失真。

## 关联概念

- [[FACT_CARD事实表]]
- [[SLA标准]]
