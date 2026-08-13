---
status: pending_review
discovered_at: 2026-08-11T21:31:06.453297
source_type: release
source_repo: langchain-ai/langchain
source_url: https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.3.15
direction: AI协同方法论
relevance_reason: 变更包含AgentMiddleware的trace_policy暴露、ToolCallLimitMiddleware的tool_calls清理、HITL审批门修复等，直接涉及Agent协同和行为控制机制
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文1979字符，超过50字符阈值放行
---

# 摘要

此版本引入多项与Agent协同相关功能：AgentMiddleware新增trace_policy参数用于追踪策略配置；ToolCallLimitMiddleware修复了结束行为中可能残留的tool_calls；修复了HITL（人机交互）审批门静默失败问题，确保审批机制可靠；并为wrap_tool_call添加了state_schema参数，以及过滤内部中间件模型调用等。这些增强了Agent开发的控制力和可靠性，体现了业界在Agent框架上的实践进展。

## 原始信息

- 标题/来源: langchain==1.3.15
- 发布/变更时间: 2026-08-11T19:11:09Z
- 原文链接: https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.3.15
- 原文摘录（截断）:

```
Changes since langchain==1.3.14

release(langchain): 1.3.15 (#39595)
feat(langchain): expose `trace_policy` on `AgentMiddleware` (#38910)
chore(langchain): fix type errors in tests (#39589)
chore: bump h2 from 4.3.0 to 4.4.1 in /libs/langchain_v1 (#39324)
fix(langchain): preserve history on `SummarizationMiddleware` summary failure (#39268)
fix(langchain): handle import error in `LLMToolEmulator` by `model` (#39290)
refactor(langchain): update doc strings (#39305)
feat(langchain): add `state_schema` param to `wrap_tool_call` (#39292)
fix(langchain): re-export `PIIMatch` from `middleware` package (#39291)
fix(langchain): restrict narrowed `ToolStrategy` in bound tools (#39259)
feat(langchain): filter internal middleware model calls from `messages` projection (#39252)
chore: bump aiohttp from 3.14.1 to 3.14.3 in /libs/langchain_v1 (#39242)
chore: bump cryptography from 48.0.1 to 50.0.0 in /libs/langchain_v1 (#39240)
test(langchain): regression test for shell tool + checkpointer msgpack error (#39267)
fix(langchain): handle malformed structured-output responses (#39245)
fix(langchain): prevent orphaned `tool_calls` in `ToolCallLimitMiddleware` end behavior (#39258)
fix(langchain): add aliases for bedrock mantle chat models (#39260)
feat(langchain): add LangSmith provider to `init_chat_model` (#39224)
fix(langchain): clear stale `structured_response` between checkpointed turns (#39248)
fix(langchain): stop HITL approval gates from silently failing open (#39247)
chore: bump the mi
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-08-11_langchain-ai-langchain_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-08-11_langchain-ai-langchain_release.md --reject --reason "..."`
