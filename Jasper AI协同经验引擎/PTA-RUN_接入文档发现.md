---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/_retired_flat_structure/README_v1.md
extracted_at: 2026-07-20T12:31:52
---

# PTA-RUN 接入文档发现

v1.5.0 起 PTA-RUN 可通过 --discover --project-root 直接调度 PTA-DISCOVER 做增量文档任务发现，结果摘要计入 .pta_state.json，--status 可查看；仍保留安全边界，不自动写入 pta_tasks.json。

## 关联概念

- [[PTA-DISCOVER 安全边界]]
- [[增量扫描机制]]
