---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/校验报告_KPI全维度审计_v1.md
extracted_at: 2026-07-20T22:41:43
---

# KPI权重逻辑破裂

企业KPI权重总和应为100，但实测仅11/32成立，21/32超过100（最高达245）。根因是补充映射并入主表后未重新归一化。岗位KPI权重同样多数不等于100。

## 关联概念

- [[KPI SSOT缺失]]
