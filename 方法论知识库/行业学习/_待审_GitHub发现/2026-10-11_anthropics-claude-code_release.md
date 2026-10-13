---
status: pending_review
discovered_at: 2026-10-11T21:31:46.536224
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
direction: AI协同方法论
relevance_reason: 包含子代理权限区分、组织审批要求、多Agent编排模板等Agent验证/编排机制
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文27217字符，超过50字符阈值放行
---

# 摘要

Claude Code发布v2.1.290，主要增强了Agent治理与多Agent编排相关的可见性和控制能力。在mods的turn.step hook结果中新增加serverToolUses字段，可查看API自行调用的工具调用详情，包括id、名称、输入和起止时间，提升对Agent内部行为的审计能力。tool.check事件新增加agentId，使hook能够区分子代理与主会话的权限检查，实现更精细的权限管理。tool.check的question和verdict对象中新增ceiling字段，指明组织对某工具要求的审批级别，引入组织级审批语义。新增/claude-api managed-agents-onboard命令，支持通过ant apply文件或Console quickstart模板快速搭建Managed Agents模式，推动多Agent模式落地。其他改动包括gateway审批Deny按钮、claude attach/logs、安全警告等。这些特性围绕子代理权限区分、审批要求和多Agent部署模式，属于AI协同方法论范畴。

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

确认收录：`python3 promote_candidate.py 2026-10-11_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-10-11_anthropics-claude-code_release.md --reject --reason "..."`
