---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:57:30
---

# SCD Type 2流程维度

DIM_PROCESS采用SCD Type 2（缓慢变化维），保留L4定义的历史版本。通过version、valid_from、valid_to、is_current字段管理版本，每个l4_code仅有一条is_current=TRUE的记录。

## 关联概念

- [[DIM_PROCESS]]
- [[代理键]]
