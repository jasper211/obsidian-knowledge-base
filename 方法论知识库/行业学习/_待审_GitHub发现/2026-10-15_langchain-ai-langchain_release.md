---
status: pending_review
discovered_at: 2026-10-15T21:32:10.592998
source_type: release
source_repo: langchain-ai/langchain
source_url: https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.6
direction: AI协同方法论
relevance_reason: 为 Human-in-the-loop 中间件增加按调用级别的中断选项，直接扩展了人机协同的粒度控制，属于人机分工模式的具体实现。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文142字符，超过50字符阈值放行
---

# 摘要

LangChain 1.4.6 发布了一项重要功能：为 HITL（Human-in-the-loop）中间件添加可选的按调用中断（opt-in per-call interrupts）。此前 HITL 中间件可能只能在全局级别配置是否在每次模型调用前请求人工审批，缺乏细粒度控制。本次更新允许开发者根据每次调用的上下文、输入或结果，动态决定是否触发人工中断。这使得人机协同更加灵活：开发者可以在关键步骤强制人工审核，而在其他步骤自动化运行，从而在安全性和效率之间找到更优平衡。该功能直接涉及人机分工模式，为构建需要人工监督的 Agent 系统提供了实用的机制，值得人工待审区进一步评估。

## 原始信息

- 标题/来源: langchain==1.4.6
- 发布/变更时间: 2026-10-14T17:28:06Z
- 原文链接: https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.6
- 原文摘录（截断）:

```
Changes since langchain==1.4.5

release(langchain): 1.4.6 (#41247)
feat(langchain): add opt-in per-call interrupts to HITL middleware (#41062)
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-10-15_langchain-ai-langchain_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-10-15_langchain-ai-langchain_release.md --reject --reason "..."`
