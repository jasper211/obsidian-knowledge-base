---
status: pending_review
discovered_at: 2026-08-09T20:43:26.915957
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.224
direction: AI协同方法论
relevance_reason: 引入跨会话通信控制与发现机制，直接涉及多Agent编排与协同治理
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文4740字符，超过50字符阈值放行
---

# 摘要

本次更新显著增强了Claude Code的Agent协同能力：新增crossSessionInbound和dialogExpiry设置，允许对跨会话消息进行审批控制，为多Agent通信引入了细粒度治理；同时SendMessage与ListAgents功能正式上线，使Agent能够跨机器发现并彼此通信，这是多Agent编排的基础范式。此外，新增的自托管执行环境(self-hosted-runner)使得Agent可以在自定义环境中运行，为协同提供了部署层面的支撑。这些特性共同构成了Agent间协同编排的框架。

## 原始信息

- 标题/来源: v2.1.224
- 发布/变更时间: 2026-08-07T04:00:59Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.224
- 原文摘录（截断）:

```
## What's changed

- Added self-hosted environments: `claude self-hosted-runner` turns your own machines or containers into a place Claude Code web, mobile, and desktop sessions can run, on Team and Enterprise plans
- Added `archive` plugin source: install plugins from a zip over HTTPS without git or npm, with optional SHA-256 pinning
- Added a cancel-and-confirm step when removing an unavailable paste changes a command's text
- Added `ANTHROPIC_BEDROCK_REGION_PREFIX` env var for Bedrock to prefer a specific cross-region inference profile over the `AWS_REGION`-derived one
- Added `crossSessionInbound` and `dialogExpiry` settings: cross-session messages sent to a session running with bypassed permissions are held for your approval, and messages to other sessions auto-deliver
- Added sandbox credential-masking options: `extract` and `onExtractNoMatch` for structured env values, `decode: "jwt"` with `maskClaims` for JWT-aware masking, and `awsPairs`/`sigv4` for AWS SigV4 re-signing; these need `network.tlsTerminate` and are honored only from user, managed, or `--settings` settings
- Added cross-session `SendMessage`: Claude Code sessions can now message each other, on any of your machines, with `ListAgents` to discover them (macOS and Linux)
- Fixed long (>200 char) project paths resolving to another project's session directory under a shared sanitized prefix; session list, rename, fork, delete and `/resume` no longer cross projects
- Fixed `SendMessage` reporting "Message sent"
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-08-09_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-08-09_anthropics-claude-code_release.md --reject --reason "..."`
