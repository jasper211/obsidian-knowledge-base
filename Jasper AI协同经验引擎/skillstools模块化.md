---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent搭建SOP_v1.2.md
extracted_at: 2026-07-20T12:23:54
---

# skills/tools模块化

PTA实操后，原'子Agent'编号命名法（S01/S02）被skills/tools模块取代。skills目录放描述性命名的业务模块（如skills/daily_sensing.py），tools目录放可被多个skill复用的纯技术层（如文件diff、LLM调用）。不再用编号区分先后，职责边界更清晰。

## 关联概念

- [[Agent组成部分]]
- [[子Agent命名法]]
