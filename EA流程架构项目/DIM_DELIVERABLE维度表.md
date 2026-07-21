---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:57:21
---

# DIM_DELIVERABLE交付物维度

DIM_DELIVERABLE遵循L4唯一物理交付物原则，每个L4对应一个物理交付物，一行记录。包含deliverable_name、deliverable_type（报告/合同/凭证等）、deliverable_category（文档/签约文件/数字产物/决策产物）、l4_code（1:1关系）、l3_code、vs_code、agentifiability。

## 关联概念

- [[L4唯一物理交付物原则]]
- [[FACT_CARD事实表]]
