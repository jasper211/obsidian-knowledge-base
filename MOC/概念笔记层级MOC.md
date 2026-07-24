---
tags: [MOC, 导航, 概念网络]
project: 知识管理
source_type: MOC
created: 2026-07-15
updated: 2026-07-24
---

# 概念笔记层级 MOC

## 一句话定义
概念笔记层级 MOC 是 **vault内schema体系的分层导航**，按"顶层目录归属→原子schema字段→原子分类体系"组织，帮助理解一个具体原子/卡片"是什么、从哪来、可信度如何"。

> 2026-07-24重写：上一版按"RW权益项目/AI协同类/知识管理类"划分22个概念，
> 链接的大部分概念页实际不存在，且框架本身（三项目+VNW/AIT桥梁）跟现状
> 不符。本次改成按"vault实际结构+原子schema"重新组织，是重写不是修补。

---

## L1：4个顶层目录（内容来源分层）

| 目录 | 负责方 | 说明 |
|---|---|---|
| `EA流程架构项目/` | OB | 项目知识原子 |
| `Jasper AI协同经验引擎/` | OB | Agent协同经验知识原子 |
| `方法论知识库/` | 方法论转正Agent | 行业知识卡片（Karpathy模式） |
| `MOC/` | 共用 | 导航 |

详见 [[跨项目关联MOC]]。

---

## L2：EA原子的schema字段体系

一个`concept_atom`原子的完整字段：

```yaml
type: concept_atom
concept_type: 规则|决策|定义|经验教训|背景说明
project / source
authority_layer: 00_治理|01_原始|02_草稿|02_定稿|03_已锁定|08_任务跟进
domain: PAY|HR|FA|KA|EQ|INS|PARTNER|TREASURY|（无）
confidence: UNSTATED|LOW|MEDIUM|HIGH
entity_type: <见下方L3分类体系>
entity_ref: <正式编码，如L3-CPM> | （无）
status: 生效|已废止|待裁定
```

- **authority_layer**：来源权威级别，检索时作为信任徽章显式标注给下游Agent
- **domain**：业务域，2026-07-22新增，只有EA项目有意义
- **status**：原子生命周期，2026-07-21新增，已废止的保留可追溯不物理删除

---

## L3：entity_type分类体系（2026-07-24确认）

### 正式编码类（对应EA自己的DIM_*字典）
- L3流程 / KPI / 价值流 / 岗位族 / （历史上曾有M战略，已撤回，见memory）

### 白名单来源类（2026-07-24新增，覆盖此前"待聚类"87%）
- **SOP** —— 05_SOP来源
- **Agent机制** —— Agent执行机制梳理来源
- **规则与GAP** —— 04_规则与GAP产出来源
- **方法论标准** —— M-01方法论与标准来源
- **规则空白** —— 规则空白地图来源
- **信号基线** —— 提取合集校准（信号提取基线）来源
- **熔断规则** —— 熔断节点补建清单来源

### 未分类
- 待聚类 / 非正式主题（现在只剩约1.1%，主要是项目章程等小体量来源）

---

## L4：知识枢纽（entity_ref精确匹配 + embedding聚类）

- **entity_ref枢纽**：同一正式编码下的原子挂载在同一个hub
- **embedding聚类枢纽**：无正式编码但语义相似的原子（threshold=0.72+LLM连贯性判断），单枢纽硬上限15个原子

详见 [[知识枢纽索引]]。

---

## 方法论知识库的独立结构（Karpathy模式，不套用上面的concept_atom schema）

```
方法论知识库/行业学习/
├── CLAUDE.md          规则手册
├── raw/                原始资料（只读）
└── wiki/
    ├── index.md          总目录（只做索引，不重复内容）
    ├── log.md            操作日志
    ├── sources/          每篇资料的摘要页
    ├── concepts/          跨2篇资料才建的独立概念页
    ├── entities/          实体页
    └── comparisons/        横向对比页
```

frontmatter字段独立于`concept_atom`：`source_url`/`collected_at`/`staleness_review_date`/`info_type`/`evidence_basis`，可选挂`entity_type`/`entity_ref`用于跟EA原子的硬关联（见[[跨项目关联MOC]]）。

---

## 使用指南

1. **想知道某个原子可信度高不高** → 看`authority_layer`+`confidence`
2. **想按业务域找EA的规则/SOP** → 看`domain`字段
3. **想知道某类内容属于什么性质** → 看`entity_type`落在"正式编码类"还是"白名单来源类"
4. **想看方法论知识库的东西** → 走Karpathy三层结构，不是concept_atom schema

---

## 变更记录

| 日期 | 说明 |
|---|---|
| 2026-07-15 | 初版，按RW权益项目/AI协同类等22个概念划分L1/L2/L3 |
| 2026-07-24 | 全面重写，改为按vault顶层目录+原子schema字段+entity_type分类体系组织 |
