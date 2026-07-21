---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据整合_修复包_v3.md
extracted_at: 2026-07-20T22:50:48
---

# FIX-05标记非VS级L3

根据L3与价值流全量分析汇总表.csv的vs_suggested字段，将标记为'非VS级'的L3的is_vs_level设为0，vs_code和vs_stage_code设为NULL。对于confidence为'中'的L3（L3-CFRM、L3-SRA、L3-SPD），将confirmation_status标记为needs_review。

## 关联概念

- [[非VS级L3]]
- [[dim_l3]]
