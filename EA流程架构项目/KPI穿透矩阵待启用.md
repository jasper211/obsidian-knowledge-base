---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V2_项目交付.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: KPI数据治理
extracted_at: 2026-07-16T11:41:42
---

# KPI穿透矩阵待启用

DIM_KPI维度表已有32行企业KPI数据（5-24导入），但FACT_CARD的kpi_key关联规则尚未启用，需待KPI穿透矩阵完成后才能逐步填入。Phase 1/2期间允许kpi_key为NULL。这反映了数据仓库建设中维度表与事实表关联的阶段性实施策略。

## 关联概念

- [[FACT_CARD事实表]]
- [[DIM_KPI维度表]]

## 所属枢纽

- [[KPI数据治理]]
