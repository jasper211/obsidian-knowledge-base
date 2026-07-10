---
type: 项目笔记
source: 08_任务与跟进/任务状态
synced: 2026-06-15
tags: [项目]
---

# 致 Carrie · fact_card 字典澄清回函 · M4-W10

> **致**: Carrie / **抄送**: Mark, Jasper  
> **发件人**: Terresa (字典维护者)  
> **日期**: 2026-05-29  
> **回复**: `致Terresa_fact_card字典澄清_M4-W10_20260528.md`

---

## 一、B1 · dim_time 0 行 — 已授权 ✅

**现状**: 目前没有现成的 `dim_time` 生成脚本在仓库里。

**决策**: 
- **授权 Carrie 自行编写并执行生成脚本**，目标范围 `generate_series('2024-01-01', '2027-12-31', '1 day')`，~1461 行。
- 脚本建议放在 `scripts/schema/` 或 `scripts/etl/` 下，命名如 `generate_dim_time.sql`，方便后续复用。
- 执行后请在群里同步一声，我更新字典备注。

**→ 此项已解锁，Carrie 可推进 CP1 验收。**

---

## 二、A1 · 字典 V1.0 与 DB 实际偏差 — 确认出 V2.0

**确认偏差存在**。Carrie 实测的偏差我逐项认可以下修正方向：

| DIM 表 | V1.0 声明 | DB 实测 | V2.0 修正方向 |
|---|---|---|---|
| `dim_process` | 425 L4 | 425 | 不变 ✅ |
| `dim_vs` | VS-1~5 + L1-05 多阶段 | 36 | 不变 ✅（描述可更精确） |
| `dim_org` | 粒度: 岗位级（同族多岗位多人） | **8 行（岗位族级）** | ⚠️ **修正为岗位族级**，frontmatter 描述改"岗位族级" |
| `dim_time` | ~1461 行 | 0 行（待 Carrie 生成） | 不变（生成后一致） |
| `dim_agent` | 361 | 361 | 不变 ✅ |
| `dim_m_strategy` | M0-M8 共 9 行 | 9 | 不变 ✅ |
| `dim_kpi` | "Phase 2 才有，Week 6 录入" | **32 行新体系 + 34 行 backup** | ⚠️ **重写描述**，反映新体系 `KPI_01` 类已上线 |
| `dim_deliverable` | ~253（一 L4 一 deliverable） | **400 行，distinct_l4=400** | ⚠️ **修正行数**，并解释 400 < 425 的原因（见 B2） |

**决策**: **确认出字典 V2.0**，我会在 5-30 前提交初稿，Carrie 配合校对。

---

## 三、B2 · dim_deliverable 缺 25 个 L4

**现状确认**: `dim_process` 425 L4 vs `dim_deliverable` 400 distinct_l4，确实缺 25 个。

**原因**: 这 25 个 L4 属于 **纯流程/管理类活动，不产生独立物理交付物**（例如内部评审节点、系统自动触发步骤、合规检查点等），在 CLAUDE.md 5.0 节原则下不生成独立 deliverable 记录。

**Phase 1 处理方案**:
- **这 25 个 L4 的 `deliverable_key` 留 NULL**，字典 FC-010 已标 NULLABLE，合法。
- 不需要先补足 `dim_deliverable` 再灌 `fact_card`。
- Carrie 可正常推进，无需阻塞。

---

## 三、B3 · rework_alert_log / trg_rework_alert

**补充 schema 如下**:

```sql
-- rework_alert_log
CREATE TABLE rework_alert_log (
    alert_id        SERIAL PRIMARY KEY,
    card_id         INT NOT NULL REFERENCES fact_card(card_id),
    alert_time      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rework_count    INT NOT NULL,
    alert_level     VARCHAR(20) DEFAULT 'WARNING',  -- WARNING / CRITICAL
    resolved        BOOLEAN DEFAULT FALSE
);

-- 触发器
CREATE TRIGGER trg_rework_alert
    AFTER INSERT OR UPDATE ON fact_card
    FOR EACH ROW
    WHEN (NEW.rework_count >= 3)
    EXECUTE FUNCTION fn_rework_alert();
```

**关键要点**:
- **AFTER INSERT OR UPDATE，行级触发器**。
- Carrie 用 batch UPSERT 时，**每行触发 1 次**（行级特性）。
- Phase 1 `rework_count` 全 0，不会触发，不影响灌数性能。
- `fn_rework_alert()` 内部已做幂等（同 card_id 未 resolved 的不重复插入）。

---

## 四、C 组 · 字段语义 / 派生规则

### C1. 一行粒度 — 一个保单产生多少行 fact_card?

**字典原始设计意图**:  **(b) 1 保单 = 经过多个 L4 → N 行 fact_card**。

但 Phase 1 的实际执行粒度，**建议按 Mark 业务决策为准**。字典层保留 N 行设计的表结构，不限制。

**→ 建议 Carrie 将此问题转交 Mark 确认最终业务口径。**

### C2. FACT_POLICY → l4_code 映射规则

**现状**: 字典 FC-012 仅说明"从 DIM_PROCESS 复制"，映射规则确实未定义。

**我的判断**: 这张 `(policy_status, business_category) → l4_code` 映射表 **应由 Mark 提供**，因为涉及业务分类逻辑。字典层只负责映射表定稿后的字段级约束。

**→ 转交 Mark，请 Carrie 在致 Mark 的文档中追加此项。**

### C3. execution_status 状态机映射表

**我的建议映射如下**（供 Mark 确认或修改）：

| FACT_POLICY.policy_status | execution_status |
|---|---|
| 生效 | 完成 |
| 取消投保 | 阻断 |
| 退保 | 阻断 |
| 尚欠保费 | 进行中 |
| 已签单 | 完成 |
| 排期 | 进行中 |
| pending | 进行中 |
| 搁置受保 | 阻断 |
| 待批核 | 进行中 |
| (NULL) | 进行中（默认） |

**→ 建议 Carrie 将此表转 Mark 确认后，我写入字典 V2.0。**

### C4. time_key 派生口径（dim_time 灌好后）

**决策**: 按以下优先级 fallback：
1. `start_date`（如果已有）→ 转 `time_key`
2. `start_date` 缺失 → 取 `record_date`（FC-002 自动生成当前日期）
3. 都不存在 → **不允许**，因为 FC-006 校验要求必须存在于 DIM_TIME，隐含 NOT NULL

**Phase 1 批量回填**: 用 `record_date` 作为 fallback 是安全的，`dim_time` 已包含 2024-2027 全覆盖。

### C5. 非销售类 L4 的派生源 (~300 个)

**决策**:  **(b) Phase 1 非销售类 L4 全部 0 行 fact_card**。

理由: Mark D1 只覆盖了销售类派生规则，非销售类（合规/培训/产品准入/合作伙伴维护等）缺乏明确的源系统映射。AG07 上线（Week 8+）后再补灌。

**Phase 1 只 cover 销售类 L4（~125 个）**。

### C6. dim_org 粒度差异 → org_key 怎么派生?

**修正**: `dim_org` 实际粒度为 **岗位族级（8 行）**，V2.0 会修正描述。

**Phase 1 处理**: `org_key` **全部 NULL**，等 GAP-01 完成后统一补映射。理由：
- 8 个岗位族无法直接映射到保单的 partner_code（粒度太粗）
- 精确映射需要一张 `partner_code → org_key` 对照表，目前不存在

### C7. dim_kpi 重构后，kpi_key 派生规则

**现状**: 新 32 行 `KPI_01` 类体系 **已基本稳定**，可用于关联。

**Phase 1 决策**:  **kpi_key 全 NULL**（保持 Mark D1 原决策）。

理由: KPI 穿透矩阵尚在制作中，按 vs_code / strategy_level / l3_code 的关联规则未最终定稿。Phase 2（Week 6+）再启用 `kpi_key` 关联。

### C8. sla_hours_actual 复制时机

**决策**: **(b) 按 `valid_from <= record_date < valid_to` 取历史快照**。

字典 FC-020 备注"DIM_PROCESS 版本更新时本字段不随之变更（保留历史标准）"已明确此意图。Phase 1 回填 2026 Q1-Q2 历史保单时，取历史 SLA 版本，而非当前最新版。

---

## 五、D 组 · 字典规则冲突

### D1. Cross-field 约束 vs Mark D1 默认值冲突

**决策**: **(a) 字典层临时加注释"Phase 1 例外，警告不阻断"**。

具体处理:
- `agentifiability='Auto'` 且已完成时 `agent_assist_flag` 理论上应为 TRUE → Phase 1 允许 FALSE，字典 V2.0 加 `/* Phase 1 exception */` 注释。
- FC-018 `end_date` 与 FC-016 `execution_status` 联动：历史回填时 `execution_status='完成'` 但 `end_date` 缺失 → **允许 `end_date` 在 Phase 1 为 NULL**，等后续业务系统补录。
- DB CHECK 约束 **不加硬限制**，只在 ETL 日志中输出警告。

### D2. data_source='批量导入' 时 entry_by 规则

**决策**: 接受 Carrie 建议。

`entry_by` 填 `'CARRIE_BATCH_ETL_20260528'` 或类似格式（`{操作者}_{模式}_{YYYYMMDD}`）。

**V2.0 会补充 FC-035 规则**: `"批量导入时 entry_by 填执行者标识，格式建议 {NAME}_BATCH_ETL_YYYYMMDD，用于审计回查。"`

### D3. fact_card 是否需要 source_notes 字段?

**决策**: **(c) 用 batch_id 关联另一张 ETL_LOG 表**。

理由:
- `entry_by + data_source + batch_id` 已能定位批次，但无法精确到单行的源记录（如 policy_id）。
- 不在 `fact_card` 上新增字段（避免事实表膨胀）。
- 建议 Carrie 在 ETL 过程中写一张 `etl_batch_detail` 辅助表，结构如下：

```sql
CREATE TABLE etl_batch_detail (
    batch_id        VARCHAR(50),
    target_table    VARCHAR(50),      -- 'fact_card'
    target_card_id  INT,              -- 灌完后回填
    source_table    VARCHAR(50),      -- 'FACT_POLICY'
    source_key      VARCHAR(100),     -- policy_id=X
    etl_time        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

这样既能溯源，又不污染事实表 schema。

---

## 六、E 组 · 运行决策（同意 Carrie 方案）

### E1. 重跑 / 增量策略

**同意 Carrie 方案**:
- `sync_history.batch_id` 判重，同一 `source_file` 不重复同步。
- 同保单已有 fact_card → **UPSERT**（按业务自然键：`policy_id + l4_code + time_key`）。
- 要求幂等，重跑失败可安全重试。

### E2. 校验失败处置

**同意 Carrie 方案**:
- **整批拒**: 任一行违反字典 CHECK 抛 RuntimeError，整批回滚。
- **支持 `--dry-run`** 预检（上线前过一遍校验，不真写库）。
- 失败时输出具体行 + 字段定位，便于排错。

Phase 1 不走逐行容错，避免脏数据进库。

---

## 七、F1 · Phase 1 行数量级

**我的预期**: **(b) ~10,000~15,000 行**。

测算逻辑:
- 当前 FACT_POLICY 活跃保单约 2,500~3,000 张（估算）。
- 销售类路径平均经过 4~5 个 L4（录入 → 初审 → 批核 → 外发 → 生效等）。
- 3,000 × 4 = ~12,000 行，落在 10K~15K 区间。

非销售类 L4 在 Phase 1 为 0 行（见 C5）。

---

## 八、问题路由总结

| 组 | 状态 | 备注 |
|---|---|---|
| **B1** | ✅ **已解锁** | Carrie 自行生成 dim_time |
| A1 | ✅ 确认出 V2.0 | Terresa 5-30 提交初稿 |
| B2 | ✅ 已答复 | 25 个 L4 deliverable_key 留 NULL |
| B3 | ✅ 已答复 | schema + 触发器 DDL 已提供 |
| C1/C2/C3/C5 | ⏳ **转 Mark** | Carrie 请同步给 Mark 确认 |
| C4/C6/C7/C8 | ✅ 已答复 | 见上 |
| D1/D2/D3 | ✅ 已答复 | V2.0 同步更新 |
| E1/E2 | ✅ 同意方案 | 按 Carrie 提议执行 |
| F1 | ✅ 已答复 | 预期 10K~15K 行 |

---

## 九、下一步行动

1. **Carrie**: 
   - 立即执行 B1（dim_time 生成脚本）。
   - 将 C1/C2/C3/C5 转交 Mark 确认（可引用本文档第三节）。
   - 确认 ETL_LOG 辅助表（D3）是否接受，如接受可纳入 ETL 方案。

2. **Terresa (我)**:
   - 5-30 前提交字典 V2.0 初稿，反映 A1/B3/C4/C6/C7/D1/D2 的修正。

3. **Mark**:
   - 确认 C1/C2/C3/C5 业务规则（建议 5-30 前回复）。

---

*本文档存档: `docs/mark协作/Terresa_回函_fact_card字典澄清_M4-W10_20260529.md`*
