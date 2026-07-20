---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/_retired_flat_structure/README_v1.md
extracted_at: 2026-07-20T12:31:45
---

# PTA-RUN 安全设计

PTA-RUN 通过 --no-sync 将 git push 从自动执行计划中摘出，改为独立显式确认阶段；--sync 必须同时搭配 --execute 和 -m 才会触发，避免无人值守下未经确认推送。

## 关联概念

- [[PTA-S04 git add限制]]
