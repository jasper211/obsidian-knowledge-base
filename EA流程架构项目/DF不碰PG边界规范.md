---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/校验报告_GV治理审核_DF执行批次_20260702.md
extracted_at: 2026-07-21T00:03:24
---

# DF不碰PG边界规范

DF（数据工厂）在治理审核中不修改PG（流程治理）的dim_process字段，即使发现PG与蓝图不一致，也仅记录为差距项，由有PG权限的角色或通过OW分发同步。

## 关联概念

- [[GV治理审核]]
- [[PG dim_process]]
