---
status: pending_review
discovered_at: 2026-08-25T21:31:44.291656
source_type: release
source_repo: langgenius/dify
source_url: https://github.com/langgenius/dify/releases/tag/1.17.0
direction: AI协同方法论
relevance_reason: 命中多项AI协同方法论主题：Agent沙箱后端扩展（E2B）、构建时主目录快照、工作区级技能管理、上下文感知历史压缩、工作流中可复用LLM环境变量、循环节点内人机交互表单，直接涉及多Agent编排、人机分工与Agent运行环境治理。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文116393字符，超过50字符阈值放行
---

# 摘要

Dify v1.17.0发布包含多项Agent与工作流相关的能力增强。在Agent运行时方面，新增E2B云沙箱后端，允许Agent的shell/代码执行在云端进行，并通过DIFY_AGENT_RUNTIME_BACKEND切换；构建时主目录快照功能在发布Agent时捕获其沙箱主目录状态，后续运行从该快照恢复，确保执行环境一致。工作区级的Skill管理提供了可复用、版本化的能力打包机制，包含草稿-发布-版本生命周期及Web UI管理，支持Agent发现和调用技能。上下文感知历史压缩通过解析模型上下文窗口并分层压缩，使长对话保持在预算内且不丢失近期上下文。工作流方面，新增可复用的LLM环境变量，允许在多个LLM节点间共享模型配置，减少漂移。此外，Human-in-the-loop表单现在支持在Loop和Iteration节点内部使用，使人机交互可以嵌入循环流程，增强了人机分工编排的灵活性。这些改动提供了多Agent编排、运行环境治理、上下文管理以及循环中人机交互的具体工程实现，对AI协同方法论有较高参考价值。

## 原始信息

- 标题/来源: v1.17.0
- 发布/变更时间: 2026-08-25T11:28:25Z
- 原文链接: https://github.com/langgenius/dify/releases/tag/1.17.0
- 原文摘录（截断）:

```
## New Features

**Agent: E2B Sandbox, Home Snapshots, and Skill Management**
- **E2B sandbox backend**: agent shell/code execution can now run on [E2B](https://e2b.dev) cloud sandboxes in addition to the local sandbox. Select the backend with `DIFY_AGENT_RUNTIME_BACKEND`; a new `docker-compose.e2b.yaml` ships the E2B stack, E2B traffic is authenticated, and the E2B template is synced on release (#39480, #39705, #39873, #39996, #40858, #40871, #40891, #40892).
- **Build-time Home Snapshots**: when an agent build is applied (published), the agent's sandbox home directory — installed packages, prepared files, working state — is captured and subsequent runs of the published agent restore their home directory from that snapshot, so the agent starts from the exact filesystem state it had at build time. (#39702, #40876, #40996).
- **Workspace-level Skill management**: Skills are reusable, versioned capabilities packaged with code and tool definitions that agents can discover and invoke. A new workspace-level skills manager with draft → publish → version lifecycle ships alongside a web UI (skill listing, builder panel, file editor).  (#39675, #39798, #39799, #41180).
- **Context-aware history compaction**: long agent conversations no longer blow past the model's context window — Dify resolves each model's effective window and tiers compaction (clear old tool results first, then summarize older history) so runs stay within budget without losing recent context (#40872).

**Reu
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-08-25_langgenius-dify_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-08-25_langgenius-dify_release.md --reject --reason "..."`
