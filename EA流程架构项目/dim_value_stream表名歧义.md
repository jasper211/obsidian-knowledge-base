---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/校验报告_数据库层_TASK-EEP-004B.md
extracted_at: 2026-07-20T23:01:49
---

# dim_value_stream表名歧义

dim_value_stream表实际存储的是价值流活动全量明细（359条活动记录），每条vs_code出现多次（如VS-2出现223次），不是仅含5行的VS维度码表。使用此表做跨表关联时需注意join条件应确认使用vs_code还是行级明细字段。

## 关联概念

- [[dim_value_stream]]
- [[vs_code]]
