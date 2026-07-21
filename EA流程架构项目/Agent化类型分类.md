---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/TMPL_流程数据库FACT_Card_V1_架构知识库.md
extracted_at: 2026-07-21T00:58:17
---

# Agent化类型分类

Agent化类型分为四类：Auto（全自动）、Aug（增强辅助）、Hybrid（人机混合）、Human（人工）。DIM_AGENT中agent_type仅包含Auto/Aug/Hybrid（不含Human），而FACT_CARD和DIM_PROCESS中agentifiability包含全部四类。

## 关联概念

- [[DIM_AGENT]]
- [[DIM_PROCESS]]
