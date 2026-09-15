---
type: concept_atom
concept_type: 背景说明
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/Agent与Skill体系/Agent执行机制梳理/人力资源长尾合并Agent.md
authority_layer: 01_过程成果
domain: 人力资源
confidence: MEDIUM
confidence_reason: 旧Agent机制只选HRM-03/07/09说明独立触发；现行L3-HRM蓝图包含9阶段生命周期主链，需区分触发入口与流程关系。
decision_status: UNSTATED
as_of: 2026-06-22
entity_type: Agent机制
entity_ref: L3-HRM
status: 设计参考
extracted_at: 2026-07-24T10:09:23
---

# HRM事务独立触发

旧长尾合并Agent机制从HRM中选取入职配置、薪酬发放、人员退出3条事务，强调它们各有触发时点，不应由一次入职任务机械串行触发发薪和离职。

现行 `L3-HRM` 蓝图包含9条规划L4，并把定岗招聘、入职、试用、培训、绩效、薪酬、晋升调岗和退出归档组织为人员全生命周期主链。更准确的边界是：`HRM-03/07/09` 可由入职、周期发薪和离职分别进入，但它们仍属于同一生命周期流程并共享人员档案与上下游状态；旧3条样本不能覆盖或否定其余6条规划L4。

当前未核事件监听、调度配置或运行记录。现行入口见 [[L3-HRM人员全生命周期管理]]。

## 关联概念

- [[HRM事务]]
- [[入职配置触发]]
- [[薪酬发放触发]]
- [[离职归档触发]]
- [[L3-HRM人员全生命周期管理]]
