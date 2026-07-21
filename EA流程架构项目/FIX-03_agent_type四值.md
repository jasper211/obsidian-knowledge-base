---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据整合_修复包_v3.md
extracted_at: 2026-07-20T22:50:42
---

# FIX-03 agent_type四值

agent_type字段必须为4个枚举值之一：Auto（规则引擎全自动）、Aug（Agent主导+人工审批）、Hybrid（人工主导+Agent辅助）、Human（纯人工）。来源为L4_核心交付物全量表_v5.csv的M2_Tier字段。修复时从m2_tier还原，并验证分布与源文件一致。

## 关联概念

- [[dim_agent_capability]]
