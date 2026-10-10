---
status: pending_review
discovered_at: 2026-10-08T21:31:08.900052
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
direction: AI协同方法论
relevance_reason: 新增 serverToolUses、agentId、ceiling 等插件钩子元数据，以及托管 Agent 模式部署，直接涉及多 Agent 编排与权限治理。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文27217字符，超过50字符阈值放行
---

# 摘要

Claude Code v2.1.290 发布多项关于插件系统和多 Agent 管理的更新：在 mod 的 turn.step hook 结果中增加 serverToolUses，用于记录 API 自执行工具调用；在 tool.check 事件中添加 agentId，以区分子代理与主会话的权限检查；增加 ceiling 字段表示组织对工具的审批要求；扩展插件验证功能，列出门控钩子是否有 catch 处理；网关登录审批页增加 Deny 按钮；新增 claude attach 和 claude logs 命令；提供 /claude-api managed-agents-onboard 命令用于部署托管 Agent 模式（如 deep-researcher 模板）。这些特性增强了多 Agent 场景下的可观测性、权限控制和部署能力。

## 原始信息

- 标题/来源: v2.1.290
- 发布/变更时间: 2026-10-05T23:33:17Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
- 原文摘录（截断）:

```
## What's changed

- Added `serverToolUses` to the result of a mod's `turn.step` hook: the tool calls the API ran itself (the advisor), each with its id, name, input, start and end
- Added `agentId` to the `tool.check` event of plugin hooks, so a hook can tell a subagent's permission check from the main session's
- Added `ceiling` to the question and verdict a mod's `tool.check` hook reads, naming the approval an organization requires for a tool
- Added `ThemeKey` and `Color` types to the plugin hooks typings, so an editor lists the theme colors a mod's drawing can name
- Added to `claude plugin validate`: each hook a mod registers at a gating site is listed with whether it has a `.catch` (`gatingHooks` under `--json`)
- Added a Deny button to the Claude apps gateway's sign-in approval page: it ends the pending sign-in, so the waiting terminal stops within seconds
- Added `claude attach <name>` and `claude logs <name>`: part of a session name works in place of the id
- Added `/claude-api managed-agents-onboard <url>` to set up the Managed Agents pattern a page describes as `ant apply` files
- Added `/claude-api managed-agents-onboard <quickstart-name>` to build a Console quickstart template, such as `deep-researcher`, with the `ant` CLI
- Added a warning when a managed settings file is a link to a file outside the managed settings folder
- Added a /status and doctor warning when managed settings ignore user-configured sandbox allowRead paths or allowed domains
- Fixed request
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-10-08_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-10-08_anthropics-claude-code_release.md --reject --reason "..."`
