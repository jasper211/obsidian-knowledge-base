---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:56:45
---

# DIM_PROCESS流程维度

DIM_PROCESS覆盖L1至L5完整流程层级，包含Agent化6维评分（输入结构化、规则清晰度、输出可验证、API可达性、降级机制、合规性），采用SCD Type 2保留L4定义的历史版本，通过version、valid_from、valid_to、is_current字段管理版本。

## 关联概念

- [[SCD Type 2]]
- [[Agent化6维评分]]
- [[FACT_CARD事实表]]
