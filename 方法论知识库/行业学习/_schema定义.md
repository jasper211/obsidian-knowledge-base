---
type: schema_design
project: 方法论知识库
scope: 方法论转正Agent-行业自学习线-AI协同方法论方向
status: 草稿-早期原型
created: 2026-07-22
updated: 2026-07-23
---

# 行业自学习线 · 源文档 Schema 定义（草案）

> 本目录用于存放"方法论转正Agent·行业自学习线·AI协同方法论方向"早期原型试点采集的行业信息源文档。
> 当前目录为空——这是 schema 设计阶段，尚未开始真实采集，避免虚构示例内容。

## 为什么需要独立 schema

不能直接复用 Jasper AI协同经验引擎项目现有的五字段 schema（`type`/`concept_type`/`project`/`source`/`extracted_at`）——那套 schema 面向内部一手项目文档，可信度和时效语义与外部二手行业信息不同。详见《行业自学习线_启动与执行方案_v1.0》二节结论4。

## 字段定义

| 字段 | 说明 | 取值示例 |
|------|------|---------|
| `source_url` | 信息的原始来源链接 | 具体 URL，或"无公开链接，来自XX访谈/内部转述"等说明 |
| `collected_at` | 采集时间 | ISO 8601 时间戳 |
| `staleness_review_date` | 时效复核周期到期日，过期需重新核实是否仍然适用 | 日期 |
| `info_type` | 信息性质分类 | `业界实践` / `学术研究` / `竞品动作` |
| `evidence_basis` | 与内部已有经验的关系 | `内部佐证` / `行业佐证` / `两者皆有` |
| `entity_type`（可选，预留） | 若未来要接入 OB 现有 entity_ref 枢纽/矛盾扫描机制，命名需与 OBAgent 的 `concept_atom` schema 保持一致 | 早期原型阶段可留空，见"跨知识源融合前提" |
| `entity_ref`（可选，预留） | 同上 | 同上 |

## 跨知识源融合前提（2026-07-23 与 OBAgent 对齐）

- 2026-07-23：本目录已从原先嵌套的 `Jasper AI协同经验引擎/方法论转正Agent/行业学习/` 迁移到 vault 顶层 `方法论知识库/行业学习/`——跟 OBAgent 已建的顶层占位文件夹（`方法论知识库/README.md`）统一，OBAgent 的每日白名单自动化（仅扫 `EA流程架构项目`/`Jasper AI协同经验引擎`）不会碰这个顶层文件夹，隔离更可靠
- OBAgent 侧的接口设计详见 OB 代码仓库 `03_规划项目结构_Plan_Project_Structure/提炼标准_v1.0.md`"与方法论Agent的接口"一节（不在本项目仓库内，无法直接核实，以 `方法论知识库/README.md` 里的摘要为准）
- 硬关联走 entity_ref 精确匹配、软关联走 embedding 聚类、晋升机制、跨知识源矛盾检测——这几点是 OBAgent 侧的设计，本文档不重复，仅记录依赖：需要本目录卡片挂 `entity_type`/`entity_ref` 才能接入

## 未决点

- 这些源文档最终是否/如何被 OB 的 `get_context()` 检索到，尚未正式确认（见方法论转正Agent需求定义.md 五节）
- 内部佐证与行业佐证并存时的合并/溯源标注格式，尚待设计（可能借用 VNW 规则级溯源模型，未拍板）
- `entity_type`/`entity_ref` 具体怎么填、跟 OBAgent 的 embedding 聚类阈值(0.72)等细节如何对齐，等本目录产出第一批真实卡片后再双方对着真实数据验证

## 关联

- [[方法论转正Agent双线]]
- [[方法论转正Agent]]
