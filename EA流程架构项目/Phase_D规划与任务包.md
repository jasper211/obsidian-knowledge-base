---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/AI上下文/Mark任务协同规则_v0_1_20260527.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-27
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T11:53:25
---

# Phase D规划与任务包

Phase D是六阶段中的第四阶段，触发条件为Phase C评估结论为✅（可直接执行）或🟡（部分可执行）。动作主体为Claude（规划+出包）和Jasper（确认+授权）。产出物包括规划图（需Jasper确认）和任务包（F2格式，含R8检查声明）。执行终端由Jasper指定：文件执行类→Qoder，代码执行类→OpenCode，内容扫描类→Kimi。

## 关联概念

- [[六阶段协同闭环]]
- [[F2规范激活时机]]
- [[跨文件夹路径规范]]
