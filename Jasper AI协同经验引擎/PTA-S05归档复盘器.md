---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/03_规划项目结构_Plan_Project_Structure/流程设计.md
extracted_at: 2026-07-20T12:31:16
---

# PTA-S05归档复盘器

PTA-S05 是 L3-PTA-05 归档复盘步骤的子 Agent，负责根据任务完整历史生成复盘报告，包含执行记录和教训库条目。复盘问题包括任务理解准确性、执行过程顺利性、产出符合预期性、改进点。输入为任务历史字典，输出为复盘报告字典，历史数据缺失时返回警告。

## 关联概念

- [[L3端到端流程]]
