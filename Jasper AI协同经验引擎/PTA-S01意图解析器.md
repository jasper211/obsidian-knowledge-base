---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/03_规划项目结构_Plan_Project_Structure/流程设计.md
extracted_at: 2026-07-20T12:31:09
---

# PTA-S01意图解析器

PTA-S01 是 L3-PTA-01 任务解析步骤的子 Agent，负责将用户自然语言指令解析为结构化任务包（JSON），包含任务ID、类型（顺序/并行/条件）、优先级、任务项列表、约束和上下文。输入为字符串，输出为字典，指令模糊时返回澄清问题列表。

## 关联概念

- [[L3端到端流程]]
- [[结构化任务包]]
