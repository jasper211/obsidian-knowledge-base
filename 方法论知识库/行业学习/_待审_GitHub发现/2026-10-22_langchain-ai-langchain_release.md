---
status: pending_review
discovered_at: 2026-10-22T20:38:25.820982
source_type: release
source_repo: langchain-ai/langchain
source_url: https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.6.13
direction: AI协同方法论
relevance_reason: 直接引入流式消费者读取`tool-call-delta`的功能，属于Agent工具调用流式处理机制的具体实现。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文236字符，超过50字符阈值放行
---

# 摘要

该版本包含核心功能更新：在langchain-core、langchain和标准测试中支持读取新的`tool-call-delta`流式事件。该功能允许流式消费者获取工具调用参数的增量切片，替换旧有的`block-delta`快照，为开发者处理流式工具调用提供了更精细的控制。同时更新了certifi依赖。该变更对构建基于LangChain的Agent系统，特别是需要实时处理工具调用流的场景，具有直接参考价值。

## 原始信息

- 标题/来源: langchain-core==1.6.13
- 发布/变更时间: 2026-10-21T20:43:48Z
- 原文链接: https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.6.13
- 原文摘录（截断）:

```
Changes since langchain-core==1.6.12

release(core): 1.6.13 (#41397)
chore(deps): bump certifi from 2025.11.12 to 2026.10.19 in /libs/core (#41373)
feat(core,langchain,standard-tests): read `tool-call-delta` in stream consumers (#41246)
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-10-22_langchain-ai-langchain_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-10-22_langchain-ai-langchain_release.md --reject --reason "..."`
