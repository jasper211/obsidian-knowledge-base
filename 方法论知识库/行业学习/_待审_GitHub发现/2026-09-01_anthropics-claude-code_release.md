---
status: pending_review
discovered_at: 2026-09-01T21:32:14.749993
source_type: release
source_repo: anthropics/claude-code
source_url: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
direction: AI协同方法论
relevance_reason: 包含多项直接涉及Agent协同和权限治理的变更，如Containment Escape规则、子代理模型强制、一次性权限提示等
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文16256字符，超过50字符阈值放行
---

# 摘要

本次版本更新（v2.1.257）引入了多项安全与协作相关的改进。在权限控制方面，新增了Containment Escape规则，防止自动模式自动批准云元数据凭据获取、出口规避和跨租户访问等敏感操作；新增一次性提示，在自动模式下首次读取工作目录外文件前询问用户，并支持通过设置完全阻止此类读取。在多Agent编排方面，新增环境变量CLAUDE_CODE_SUBAGENT_MODEL_FORCE，可强制所有子代理使用指定模型，忽略单独的生成或代理定义覆盖，简化了模型管理。此外，还增加了对网关提供的模型描述的支持，改进了模型发现体验。其他变更包括新增Claude Fable 5.1模型、时间格式设置、/effort命令会话级调整、/doctor对陈旧沙箱掩码文件的警告，以及若干会话、权限模式、键绑定和后台会话相关的修复。总体而言，本次更新在Agent权限边界和子代理模型控制上提供了更细粒度的治理手段。

## 原始信息

- 标题/来源: v2.1.257
- 发布/变更时间: 2026-09-01T17:53:52Z
- 原文链接: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
- 原文摘录（截断）:

```
## What's changed

- Added Claude Fable 5.1 (`claude-fable-5-1`), now the default Fable model — 1M context, $10/$50 per Mtok with $0.25/Mtok cache reads
- Added "Time format" (`timeFormat`) and `timeZone` settings: 12-hour, 24-hour, 24-hour UTC, or a strftime pattern for the turn-end clock and transcript-view timestamps
- Added a Containment Escape rule to auto mode so cloud metadata-credential fetches, egress evasion, and cross-tenant reach are no longer auto-approved unless your environment marks them expected
- Added `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` to apply `CLAUDE_CODE_SUBAGENT_MODEL` (or the main model) to every subagent, ignoring per-spawn and agent-definition model overrides
- Added `s` in `/effort` to change effort for the current session only, matching `/model`
- Added a `/doctor` warning for stale sandbox mask files left by a killed session
- Added a one-time prompt in auto mode before the first file read outside the working directories, with the option to block such reads (`permissions.blockReadsOutsideWorkingDirectories`)
- Added support for a gateway-supplied `description` on discovered `/model` picker entries (`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY`); entries without one still read "From gateway"
- Fixed settings in a `.claude/` folder created after startup not being picked up until restart
- Fixed sessions dispatched from an agent view opened with `←` always starting in the original session's permission mode, overriding the target directory's `defaultMo
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-09-01_anthropics-claude-code_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-09-01_anthropics-claude-code_release.md --reject --reason "..."`
