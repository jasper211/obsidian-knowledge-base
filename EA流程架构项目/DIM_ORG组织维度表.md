---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 组织维度
extracted_at: 2026-07-16T11:45:18
---

# DIM_ORG组织维度表

DIM_ORG是组织维度表，粒度为岗位级（同一岗位族内可有多个岗位，同一岗位可有多个执行人）。包含岗位族编码、岗位编码、编制人数、执行人信息等字段。主键为org_key（自增序列）。

## 关联概念

- [[FACT_CARD事实表]]
- [[岗位族编码]]

## 所属枢纽

- [[组织维度]]
