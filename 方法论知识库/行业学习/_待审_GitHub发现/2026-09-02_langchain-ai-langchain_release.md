---
status: pending_review
discovered_at: 2026-09-02T21:31:43.895743
source_type: release
source_repo: langchain-ai/langchain
source_url: https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a4
direction: AI协同方法论
relevance_reason: 命中：LangChain MCP适配器引入ClientGroup和中断路由，直接涉及多客户端Agent与工具服务器之间的协同与中断处理机制。
info_type_suggestion: 业界实践
evidence_basis_suggestion: 行业佐证
stage1_filter_reason: release正文39702字符，超过50字符阈值放行
---

# 摘要

LangChain 1.4.0a4及多个alpha版本针对MCP集成进行了迭代：引入ClientGroup作为MCPAdapter的目标，支持多个MCP客户端组；将MCP工具元数据分组到mcp命名空间；实现基于协商协议时代的中断路由；通过成员会话驱动MCP elicitation；新增_ReentrantClientGroup支持可重入；将fastmcp依赖升级到4.0.x；重构MCPAdapter接口并标记beta；要求MCP目标为http(s) URL；调整转换函数命名等。这些改动聚焦于Agent与多MCP服务器之间的协同、中断处理和协议协商，为多工具Agent编排提供了基础设施支持，属于业界实践中Agent协同机制的演进。

## 原始信息

- 标题/来源: langchain==1.4.0a4
- 发布/变更时间: 2026-09-02T05:35:20Z
- 原文链接: https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a4
- 原文摘录（截断）:

```
Initial release

release(langchain): 1.4.0a4
test(langchain): cover mixed-era ClientGroup and group elicitation
Update libs/langchain_v1/langchain/mcp/adapter.py
fix(langchain): drive MCP elicitation via member session for fastmcp 4.0.1
fix(sdk): use latest fastmcp and rm reentrant impl
cr
cr
refactor(langchain): inline MCP client arming into `__init__`
refactor(langchain): stamp an arm marker instead of introspecting the handler closure
fix(langchain): gate MCP interrupt routing on the negotiated protocol era
refactor(langchain): drop MCP `elicitation` flag, derive interrupt routing from the client
fix(sdk): add _ReentrantClientGroup
fix(langchain): narrow `MCPAdapter.client` union in mcp tests for mypy
chore(langchain): format `mcp/adapter.py`
release(langchain): 1.4.0a3
feat(langchain): group MCP tool metadata under an `mcp` namespace
refactor(langchain): stop exporting `MCPAdapterTarget` from `langchain.mcp`
refactor(langchain): rename `convert_mcp_tool_to_langchain_tool` to `as_langchain_tool`
refactor(langchain): rename `MCPAdapter.get_tools` to `list_tools`
feat(langchain): expose `cache_mode` on `MCPAdapter.get_tools`
chore(langchain): require `fastmcp` 4.0.0
feat(langchain): accept a `ClientGroup` as an `MCPAdapter` target
feat(langchain): mark the `langchain.mcp` namespace as beta
Revert "feat(langchain): accept a `ClientGroup` as an `MCPAdapter` target"
feat(langchain): accept a `ClientGroup` as an `MCPAdapter` target
chore(langchain): require `fastmcp` 4.0.0b5
fix
```

## 人工确认后如何操作

确认收录：`python3 promote_candidate.py 2026-09-02_langchain-ai-langchain_release.md --promote`
（或手动：把上面"摘要+原始信息"整理后另存为 raw/ 下的新md文件，frontmatter
补齐 collected_at/staleness_review_date，source_url/info_type/evidence_basis
从建议值确认或改写后带过去）

不收录：`python3 promote_candidate.py 2026-09-02_langchain-ai-langchain_release.md --reject --reason "..."`
