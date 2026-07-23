# 行业学习 · Schema（行为说明书）

> 范围：方法论转正Agent · 行业自学习线 · AI协同方法论方向（早期原型试跑）
> 参照 Karpathy LLM-Wiki 模式（[原文](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)），本文件是这个主题工作区的规则手册

---

## 三层结构

```
行业学习/
├── CLAUDE.md          ← 本文件，规则手册
├── raw/                ← 原始资料层（人工放入，AI 只读，不改）
│   └── README.md
└── wiki/                ← 知识库层（AI 摄入后维护）
    ├── index.md          ← 总目录，每次 ingest 后更新
    ├── log.md            ← 操作日志，仅追加
    ├── entities/          ← 人/公司/产品/工具等实体页
    ├── concepts/          ← 方法论原理/技术术语等概念页
    ├── sources/            ← 每篇原始资料的摘要页
    └── comparisons/         ← 跨资料横向对比页
```

## Frontmatter 字段（详见 `_schema定义.md`）

每份 `wiki/` 下的页面需挂载：`source_url` / `collected_at` / `staleness_review_date` / `info_type` / `evidence_basis`。这套字段独立于 OB 现有五字段 schema，理由见 `_schema定义.md`。

**跨知识源融合前提（2026-07-23 与 OBAgent 对齐）**：若未来要复用 OB 现有的 entity_ref 枢纽/矛盾扫描机制，本目录卡片还需额外挂载 `entity_type`/`entity_ref` 两个字段，命名和取值方式需跟 OBAgent 的 `concept_atom` schema 保持一致。早期原型阶段暂不强制，等真实卡片产出、双方对着真实数据验证后再决定怎么填，见 `_schema定义.md` 对应说明。

## 三项操作

1. **摄入（Ingest）**：读 `raw/` 里的一份新资料 → 提炼核心要点（与 Jasper 讨论确认）→ 判断是否创建新概念/实体页（准则：至少跨两篇资料出现才建新概念页，否则先记进对应 `sources/` 摘要页里，不急着拆页）→ 若已有相关页面，优先合并（新增小节+回链源头），不重复新建 → 同时跟 vault 内 `Jasper AI协同经验引擎/` 目录下已有的 L1-L16 系列方法论笔记做交叉比对，标注是佐证/补充/矛盾 → 更新 `index.md` 和 `log.md`

   **`index.md` 只做索引，不重复内容（2026-07-23 补充，真实ingest后发现的偏差）**：还没达到独立建页门槛的概念/实体，其**完整内容只写一份，放在对应的 `sources/` 摘要页里**；`index.md` 对应条目只放一行链接+一句话指向那个 sources 页面，不要把概念的定义/场景/特性等内容再摘要一遍写进 `index.md`。同一份内容分裂成"sources页详细版+index.md摘要版"两处，后续更新容易漏改其中一处导致两边说法对不上，`index.md` 也会因为塞了实际内容而越写越臃肿、失去"一眼看清全局"的索引作用。等概念/实体真正升级成 `concepts/`/`entities/` 下的独立页面后，`index.md` 再改成链接指向那个新页面，同样只放链接不复制内容。
2. **查询（Query）**：先读 `index.md` 定位相关页 → 深入读页面 → 综合作答并标注引用来源 → 好答案可以写回 `wiki/` 作为新页面，形成积累
3. **维护（Lint）**：定期检查 `wiki/` 内矛盾说法、孤儿页（无反向链接）、过时信息（对照 `staleness_review_date`）

## 明确边界（不追求自动化，早期原型阶段）

- 目前所有操作均为人工/对话驱动，不是自动化脚本
- `raw/` 只能人工放入资料，AI 不主动抓取（收集过滤机制 v0 仍是人工判断，见需求定义.md 五节）
- 与 OB 现有检索系统（`get_context()`）的关系仍是待裁定项，本文件不预设结论
