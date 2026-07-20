---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/08_设计提示词_Design_Prompts/prompts/system.md
extracted_at: 2026-07-20T12:32:51
---

# PTA状态隔离写入工作区

PTA自己的状态和运行产物（state.json、每次运行的task/plan/report快照）写入目标项目专属工作区（memory/workspace.py），不写入目标项目目录，也不写入PTA源码所在的共享仓库。

## 关联概念

- [[安全边界]]
- [[归档复盘写入目标项目]]
