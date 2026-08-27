---
status: pending_review
discovered_at: 2026-08-25T21:31:44.289371
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
direction: AI协同方法论
relevance_reason: 命中AI协同方法论中的人机分工模式（新增自动模式分类器规则编辑界面）与多Agent编排交互（动态工作流重启子代理前询问确认），且包含MCP工具中断错误报告的改进，这些涉及Agent协同机制的工程实践。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文9261字符，超过50字符阈值放行
---

# 摘要

Claude Code v2.1.246发布包含多项改进。与AI协同方法论直接相关的内容包括：在`/permissions`下新增Auto模式标签页，用于查看和编辑自动模式分类器规则，增强了对人机分工中自动执行边界的管理；修复了动态工作流中按左箭头或运行`/background`会重新启动已完成的子代理的问题，现在会先询问并提示将重启的子代理数量，改进了多Agent编排中的安全交互；修复了MCP工具调用在无头/远程会话中被传入消息打断时被错误报告为“无输出完成”而非显式中断错误的问题，提升了Agent工具调用的状态可见性。此外还包含大量常规修复，如启动警告、全屏模式渲染、长行diff导致的转录性能、后台会话启动失败、Markdown渲染、命令中断显示等。整体上该版本以功能性修复为主，但其中关于自动模式权限管理、子代理重启确认以及工具中断错误报告的改动，为多Agent协同与人机分工提供了具体工程案例，具备一定参考价值。

## 原始信息

- 标题/来源: v2.1.246
- 发布/变更时间: 2026-08-25T22:31:52Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
- 原文摘录（截断）:

```
## What's changed

- Added a startup warning for Bash allow rules with a wildcard before the subcommand (e.g. `Bash(git * main)`), since they also match options inserted before the subcommand
- Added an Auto mode tab to `/permissions` for viewing and editing auto mode classifier rules
- Added the turn's completion time to the end-of-turn duration line, e.g. `✻ Sautéed for 23s · done 6:05 PM`
- Fixed fullscreen mode showing a blank transcript after resizing the terminal and jumping to the bottom until the next keypress
- Fixed a severe transcript slowdown when a diff contained a very long single line (e.g. a base64 string); such lines now render truncated with a marker
- Fixed erratic fullscreen scrolling when positioned at an earlier message, including jump-to-bottom getting stuck mid-transcript
- Fixed background sessions failing to open after 45 seconds when Claude Code's starting directory had been deleted, the machine had slept, or the host is slow to start processes
- Fixed background sessions failing to open with "Couldn't start the background service … EACCES" when another Claude Code process was re-installing the npm package at that moment
- Fixed markdown rendering being disabled for a whole message when its first 500 characters contained no markdown, and for `+`/`N)` lists and setext headings
- Fixed MCP tool calls interrupted by an incoming message in headless/remote sessions being reported to the model as "completed with no output" instead of an explicit interrupt
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-08-25_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-08-25_anthropics-claude-code_release.md --reject --reason "..."`
