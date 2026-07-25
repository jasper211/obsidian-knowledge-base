---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/Agent与Skill体系/Agent执行机制梳理/人力资源长尾合并Agent.md
authority_layer: 02_定稿
domain: （无）
confidence: HIGH
confidence_reason: 原文以明确建议性语气表述，但确定性高
decision_status: UNSTATED
as_of: 未知
entity_type: Agent机制
entity_ref: HR Agent架构设计
status: 生效
extracted_at: 2026-07-24T10:09:19
---

# HR持久化双逻辑

HR Agent的状态记录需要两套逻辑：按员工记录事务类历史(入职、薪酬、离职)，按周期记录分析类盘点结果，不建议合并为一张表。

## 关联概念

- [[员工事务历史]]
- [[周期分析盘点]]
- [[状态持久化]]

## 所属枢纽

- [[HR Agent架构设计]]
