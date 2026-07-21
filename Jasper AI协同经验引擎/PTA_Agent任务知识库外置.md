---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/三大主Agent体系架构_v1.1.md
extracted_at: 2026-07-20T12:24:56
---

# PTA v1.2.0关键改造

任务知识库外置为可插拔JSON（`pta_common.py`+`pta_tasks.json`），`--project-root`下的项目自定义`pta_tasks.json`优先，兜底本项目内置默认值。已用真实假外部项目和Rw权益项目验证，是本体系第一个证明'可推向公司/其他项目使用'的案例。

## 关联概念

- [[PTA]]
- [[面向复用设计]]


---
⚠️ **待复核**：源文档「能力整改看板.md」已更新，此原子未出现在最新提炼结果中（标记时间：2026-07-21T02:00:17）
