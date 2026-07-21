---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/校验报告_数据库层_TASK-EEP-004B.md
extracted_at: 2026-07-20T23:01:35
---

# dim_l3 vs_code空值

dim_l3表中vs_code字段有17条空值（占比20.7%），集中在L1-01（战略类，9/9全空）、L1-03（佣金类，4条）、L1-05（权益类，4条）。已知问题中L3-SDSA确认为空值，其余3条（SRA/SPD/CFRM）已有映射。需评估战略类L3是否设计上不归属任何价值流，或映射尚未完成。

## 关联概念

- [[dim_l3]]
- [[vs_code]]
- [[L1-01]]
