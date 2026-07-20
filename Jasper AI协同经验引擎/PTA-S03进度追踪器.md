---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/03_规划项目结构_Plan_Project_Structure/流程设计.md
extracted_at: 2026-07-20T12:31:13
---

# PTA-S03进度追踪器

PTA-S03 是 L3-PTA-03 进度监控步骤的子 Agent，负责根据执行计划和当前状态生成进度报告，包含总体状态、已完成步骤数、总步骤数、当前步骤详情和预警列表。输入为执行计划字典和当前状态字典，输出为进度报告字典，步骤超时/失败时返回异常报告。

## 关联概念

- [[L3端到端流程]]
- [[执行计划]]
