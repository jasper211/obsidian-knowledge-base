---
type: project_note
project: 流程架构
layer: "08_任务与跟进"
layer_tag: 任务
subdir: "任务状态"
tags: [任务]
---

## 🧭 导航
⬆️ [[08_任务与跟进]] · ⬆️ [[任务状态]] · 🏠 [[流程架构项目MOC]]

---

[partial ready 75%] DIM_KPI 表已建，32/32 行 KPI 数据 ready，
PG 凭据已就绪（43.98.163.46/DIM_ORG）。

差距：缺 4 个字段——所属L1、关联L3、分子分母字段、责任Agent。
前三项需从 KPI-L3 映射标准文档提取后 ALTER TABLE + UPDATE，
责任Agent 列建空（AG07 上线后写入）。

ETA：5-28 前完成字段补齐，5-29 Day 0 可正常起跑。

