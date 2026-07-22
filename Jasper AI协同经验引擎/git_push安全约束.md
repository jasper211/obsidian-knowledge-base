---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/08_设计提示词_Design_Prompts/prompts/system.md
extracted_at: 2026-07-20T12:32:48
---

# git push仅由doc_sync触发

唯一有真实副作用（git push）的动作是skills/doc_sync.py，必须用户显式要求同步才触发，且需要同时具备执行模式（非dry-run）和明确的提交信息，三者缺一不可。

## 关联概念

- [[安全边界]]
- [[dry-run默认]]


---
⚠️ **待复核**：源文档「05_Agent库/草稿/PTA/README.md」已更新，此原子未出现在最新提炼结果中（标记时间：2026-07-22T03:11:53）
