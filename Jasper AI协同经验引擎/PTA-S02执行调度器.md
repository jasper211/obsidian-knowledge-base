---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/03_规划项目结构_Plan_Project_Structure/流程设计.md
extracted_at: 2026-07-20T12:31:11
---

# PTA-S02执行调度器

PTA-S02 是 L3-PTA-02 执行编排步骤的子 Agent，负责将结构化任务包转化为执行计划（步骤清单+工具调度），包含步骤序号、动作、工具、命令、依赖和超时。输入为任务包字典，输出为执行计划字典，格式错误时返回错误信息。

## 关联概念

- [[L3端到端流程]]
- [[结构化任务包]]
