---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/KPI穿透/kpi_cross_check.txt
extracted_at: 2026-07-20T21:50:20
---

# KPI ID跨文档核对方法

核对企业KPI目录与dim_kpi表时，需注意ID格式差异：企业目录使用两位数字前缀（如'01'），dim_kpi使用无前缀数字（如'1'）。共同ID为去掉前缀后相同的那些，如'12'与'12'匹配。

## 关联概念

- [[KPI ID前缀差异]]
