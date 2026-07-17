---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Carrie回执_AG07底座_ready_20260524.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-24
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-真KPI目标待定
extracted_at: 2026-07-16T12:14:24
---

# DIM_KPI表字段补齐

DIM_KPI表当前缺少所属L1、关联L3、分子分母字段、责任Agent四个字段。前三项需从KPI-L3映射标准文档提取后通过ALTER TABLE和UPDATE补齐，责任Agent列先建空，待AG07上线后写入。

## 关联概念

- [[KPI-L3映射标准文档]]
- [[AG07上线]]
