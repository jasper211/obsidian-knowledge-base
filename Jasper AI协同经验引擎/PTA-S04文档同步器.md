---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/03_规划项目结构_Plan_Project_Structure/流程设计.md
extracted_at: 2026-07-20T12:31:15
---

# PTA-S04文档同步器

PTA-S04 是 L3-PTA-04 产出同步步骤的子 Agent，负责在任务完成后同步文档：更新能力整改看板、创建/更新任务执行记录、Git add/commit/push、更新Phase完成总结。输入为任务完成信号字典，输出为同步结果字典，Git提交失败时返回错误和手动操作指南。

## 关联概念

- [[L3端到端流程]]
