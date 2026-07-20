---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/AI_PLATFORM_GUIDE.md
extracted_at: 2026-07-20T12:29:33
---

# PTA统一入口

PTA Agent 的统一入口是 agents/agent.py，它实现了 Think-Act-Observe 主循环，自动串联意图解析、执行编排、进度追踪和归档复盘，并将状态记录在 state.json 中。任何 AI 平台都应优先使用此入口，而非直接调用各个技能脚本。

## 关联概念

- [[PTA技能无独立CLI]]
- [[PTA跨项目使用]]
