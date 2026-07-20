---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/_retired_flat_structure/README_v1.md
extracted_at: 2026-07-20T12:31:47
---

# PTA-DISCOVER 安全边界

PTA-DISCOVER 只产出人工可审阅的发现报告，不会自动写入 pta_tasks.json 的 steps/command 字段，避免文档内容变成命令注入面；将发现的任务变为可执行步骤永远需要人工手写 pta_tasks.json。

## 关联概念

- [[任务分类登记表]]
