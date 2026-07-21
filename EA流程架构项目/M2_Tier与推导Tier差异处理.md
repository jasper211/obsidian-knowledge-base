---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/映射分析/交付物Agent_核心交付物映射逻辑分析与标准.md
extracted_at: 2026-07-20T21:39:01
---

# M2 Tier与推导Tier差异处理

当M2 Tier（Mark原始评分）与推导Tier（基于六维度自动推导）不一致时，处理规则：若M2=Auto且推导=Aug，以M2为准；若M2=Hybrid且推导=Aug，保留Hybrid（保守原则）；若M2=Human且推导=Aug/Auto，以M2为准（存在隐性合规或情感因素）。

## 关联概念

- [[总分Tier映射阈值]]
- [[六维度评分体系]]
