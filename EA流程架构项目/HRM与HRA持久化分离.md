---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/Agent与Skill体系/Agent执行机制梳理/人力资源长尾合并Agent.md
authority_layer: 01_过程成果
domain: 人力资源
confidence: MEDIUM
confidence_reason: 旧Agent机制提出两套记录逻辑，符合HRM/HRA对象差异，但未提供实际数据模型、存储或运行证据。
decision_status: PROPOSED
as_of: 2026-06-22
entity_type: Agent机制
entity_ref: L3-HRM/L3-HRA
status: 设计参考
extracted_at: 2026-07-16T16:39:42
---

# HRM与HRA持久化分离

旧Agent机制建议：HRM事务历史按员工记录，HRA分析结果按分析周期记录，两类对象不合并为一张状态表。该原则与现行流程边界相容：HRM围绕人员生命周期，HRA围绕人效、成本、结构和诊断分析。

这仍是持久化设计，不是已落地的数据模型。源材料没有给出表结构、唯一键、版本规则、系统位置、迁移结果或读写日志；也不能因候选Agent仍合并，就推导两类状态应共表。后续实现应至少保留员工标识/生命周期版本与分析期间/口径版本的独立主键边界。

流程入口见 [[L3-HRM人员全生命周期管理]] 与 [[L3-HRA人力分析与决策支持]]。

## 所属枢纽

- [[HR Agent架构设计]]
- [[L3-HRM人员全生命周期管理]]
- [[L3-HRA人力分析与决策支持]]
