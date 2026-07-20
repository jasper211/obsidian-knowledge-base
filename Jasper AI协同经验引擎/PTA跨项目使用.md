---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/AI_PLATFORM_GUIDE.md
extracted_at: 2026-07-20T12:29:36
---

# PTA跨项目使用

PTA 从 v1.2.0 起不再硬编码只识别本项目的任务。要在其他项目上使用 PTA，只需在目标项目根目录放置一份 pta_tasks.json 文件定义任务，然后通过 agent.py 的 --project-root 参数指定项目路径即可。未定义的任务 ID 会优雅降级为占位步骤，不会报错。

## 关联概念

- [[PTA统一入口]]
