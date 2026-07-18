---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/项目规划/数据字典_流程数据库数据字典_V1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 流程维度SCD
extracted_at: 2026-07-16T12:34:51
---

# 流程维度SCD Type2

DIM_PROCESS 采用 SCD Type 2，L4 定义随里程碑迭代保留历史版本；同一 l4_code 只能有一条 is_current=TRUE 的记录，版本号递增。

## 关联概念

- [[DIM_PROCESS]]

## 所属枢纽

- [[流程维度SCD]]
