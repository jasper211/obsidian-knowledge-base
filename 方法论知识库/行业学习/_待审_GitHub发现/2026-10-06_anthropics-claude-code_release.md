---
status: pending_review
discovered_at: 2026-10-06T21:31:04.638535
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
direction: AI协同方法论
relevance_reason: 新增 managed-agents-onboard 命令以搭建 Managed Agents 模式，以及 serverToolUses/agentId/ceiling 等钩子，涉及多Agent编排与组织级权限协同
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文27217字符，超过50字符阈值放行
---

# 摘要

本次Claude Code v2.1.290发布包含多项与AI协同方法论相关的能力。新增`/claude-api managed-agents-onboard`命令，可以直接基于URL或Console quickstart模板（如deep-researcher）搭建Managed Agents模式，简化多Agent应用的部署。在mod钩子层面，`turn.step`结果新增`serverToolUses`，可获取API自行运行的工具调用（advisor）的id、name、input、起止时间，提升对Agent执行过程的观测性；`tool.check`事件新增`agentId`，使钩子能区分子Agent与主会话的权限检查，并新增`ceiling`字段指明组织要求的审批级别，强化了多Agent场景下的权限治理。此外还增加了`claude attach/logs`等会话管理命令及若干修复。

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

确认收录：`python3 promote_candidate.py 2026-10-06_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-10-06_anthropics-claude-code_release.md --reject --reason "..."`
