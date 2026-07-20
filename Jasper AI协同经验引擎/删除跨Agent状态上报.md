---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/11_监控与优化_Monitor_and_Optimize/README.md
extracted_at: 2026-07-20T12:32:17
---

# 删除跨Agent状态上报

原 PTA-INTEL 内嵌的 agent_status 跨 Agent 状态上报功能（将分析结果写入第三方路径）违反 workspace 隔离原则，迁移时直接删除。

## 关联概念

- [[workspace隔离原则]]
- [[跨Agent通信]]
