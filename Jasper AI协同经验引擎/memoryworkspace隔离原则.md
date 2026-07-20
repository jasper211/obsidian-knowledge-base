---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent搭建SOP_v1.2.md
extracted_at: 2026-07-20T12:24:18
---

# memory/workspace隔离原则

memory/workspace.py负责状态持久化和专属工作区隔离，与目标项目物理隔离。skill/tool不直接读写状态文件，而是接收状态dict并返回更新后的dict，由调用方（agent.py）负责加载和保存。

## 关联概念

- [[Agent组成部分]]
- [[子Agent开发]]
