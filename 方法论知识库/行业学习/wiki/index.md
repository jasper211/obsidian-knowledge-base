---
type: wiki_index
scope: 方法论转正Agent-行业自学习线-AI协同方法论方向
updated: 2026-07-24 10:30
last_ingest: 2026-07-24 - Loop Engineering (新源头：AI系统工程架构)
total_sources: 3 (LLM Wiki + 本体推理 + 循环工程)
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

### 2026-07-24：AI 系统工程与自动化架构

- [[wiki/sources/循环工程与AI系统架构设计]] - LangChain 官方博文深度拆解，循环工程的四层架构
  - 核心洞察：从"提示词工程"到"循环工程"的范式转变（2026年6月正式定义）
  - 四层架构：Agent Loop → Verification Loop → Event-driven Loop → Hill Climbing Loop
  - 核心价值：多层循环嵌套的完整管控体系（差异化竞争壁垒）
  - **人机协同**：四层循环每一层预留人工介入点，确保可控性
  - 📚 来源：LangChain 官方博客（The Art of Loop Engineering）

## entities/（实体页，尚未有独立页面，暂记于此）

- Andrej Karpathy——完整信息见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]
- Obsidian（Web Clipper 工具）——完整信息见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]

## concepts/（概念页，尚未有独立页面，完整内容见对应 sources 页，此处只做索引）

### 知识管理与表示维度
- **LLM Wiki 范式** / **RAG 范式** —— 完整定义/场景/特性见 [[wiki/sources/Karpathy_LLM-Wiki知识管理范式]]
- **本体推理范式** —— 完整内容见 [[wiki/sources/本体推理与知识图谱实践]]

### AI 系统工程维度
- **循环工程范式（Loop Engineering）** —— 完整定义/四层架构见 [[wiki/sources/循环工程与AI系统架构设计]]
  - Agent Loop / Verification Loop / Event-driven Loop / Hill Climbing Loop
  - 差异化竞争力来源：多层循环嵌套的完整管控体系

### 与 Jasper 协同的关键对标（索引，完整映射说明见各 sources 页）

- **AI 人分工哲学** ←→ [[Jasper AI协同经验引擎/AI人分工哲学]]
  - LLM Wiki：AI 从工具升维为协作者
  - 本体推理：AI 作自动推理引擎
  - 循环工程：机器负责标准化工作，人类负责价值判断（详见三份 sources 页）

- **AI 是判断力放大器** ←→ [[Jasper AI协同经验引擎/AI是判断力放大器]]
  - LLM Wiki：人审核、AI 编译的分工
  - 本体推理：人定规则、AI 推导新知识
  - 循环工程：四层循环每层预留人工介入点（详见三份 sources 页）

- **知识工程方法** ←→ [[Jasper AI协同经验引擎/知识工程方法]]
  - 本体推理：本体定义是规则显式化的形式
  - 循环工程：四层循环是工程化流程的显式化
  - 系统性规则管理的不同实现方式

## comparisons/（横向对比页）

- [[wiki/comparisons/RAG-vs-LLM-Wiki对比]] - RAG 与 LLM Wiki 的范式对立与互补分析
  - 哲学差异：运行时检索 vs 编译时编译
  - 适用金字塔：L1 热数据 (LLM Wiki) vs L2 温数据 (RAG) vs L3 冷数据 (预训练)
  - 三个维度的优劣权衡
  - 混合方案建议
