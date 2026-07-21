---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据整合_修复包_v3.md
extracted_at: 2026-07-20T22:50:45
---

# FIX-04更正l1_name

dim_l3表中的l1_name字段必须使用L1权威名称，禁止使用旧名称（如保险业务赋能、代理人事业发展等）。通过UPDATE语句按l1_code逐一更正，并验证无旧名称残留。

## 关联概念

- [[L1权威名称]]
- [[dim_l3]]
