---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 能力整改看板.md
extracted_at: 2026-07-21T02:00:17
---

# PTA Agent每日主动巡检

PTA Agent新增每日主动巡检功能：通过本地文件diff（免费、确定性）→合并一次LLM关系分析+相关性判断→建议任务以RPT-YYYYMMDD-NN格式安全写入目标项目pta_tasks.json，绝不自动执行，确认执行走正常执行路径。

## 关联概念

- [[PTA Agent]]
