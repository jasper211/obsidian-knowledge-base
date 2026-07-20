---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/三大主Agent体系架构_v1.2.md
extracted_at: 2026-07-20T12:22:31
---

# PTA背景记忆层缺口

PTA五个扩展能力（rule-scan、discover、daily-scan、intel、dashboard）都缺少“先理解项目背景/文档逻辑关系再做任务抽取”的能力，导致--rule-scan在真实叙述性文档上噪音大（290条任务中很多是历史记录误抽取）。根因不是规则不够严，而是缺乏持续积累的语义记忆。正确填补方式是接入Obsidian巡检Agent的知识图谱能力，而非PTA自己重新实现。

## 关联概念

- [[PTA]]
- [[Obsidian巡检Agent]]
- [[知识图谱]]
