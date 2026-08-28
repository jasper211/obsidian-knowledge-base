---
status: pending_review
discovered_at: 2026-08-26T21:30:52.154028
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
direction: AI协同方法论
relevance_reason: 变更中包含了多个与Agent协同机制直接相关的改进，如子代理fallback模型链和错误信息传递、后台代理错误输出防溢出等。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文5517字符，超过50字符阈值放行
---

# 摘要

本次更新（v2.1.247）主要包含功能新增和问题修复。在Agent协同方面，修复了子代理在首次调用模型遇到404错误时崩溃的问题，现在子代理会使用会话的fallback model chain，并将错误类型、状态、请求ID和模型信息返回给父代理；同时修复了hook或后台代理打印大量错误输出导致会话溢出的问题。此外，还新增了SendFeedback工具，允许Claude在出现问题时起草反馈报告供用户审核发送；新增了/spinnerTipsOverride的自定义提示轮换支持；增加了Bash权限提示的自动模式引导；新增了/claude-api cost-optimize命令用于分析API成本并逐步优化；更新了/claude-api技能以覆盖Admin API；以及修复了键盘导航、终端设置合并、沙箱清理等多个问题。

## 原始信息

- 标题/来源: v2.1.247
- 发布/变更时间: 2026-08-26T23:06:39Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.247
- 原文摘录（截断）:

```
## What's changed

- Added the `SendFeedback` tool: when something goes wrong in a session, Claude can draft a feedback report for you to review and send from `/feedback` (turn off with the `feedbackDrafts` setting)
- Added `{id, text, cooldownSessions, priority}` entries, `tipsFile`, and `label` to `spinnerTipsOverride`, so organizations can rotate their own tips alongside the built-in ones
- Added a tip on Bash permission prompts pointing to auto mode, with a one-keystroke "Yes, and switch to auto mode" option
- Added `/claude-api cost-optimize` to profile an existing project's Claude API spend and work through cost levers (caching, token hygiene, batch, effort, model choice) one measured change at a time
- Updated the `/claude-api` skill with Admin API coverage (organization members, invites, workspaces, API keys, rate limit reports, workload identity federation, CMEK)
- Fixed fast arrow-key + Enter sequences acting on the row above the one you navigated to in history search, `/config`, `/mcp`, `/skills`, background tasks, and `/model`
- Fixed sub-agents dying on a first-call model 404: they now use the session's fallback model chain, and the error returned to the parent includes the error type, status, request id, and model
- Fixed a hook or background agent that printed megabytes of error output being able to overflow the conversation and wedge the session on "Prompt is too long"
- Fixed Ctrl keyboard shortcuts not firing under non-Latin (e.g. Cyrillic) keyboard layouts 
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-08-26_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-08-26_anthropics-claude-code_release.md --reject --reason "..."`
