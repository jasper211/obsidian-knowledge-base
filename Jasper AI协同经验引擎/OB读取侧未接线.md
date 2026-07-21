---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/三大主Agent体系架构_v1.3.md
extracted_at: 2026-07-20T23:14:52
---

# OB读取侧未接线

OB的检索服务端（get_context()）虽已就绪，但PTA/VNW/AIT三个业务Agent里没有一行代码真正发起过这个调用。PTA的'背景记忆层缺口'至今未填补，不是因为OB没建好，而是因为业务Agent自己没接线。

## 关联概念

- [[Obsidian巡检Agent]]
- [[OB写入侧空白]]
