---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/Agent与Skill体系/Agent执行机制梳理/人力资源长尾合并Agent.md
authority_layer: 03_历史吸收
domain: 人力资源
confidence: MEDIUM
confidence_reason: 与“HRM与HRA持久化分离”同源同义，保留为历史兼容入口；设计尚无数据模型或运行证据。
decision_status: PROPOSED
as_of: 2026-06-22
entity_type: Agent机制
entity_ref: HRM与HRA持久化分离
status: 历史吸收
extracted_at: 2026-07-24T10:09:19
---

# HR持久化双逻辑

本页与 [[HRM与HRA持久化分离]] 同源同义，保留旧标题用于兼容引用，不再作为独立现行规则。

可复用原则是HRM事务历史按员工、HRA分析结果按周期分开记录；但这仍是设计建议，未见表结构、唯一键、系统位置或读写日志。现行解释、实现边界及HRM/HRA流程入口统一从主页面查询。

## 关联概念

- [[员工事务历史]]
- [[周期分析盘点]]
- [[状态持久化]]
- [[HRM与HRA持久化分离]]

## 所属枢纽

- [[HRM与HRA持久化分离]]
