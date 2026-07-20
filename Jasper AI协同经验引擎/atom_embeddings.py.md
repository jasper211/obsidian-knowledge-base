---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/OB/README.md
extracted_at: 2026-07-20T12:26:17
---

# atom_embeddings.py

tools/atom_embeddings.py 负责原子语义去重，复用 obsidian-mcp-server 的 vector.mjs 中的 getEmbeddings 能力。当本机无 OPENAI_API_KEY 时，优雅退回精确匹配去重，不崩溃。

## 关联概念

- [[批量增量提炼]]
