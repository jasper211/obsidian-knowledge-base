---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent搭建SOP_v1.1.md
extracted_at: 2026-07-20T12:23:03
---

# config.json结构

config.json是Agent的大脑，包含agent_id、name、version、status、description、l3_flow（每个L3的code、name、sub_agents、input、output）、skills_used、dependencies（upstream/downstream）、archive_gate（mark_confirmed、deliverables）。

## 关联概念

- [[Agent组成部分]]
