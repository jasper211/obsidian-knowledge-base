---
status: pending_review
discovered_at: 2026-10-13T20:59:06.558366
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
direction: AI协同方法论
relevance_reason: 命中：包含serverToolUses、agentId区分主子代理权限检查、managed-agents-onboard模式设置等，直接涉及多Agent编排与权限协同。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文27217字符，超过50字符阈值放行
---

# 摘要

本次更新包含多项与Agent协同相关的功能增强。在权限控制方面，`tool.check`事件新增`agentId`字段，使钩子能够识别工具检查请求来自主会话还是子代理，为多Agent环境下的差异化权限策略奠定了基础。同时，该事件的裁决与问题中新增`ceiling`字段，可以表示组织对工具使用的最低审批级别，这有助于实施层级审批流程。在可观测性方面，`turn.step`钩子返回值新增`serverToolUses`，记录API自身运行的工具调用详情，包括id、名称、输入和起止时间，增强了多Agent链路的透明度。另外，新增`/claude-api managed-agents-onboard`命令支持从文件或快速启动模板（如deep-researcher）创建Managed Agents模式，降低了复杂Agent工作流的搭建门槛。这些特性直接涉及多Agent编排、权限协同与审计，具有明确的方法论价值。

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

确认收录：`python3 promote_candidate.py 2026-10-13_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-10-13_anthropics-claude-code_release.md --reject --reason "..."`
