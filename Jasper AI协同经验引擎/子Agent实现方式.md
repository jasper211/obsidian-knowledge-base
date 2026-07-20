---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/03_规划项目结构_Plan_Project_Structure/流程设计.md
extracted_at: 2026-07-20T12:31:21
---

# 子Agent实现方式

原始流程设计中子 Agent 为独立进程/脚本，但实际实现中改为 skills/ 包里的 Python 类（如 intent_parsing.py），彼此靠同进程内函数调用衔接，不再有落地临时 JSON 文件再互相读取的步骤。

## 关联概念

- [[PTA-S01意图解析器]]
- [[PTA-S02执行调度器]]
- [[PTA-S03进度追踪器]]
- [[PTA-S04文档同步器]]
- [[PTA-S05归档复盘器]]
