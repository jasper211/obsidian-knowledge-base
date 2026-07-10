---
type: project_note
project: 流程架构
layer: "08_任务与跟进"
layer_tag: 任务
subdir: "任务状态"
tags: [任务]
---

## 🧭 导航
⬆️ [[08_任务与跟进]] · ⬆️ [[任务状态]] · 🏠 [[流程架构项目MOC]]

---

# 致 Terresa · fact_card 字典澄清与问题清单 · M4-W10

> **致**: Terresa (字典维护者) / **抄送**: Mark, Jasper
> **日期**: 2026-05-28
> **依据**: `DICT_流程数据库数据字典_V1_项目交付.md` (V1.0, 2026-04-22) + 2026-05-28 实测 mga_platform.process_analytics schema
> **来源**: Mark 5-27 第二轮回复指引"M1 材料已在字典中, 不需要额外提供" → Carrie 接手发现仍有 16 项需澄清
> **回复期望**: 5-28 晚 / 5-29 早上前部分回复 (B1 最紧急, 其余分批)

---

## 一、背景

Carrie 5-28 接手 fact_card Phase 1 灌数, 读完字典 V1.0 后**确认 90% 的字段级约束清晰**(类型 / 枚举 / CHECK / PK / FK 全有), 但仍有 16 项空白阻碍灌数方案落地, 整理供你回复。

字典层面建议出 V2.0 反映 DB 实际状态 (见 A1).

---

## 二、问题清单 (16 项, 分 6 组)

### A · 字典本身的更新建议

#### A1. 字典 V1.0 与 DB 实际严重不一致, 是否出 V2.0?

校对结果 (Carrie 2026-05-28 实测):

| DIM 表 | 字典 V1.0 声明 | DB 实测 | 偏差判定 |
|---|---|---|---|
| `dim_process` | 425 L4 | 425 | ✅ |
| `dim_vs` | VS-1~5 + L1-05 多阶段 | 36 | ✅ |
| `dim_org` | "粒度: 岗位级 (同族多岗位多人)" | **8 行** (岗位族级) | ⚠️ **粒度不一致** |
| `dim_time` | "Week 3 一次性 ~1461 行" | **0 行** | ❌ **硬阻塞** |
| `dim_agent` | 361 | 361 | ✅ |
| `dim_m_strategy` | M0-M8 共 9 行 | 9 | ✅ |
| `dim_kpi` | "Phase 2 才有, Week 6 录入" | **32 行 (新体系)** + 34 行 backup_20260524 (旧体系) | ⚠️ **字典严重落后**, 体系已重构 |
| `dim_deliverable` | "~253 (一 L4 一 deliverable)" | **400 行**, distinct_l4=400 | ⚠️ 比 dim_process 少 25 个 L4 |

**是否出 V2.0 反映当前真实状态?** 若是, Carrie 配合更新。

---

### B · 硬阻塞 / 前置依赖

#### B1. `dim_time` 0 行 — fact_card 灌库的硬阻塞 🔴

fact_card.time_key 强制 FK → dim_time(time_key), 字典 FC-006 校验规则说"必须存在于 DIM_TIME". dim_time 0 行 → fact_card **一行都灌不进**.

字典声明 "脚本生成 2024-01-01 至 2027-12-31 ~1461 行 (无外部依赖)" — 请告知:
- 这个生成脚本谁拥有? 是否在仓库里 (`schema/` 或 `scripts/`)?
- 5-28 晚 / 5-29 上午是否能跑出来?
- 如果没有现成脚本, Carrie 自己写一个 (`generate_series('2024-01-01', '2027-12-31', '1 day')`) 是否可接受?

**这一项不解锁, fact_card 5-29 CP1 验收无法推进**.

#### B2. `dim_deliverable` 缺 25 个 L4 的物理交付物

dim_process 425 L4 vs dim_deliverable 400. distinct_l4=400 — **25 个 L4 没有对应 deliverable**, 跟字典声明 "一 L4 一 deliverable (CLAUDE.md 5.0 节 L4 唯一物理交付物原则)" 矛盾.

- 这 25 个 L4 是哪些? (可以给 Carrie 一个 list 或 SQL)
- Phase 1 灌 fact_card 时, 这 25 个 L4 的 deliverable_key 留 NULL? (字典 FC-010 标 NULLABLE, 允许)
- 还是先补足 dim_deliverable 再灌 fact_card?

#### B3. `rework_alert_log` 表 + `trg_rework_alert` 触发器现状

字典 FC-022 提到 "rework_count >= 3 时自动触发预警标记 (写日志)". 实测 `rework_alert_log` 已建空表, 但**字典里没列其字段集与触发器 DDL**.

- `rework_alert_log` 表 schema (字段集)?
- `trg_rework_alert` 触发器是 BEFORE INSERT 还是 AFTER INSERT? 行级还是语句级?
- Carrie 用 batch UPSERT 灌 fact_card 时, 触发器会触发 N 次还是 1 次?
- Phase 1 全 0 默认 rework_count 不会触发, 但 Carrie 需要做 sanity check 确认对象正确

---

### C · 字段语义 / 派生规则 (Terresa 字典层澄清 + 需 Mark 联动确认部分)

#### C1. 一行的粒度 — 一个保单产生多少行 fact_card?

字典开头 "每行 = 一次 L4 活动完整执行实例记录", 但具体粒度未定:
- (a) 1 保单 = 1 个主 L4 → 1 行 fact_card
- (b) 1 保单 = 经过多个 L4 (从佣金录入到批核到外发) → N 行 fact_card

Mark D1 决策 (从 FACT_POLICY 状态机自动映射 C 段) 暗示 (a), 但没说死。请确认字典原始设计意图。

#### C2. FACT_POLICY → l4_code 映射规则

字典 FC-012 说"从 DIM_PROCESS 复制 l4_code", 但 FACT_POLICY(保单) 与 DIM_PROCESS(L4) 的映射规则字典没给:
- 一个保单签约 → l4_code = `L4-COM-???` 是哪一个?
- 销售类 L3 (L3-COM, L3-SOA 等) 下有多少 L4 是 "保单事件" 路径?
- 是否有现成的 `(policy_status, business_category) → l4_code` 映射表?
- 没有的话, 谁来制定这张映射表 (Terresa 还是 Mark)?

#### C3. execution_status 状态机映射表

字典 FC-016 列 4 枚举 (完成/进行中/阻断/逾期). Mark D1 说"按保单阶段自动赋值". 但完整映射表没给 — 请补全:

| FACT_POLICY.policy_status | execution_status 映射 |
|---|---|
| 生效 | ? |
| 取消投保 | ? |
| 退保 | ? |
| 尚欠保费 | ? |
| 已签单 | ? |
| 排期 | ? |
| pending | ? |
| 搁置受保 | ? |
| 待批核 | ? |
| (NULL) | ? |

#### C4. `time_key` 派生口径 (dim_time 灌好后)

字典 FC-006 "按 start_date 自动转换", 但 FC-017 start_date 是手工录入 (❌). Phase 1 批量回填 start_date 缺失时, time_key 用什么 fallback?
- (a) record_date (FC-002 自动取当前日期)
- (b) FACT_POLICY 的某个日期 (sign_date / issue_date / paid_to_date / effective_date)
- (c) NULL? — 但 FC-006 校验说"必须存在于 DIM_TIME", 暗示 NOT NULL

#### C5. 非销售类 L4 的派生源

425 L4 中大部分是非销售类 (合规 / 培训 / 产品准入 / 合作伙伴维护 等). Mark D1 只覆盖了销售类 L4 (从 FACT_POLICY 派生). **非销售类 L4 (~70%, 即 ~300 个) Phase 1 怎么进 fact_card**?
- (a) Phase 1 只 cover 销售类 (~125 个 L4 假设), 非销售类等 AG07 上线 (Week 8+)
- (b) 非销售类 L4 Phase 1 全部 0 行 fact_card (表上看不到)
- (c) 还有其他派生源 (Mark 减负清单 / Mark 裁定记录 / Jasper 处理的合规事件等)?

#### C6. `dim_org` 粒度差异 → org_key 怎么派生?

字典 frontmatter 声明粒度 "岗位级 (同族多岗位多人, 每人一行)", 实测仅 8 行 (岗位族级). Carrie 派生 fact_card.org_key 时:
- 一个保单的 partner_code 怎么映射到具体 org_key?
- 是按"该 L4 所属族" 取 org_key (8 选 1)?
- 还是 Phase 1 全部 NULL 等 GAP-01 完成?

#### C7. dim_kpi 重构后, kpi_key 派生规则

实测发现 dim_kpi 从旧体系 (33 行 `KPI-A-001` 类, 岗位/VS 级, 5-24 备份) 重构为新 (32 行 `KPI_01` 类, 企业级). 字典 V1.0 描述的还是旧体系。
- 新 32 行 KPI 是否已经稳定可用于 fact_card.kpi_key 关联?
- 关联规则: 按 vs_code? 按 strategy_level? 按 l3_code? 还是字典 frontmatter 提到的 "KPI穿透矩阵" 还在制作?
- Mark D1 说 Phase 1 kpi_key 全 NULL — 这跟新 dim_kpi 已存在的 32 行是否仍合理?

#### C8. `sla_hours_actual` 复制时机

字典 FC-020 "从 DIM_PROCESS.sla_hours 自动复制", DIM_PROCESS 有 SCD Type 2 (DP-030~033). 复制时取:
- (a) `is_current = TRUE` 的当前版本
- (b) `valid_from <= record_date < valid_to` 的历史快照

Phase 1 回填 2026 Q1-Q2 历史保单时, 取最新 SLA 还是历史 SLA? 字典提示 "DIM_PROCESS 版本更新时本字段不随之变更 (保留历史标准)" 暗示 (b), 请确认.

---

### D · 字典中规则冲突澄清

#### D1. Cross-field 约束 vs Mark D1 默认值冲突

字典 FC-028 明示: `agentifiability='Auto' 且活动已完成时, agent_assist_flag 理论上须为 TRUE (预警, 不阻断)`. 但 Mark D1 让 G 段全 FALSE 默认.

Phase 1 在 AG07 未上线时, 这些 cross-field 约束怎么处理?
- (a) 字典层临时加注释 "Phase 1 例外, 警告不阻断"
- (b) DB CHECK 不强制, 只在 stderr 警告
- (c) 用 data_source='批量导入' 触发例外分支

类似冲突还有: FC-007 agent_key 与 FC-028 联动, FC-018 end_date 与 FC-016 execution_status 联动 (Phase 1 historical 回填若 execution_status='完成' 则 end_date 必须 NOT NULL — 这在批量回填时怎么处理).

#### D2. `data_source='批量导入'` 时 `entry_by` 规则

字典 FC-035 entry_by 校验只覆盖 3 种 data_source: "手工录入时须 NOT NULL; Agent日志/系统自动时可为 NULL". **'批量导入' 没出现在规则里**.

- data_source='批量导入' 时 entry_by 填什么?
- 建议 (Carrie): `'CARRIE_BATCH_ETL_20260528'` 或类似 (含时间戳便于审计回查)

#### D3. fact_card 是否需要 `source_notes` 字段?

DIM_PROCESS 有 source_notes (DP-034) 用于备注溯源 (含 G3-1 等历史分组), **但 fact_card 没有**. Phase 1 批量灌数时, 想标注"本行从 FACT_POLICY.policy_id=X 派生"的溯源信息:
- (a) 用 entry_by + data_source + batch_id 已经够
- (b) 需要新增 fact_card.source_ref 字段挂 policy_id 等回查锚
- (c) 用 batch_id 关联另一张 ETL_LOG 表

---

### E · 运行决策 (Carrie 提议方案, 待 Terresa/Mark 同意 / 修改)

#### E1. 重跑 / 增量策略

Carrie 提议 (跟 FIN 子项目 `sync_insurance_plan` 一致风格):
- 用 sync_history.batch_id 判重 — 同一 source_file 不重复同步
- 同保单已有 fact_card → UPSERT 而非 INSERT (按某种业务自然键)
- 重跑失败可幂等

可接受? 还是 Phase 1 走简单 `TRUNCATE + INSERT` 即可?

#### E2. 校验失败处置

Carrie 提议 (同 FIN 风格):
- 整批拒 — 任一行违反字典 CHECK 抛 RuntimeError, 整批回滚 (避免脏数据)
- 支持 `--dry-run` 预检 (上线前过一遍校验, 不真写库)
- 失败时输出具体行 + 字段定位

可接受? 还是 Phase 1 走逐行容错 (违反的行跳过, 不阻断整批)?

---

### F · 行数估算 (规划用)

#### F1. Phase 1 fact_card 行数量级

Terresa 作为字典维护者, 设计 fact_card 时心里的 Phase 1 行数量级是?
- (a) ~2,917 (一保单一行, 主 L4 归类)
- (b) ~10,000~15,000 (一保单经过 4~5 个销售类 L4)
- (c) ~10,000 + 非销售类 (待 C5 决策后定)
- (d) 不限制, 等业务跑出来

这数字决定: Q-T5 触发器性能预估 / 索引建议 / 表分区设计 / 全表扫描成本.

---

## 三、问题路由与紧急度

| 组 | 紧急度 | 谁拍 | 期望响应 |
|---|---|---|---|
| **A1** 字典 V2.0 | 中 | Terresa | 5-29 给方向 |
| **B1** dim_time | 🔴 极高 | Terresa (或转给脚本拥有者) | 5-28 晚 / 5-29 早 |
| **B2/B3** | 高 | Terresa | 5-29 |
| **C1/C2/C3/C5** | 高 | Terresa 字典澄清 + **Mark 业务确认** | 5-29 ~ 5-30 |
| **C4/C6/C7/C8** | 中 | Terresa | 5-29 ~ 5-30 |
| **D1/D2/D3** | 中 | Terresa | 5-29 ~ 5-30 |
| **E1/E2** | 中 | Terresa / Mark 默认接受 Carrie 方案即可 | 5-29 ~ 5-30 |
| **F1** | 低 | Terresa 一句话即可 | 5-30 前 |

**核心阻塞: B1 不解锁, fact_card 灌数方案进不到"可执行"状态**. 其余 15 项可并行回复.

---

## 四、Carrie 同步交付

- 待 Terresa 回复以上问题 (尤其 B1) 后, **24h 内交完整 fact_card ETL 方案**
- Carrie 5-28 已校对 process_analytics 实际状态, DB 现状摸清, 不会盲写 SQL
- Carrie 已与 Mark 同步 (`docs/mark协作/致Mark_今日回执_M4-W10_20260528.md` §二), Mark 不必逐一回字典问题, Terresa 整体答复后涉及业务规则部分 Carrie 会转交 Mark 拍板

---

*本文档存档: `docs/mark协作/致Terresa_fact_card字典澄清_M4-W10_20260528.md`*
*关联: 字典 V1.0 + Mark 第二轮决策回复 + P1 字段清单*

