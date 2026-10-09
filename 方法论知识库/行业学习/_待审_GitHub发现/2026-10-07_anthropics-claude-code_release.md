---
status: pending_review
discovered_at: 2026-10-07T21:31:36.179577
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
direction: AI协同方法论
relevance_reason: 新增agentType字段用于区分自定义子代理类型，直接涉及多Agent协同中的子代理识别与管理。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文8403字符，超过50字符阈值放行
---

# 摘要

Claude Code v2.1.293发布，主要变更包括：引入Claude Haiku 5.5模型作为新的默认Haiku模型，支持1M上下文及分层定价；在subagentStatusLine负载中新增agentType字段，使脚本能够区分自定义子代理类型，提升了对多代理系统中不同角色代理的监控与编排能力；为mod开发者新增isDeferred工具注册选项，允许工具schema从对话开始就包含在提示中，而不是隐藏在工具搜索后面，这优化了工具发现与提示构建策略。此外，修复了多个与上下文压缩、MCP连接内存泄漏、后台消息丢失、模型努力级别边界、工具禁用提示、技能同步以及CLI命令会话管理等相关的缺陷，这些修复增强了代理行为的稳定性和一致性。整体而言，该版本包含若干针对多代理协同与工具交互的功能增强，以及大量稳定性修复。

## 原始信息

- 标题/来源: v2.1.293
- 发布/变更时间: 2026-10-07T18:10:20Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.293
- 原文摘录（截断）:

```
## What's changed

- Added Claude Haiku 5.5 (`claude-haiku-5-5`), now the default Haiku model on the Anthropic API — 1M context, $0.10/$0.50 per Mtok ($0.50/$2.50 for prompts over 100K)
- Added `agentType` to the `subagentStatusLine` payload, so scripts can tell custom subagent types apart
- Added `isDeferred` to `$.tool.register` for mods: `false` lists the tool's schema in the prompt from the start instead of behind tool search
- Fixed Claude sometimes treating its own last actions before a context compaction as done after it, and retracting or redoing finished work
- Fixed a memory leak where an HTTP MCP connection kept every request it had sent until it closed
- Fixed a message sent while Claude was working being lost when `←` moved the session to the background; if a queued message can't move, `←` now stays put and says so
- Fixed `/model` effort ←/→ wrapping past the highest or lowest level, which could accidentally save Low as a model's default effort
- Fixed `/tui` disconnecting Claude in Chrome in a session started with `--chrome`, and ignoring `--no-chrome`
- Fixed Claude being told to continue or message subagents with `SendMessage` in sessions, including resumed ones, where a host, a permission rule or a `--tools` list removed that tool
- Fixed subagents and `--agent` sessions being told a built-in tool was disabled for the whole session when only their own tool list left it out
- Fixed a claude.ai-synced skill's edited description sometimes not reaching the model
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-10-07_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-10-07_anthropics-claude-code_release.md --reject --reason "..."`
