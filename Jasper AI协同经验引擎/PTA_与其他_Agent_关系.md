---
type: concept_atom
concept_type: 背景说明
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/01_初始化项目_Initialize_Project/需求定义.md
extracted_at: 2026-07-20T12:30:32
---

# PTA 与其他 Agent 关系

用户指令先由 PTA-S01 意图解析生成任务包，然后判断任务类型：通用任务由 PTA-S02 执行，价值节点任务调用 VNW，转型咨询任务调用 AIT。执行后由 PTA-S03 同步产出，最终由 PTA-S04 归档复盘。

## 关联概念

- [[PTA-S01 意图解析]]
- [[PTA-S02 通用任务执行]]
- [[PTA-S03 产出同步]]
- [[PTA-S04 归档复盘]]
- [[VNW]]
- [[AIT]]
