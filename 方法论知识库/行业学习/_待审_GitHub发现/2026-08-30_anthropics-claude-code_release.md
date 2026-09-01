---
status: pending_review
discovered_at: 2026-08-30T21:31:27.159046
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
direction: AI协同方法论
relevance_reason: 新增前台子Agent工具调用实时流和模型切换钩子，直接涉及Agent协同机制与人机分工模式
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文11252字符，超过50字符阈值放行
---

# 摘要

Claude Code v2.1.251版本更新，主要变更包括：新增PreModelSwitch和PostModelSwitch钩子事件，允许在模型切换时阻止、确认或注释；SessionStart恢复钩子现在接收会话陈旧度和重新缓存成本估计；新增前台子Agent工具调用和结果的实时流式传输到远程控制客户端（后台子Agent仍仅显示状态）；新增/usage的Spend limit条和rate_limits.spend_limit状态行字段；新增/cost的每会话提示缓存行和prompt_cache对象；新增attach、logs、stop、respawn、rm命令；以及一系列安全修复，包括修复文件工具跟随符号链接问题、插件命令路径遍历、项目设置可启用详细beta追踪等。此外还修复了多个问题，如模型只产生thinking时对话卡住、Opus 5请求effort不支持等。整体上，该版本强化了子Agent监控、模型切换干预和成本/缓存追踪能力。

## 原始信息

- 标题/来源: v2.1.251
- 发布/变更时间: 2026-08-28T18:19:32Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
- 原文摘录（截断）:

```
## What's changed

- Added `PreModelSwitch` and `PostModelSwitch` hook events (block, confirm, or annotate a model switch); `SessionStart` resume hooks now receive session staleness and the estimated re-cache cost
- Added live streaming of a foreground subagent's tool calls and results to Remote Control clients (background subagents, the default, still show status only)
- Added a Spend limit bar to `/usage` and a `rate_limits.spend_limit` status line field for developers behind a Claude apps gateway with spend limits
- Added a per-session prompt-cache line to `/cost` (hit ratio, misses, tokens re-cached, warm/cold) and a matching `prompt_cache` object for status line scripts
- Added `attach`, `logs`, `stop`, `respawn`, and `rm` to `claude --help`; the `--resume` message for a running background session now names the exact `claude attach <id>` command
- Fixed file tools (Read, Write, Edit) following a symlink swapped inside the working directory after the permission check, which could read or write outside the approved location
- Fixed plugin commands declared in a marketplace entry being able to point outside the plugin directory; such paths are now rejected with a path-traversal error
- Fixed project settings being able to enable detailed beta tracing or raw API body logging, and a lower-scope beta tracing endpoint bypassing an OTLP collector pinned by managed settings or a host app
- Fixed the Workflow tool reading (and quoting in errors) a `scriptPath` outside what the ses
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-08-30_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-08-30_anthropics-claude-code_release.md --reject --reason "..."`
