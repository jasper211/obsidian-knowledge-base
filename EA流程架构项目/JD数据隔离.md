---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据溯源_溯源审计报告_20260430.txt
extracted_at: 2026-07-20T22:04:05
---

# JD数据隔离

T1数据底座必须严格隔离岗位JD数据：表级无dim_job_family等JD表，字段级无job/jd/ep_code/岗位/族关键字，数据级无JD_A~JD_G或'岗位'的source_doc。审计确认0条JD数据进入T1。

## 关联概念

- [[T2溯源审计通过标准]]
