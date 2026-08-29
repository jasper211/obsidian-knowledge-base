---
status: pending_review
discovered_at: 2026-08-27T21:32:10.723138
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
direction: AI协同方法论
relevance_reason: 新增跨会话消息传递（SendMessage/ListAgents）机制，直接支持同一机器上多个Agent会话之间的通信与协同，属于多Agent编排范式的具体实现
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文8381字符，超过50字符阈值放行
---

# 摘要

Claude Code v2.1.248发布说明包含多项新功能和修复。其中与AI协同方法论直接相关的是新增跨会话消息传递能力：在Bedrock、Vertex、Foundry等平台上，同一机器上的不同会话可以通过SendMessage和ListAgents相互通信，即使禁用遥测也能使用。这为多Agent协作提供了底层通信机制，使不同会话能够交换信息，是实现多Agent编排的基础设施。此外，还引入了experimental.cacheTtl，允许为每个Agent设置独立的提示缓存TTL，用于优化子代理的缓存策略，这属于多Agent系统中的资源管理优化。其他变更如--restricted模式、自托管运行器标签、设置诊断、使用量信用等，主要涉及安全、部署和运维，与协同方法论关系不大。该版本来自Anthropic官方，技术说明具体，提供了可验证的新协作机制，值得人工进一步评审。

## 原始信息

- 标题/来源: v2.1.248
- 发布/变更时间: 2026-08-27T22:12:20Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
- 原文摘录（截断）:

```
## What's changed

- Added `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in tools that run commands or code and `WebFetch` (unless named in `--tools`), keeps file tools inside the working directory, refuses `bypassPermissions`, and ignores user, project and local settings files
- Added `experimental.cacheTtl` (`"5m"` or `"1h"`) to agent frontmatter: a per-agent prompt cache TTL used when no subagent TTL setting is configured
- Added `claude self-hosted-runner --client-label <label>` (or `SELF_HOSTED_RUNNER_CLIENT_LABEL`) to override the label the runner registers with (default: hostname)
- Added server-managed settings diagnostics: a startup warning when the settings fail to load, and a `/doctor` and `/status` line explaining a load failure or why they weren't fetched (Bedrock/Vertex/third-party provider, custom `ANTHROPIC_BASE_URL`)
- Added a warning in `/web-setup` when the GitHub CLI token lacks the `workflow` scope, since pushes to very large repositories can be rejected without it
- Added `/usage-credits` for Enterprise organizations billed through AWS Marketplace, self-serve Enterprise, and Enterprise trials, so members can request a higher usage limit from their admin
- Added cross-session messaging (`SendMessage` / `ListAgents`) between sessions on the same machine on Bedrock, Vertex, and Foundry, and when telemetry is disabled
- Fixed a prompt-cache miss (and lost extended-thinking context) roughly once an hour in long sessions, caused by tool def
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-08-27_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-08-27_anthropics-claude-code_release.md --reject --reason "..."`
