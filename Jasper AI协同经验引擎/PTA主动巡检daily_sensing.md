---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/README.md
extracted_at: 2026-07-20T12:28:53
---

# 主动感知闭环

v2.3.0新增的--daily-scan能力使PTA从纯粹的被动执行引擎升级为主动感知+人工确认+执行的闭环。每日巡检检测目标项目文件变化，分析逻辑关系，生成建议任务写入pta_tasks.json，但不会自动执行，需用户确认后走原有被动执行路径。

## 关联概念

- [[每日巡检]]
- [[被动执行]]


---
⚠️ **待复核**：源文档「05_Agent库/草稿/三大主Agent体系架构_v1.2.md」已被删除（标记时间：2026-07-21T02:00:44）
