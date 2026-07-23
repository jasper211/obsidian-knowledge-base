---
type: wiki_index
scope: 方法论转正Agent-行业自学习线-AI协同方法论方向
updated: 2026-07-23 15:15
last_ingest: 2026-07-23 15:15 - demo-ontology (新源头：本体推理与知识图谱)
total_sources: 2 (LLM Wiki + 本体推理)
---

# 行业学习 · 总目录

> 跟踪行业前沿方法论的演进。每次 ingest 后更新。

## sources/（原始资料摘要页）

### 2026-06-20 → 2026-07-23：知识管理范式论（双源头）

- [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]] - Andrej Karpathy 的 LLM Wiki 范式，对标 RAG 的编译型知识管理
  - 核心洞察：从"检索时理解"转向"编译时理解"
  - 关键数据：40万字、100篇文章的验证规模
  - 与 Jasper AI 协同模式的对标关系
  - **补充摄入**（2026-07-23）：行业应用细分、实施策略、回音壁补充分析
  - 📚 来源：CSDN文章 + 知识库版本（已合并）

### 2026-07-23：知识形式化与推理架构

- [[wiki/sources/本体推理与知识图谱实践]] - demo-ontology 项目示例，展示本体推理在订单系统中的应用
  - 核心洞察：从"硬编码规则"到"声明式本体推理"的范式转变
  - 技术栈：Python, owlready2, OWL/RDF 标准化格式
  - 应用场景：订单管理、医疗诊断、法律合规检查
  - **新维度**：本体推理与 LLM Wiki 的互补关系（文本化 vs 形式化）
  - 📚 来源：GitHub 项目（pingcy/demo-ontology）

## entities/（实体页，尚未有独立页面，暂记于此）

- Andrej Karpathy——完整信息见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]
- Obsidian（Web Clipper 工具）——完整信息见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]

## concepts/（概念页，尚未有独立页面，完整内容见对应 sources 页，此处只做索引）

- **LLM Wiki 范式** / **RAG 范式** —— 完整定义/场景/特性见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]
- **本体推理范式** —— 完整内容见 [[wiki/sources/本体推理与知识图谱实践]]

### 与 Jasper 协同的关键对标（索引，完整映射说明见各 sources 页）

- **AI 人分工哲学** ←→ [[Jasper AI协同经验引擎/AI人分工哲学]]，详见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]、[[wiki/sources/本体推理与知识图谱实践]]
- **AI 是判断力放大器** ←→ [[Jasper AI协同经验引擎/AI是判断力放大器]]，详见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]、[[wiki/sources/本体推理与知识图谱实践]]
- **知识工程方法** ←→ [[Jasper AI协同经验引擎/知识工程方法]]，详见 [[wiki/sources/本体推理与知识图谱实践]]

## comparisons/（横向对比页）

- [[wiki/comparisons/RAG-vs-LLM-Wiki对比]] - RAG 与 LLM Wiki 的范式对立与互补分析
  - 哲学差异：运行时检索 vs 编译时编译
  - 适用金字塔：L1 热数据 (LLM Wiki) vs L2 温数据 (RAG) vs L3 冷数据 (预训练)
  - 三个维度的优劣权衡
  - 混合方案建议
