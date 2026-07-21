---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/校验报告_KPI全维度审计_v1.md
extracted_at: 2026-07-20T22:42:42
---

# KPI SSOT数据模型建议

建议建立dim_kpi主表（含计算公式、方向、单位、目标值等完整属性）、bridge_kpi_l3（KPI→L3贡献，权重组内归一=100）、bridge_job_kpi（岗位KPI→企业KPI落责），入T1活跃库并晋升03层。

## 关联概念

- [[KPI SSOT缺失]]
- [[KPI计算口径缺失]]
