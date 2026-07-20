---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/08_设计提示词_Design_Prompts/prompts/task_examples.md
extracted_at: 2026-07-20T12:32:37
---

# PTA命令行参数

PTA agent.py支持多种命令行参数：--status（只读回顾进度）、--execute（真实执行步骤但不推送）、--sync（额外同步并提交）、-m（提交信息）、--project-root（指定其他项目根目录）。默认不带--execute时为dry-run模式，只输出计划与报告。

## 关联概念

- [[PTA指令类型]]
