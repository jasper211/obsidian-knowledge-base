---
type: 项目笔记
source: 08_任务与跟进/任务状态
synced: 2026-06-15
tags: [项目]
---

# 致 Carrie · fact_card 字典澄清回函 · M4-W10（修正版）

> **致**: Carrie / **抄送**: Mark, Jasper  
> **发件人**: Terresa (字典维护者)  
> **日期**: 2026-05-29  
> **回复**: `致Terresa_fact_card字典澄清_M4-W10_20260528.md`  
> **依据**: `DICT_流程数据库数据字典_V1_项目交付.md` (V1.0, 2026-04-22) + `create_process_schema.sql` + `seed_dim_org.sql` + `dim_deliverable_字典匹配结果.csv` + `dim_kpi_insert_enterprise.sql`

---

## 一、B1 · dim_time 0 行 — 已授权 ✅

**依据**: `create_process_schema.sql` 第 15-27 行仅定义表结构，无 INSERT 脚本。

**决策**:
- **确认没有现成的 dim_time 生成脚本**，仓库 `schema/` 和 `scripts/` 目录下均未发现。
- **授权 Carrie 自行编写并执行生成脚本**，目标范围 `generate_series('2024-01-01', '2027-12-31', '1 day')`，~1461 行。
- 脚本建议放在 `scripts/schema/` 下，命名如 `generate_dim_time.sql`。
- 执行后请在群里同步，我更新字典备注。

**→ 此项已解锁，Carrie 可推进 CP1 验收。**

---

## 二、A1 · 字典 V1.0 与 DB 实际偏差 — 确认出 V2.0

**基于真实文件逐项确认偏差存在**:

| DIM 表 | V1.0 声明 | 真实文件证据 | V2.0 修正方向 |
|---|---|---|---|
| `dim_process` | 425 L4 | `DIM_PROCESS_import_L3流程库_01.sql` 插入 139 行，Carrie 实测 425，存在后续导入 | 待查后续导入记录，补充来源说明 |
| `dim_vs` | VS-1~5 + L1-05 多阶段 | `seed_dim_vs_v1.sql` 插入 60 行（VS-1:8, VS-2:22, VS-3:12, VS-4:6, VS-5:12），Carrie 实测 36 | ⚠️ **待与 Carrie 确认 36 的统计口径**（是否仅计有效覆盖阶段？） |
| `dim_org` | 粒度: 岗位级（同族多岗位多人） | `seed_dim_org.sql` 实际仅 **8 行**；注释写"C族是复合族，用一个记录代表整体" | ⚠️ **修正为岗位族级**，frontmatter 描述改"岗位族级（8 行）" |
| `dim_time` | ~1461 行 | `create_process_schema.sql` 无 INSERT 脚本 | 确认由 Carrie 生成后一致 |
| `dim_agent` | 361 | 未找到导入脚本，以 Carrie 实测为准 | 待补充脚本来源 |
| `dim_m_strategy` | M0-M8 共 9 行 | `create_process_schema.sql` 第 497-508 行已初始化 9 行 | ✅ 一致 |
| `dim_kpi` | "Phase 2 才有，Week 6 录入" | `dim_kpi_insert_enterprise.sql`（5-24）已删旧岗位 KPI，插入 **32 企业 KPI**（KPI_01~KPI_51）；`已完成_dim_kpi_w8c_alter_update.sql` 已补 l1_code/l3_codes/formula 字段 | ⚠️ **严重落后，V2.0 重写描述** |
| `dim_deliverable` | ~253（一 L4 一 deliverable） | `create_process_schema.sql` 注释写"253条"；`dim_deliverable_字典匹配结果.csv` 实际 **400 行**；Carrie 实测 distinct_l4=400 | ⚠️ **修正行数为 400，并解释 400 < 425 的原因** |

**决策**: **确认出字典 V2.0**，我会在 5-30 前提交初稿，Carrie 配合校对。

---

## 三、B2 · dim_deliverable 缺 25 个 L4

**依据**: `dim_deliverable_字典匹配结果.csv` 有 400 行数据；Carrie 实测 `dim_process` 425 L4 vs `dim_deliverable` 400，缺 25 个。

**答复**:

当前 L3/L4 定义仍在演进中（M2 裁定持续迭代），`dim_process` 425 L4 中部分新增/合并/重构的 L4 尚未同步到 `dim_deliverable`。**缺失 25 个 L4 的交付物记录是正常过渡状态**。

**Phase 1 处理方案**:
- **这 25 个 L4 的 `deliverable_key` 留 NULL**，字典 FC-010 已标 NULLABLE，合法。
- **不需要先补足 `dim_deliverable` 再灌 `fact_card`**。
- 等 L3/L4 定义稳定后（M2 裁定完成），再统一补录 `dim_deliverable`。

以上表述已同步写入字典 **V2.0 §九、DIM_DELIVERABLE**。

**→ Carrie 可正常推进，此项不阻塞 Phase 1。**

---

## 四、B3 · rework_alert_log / trg_rework_alert — 已确认 ✅

**依据**: `create_process_schema.sql` 第 448-469 行。

**真实 schema 如下**（直接从 DDL 复制）：

```sql
CREATE TABLE IF NOT EXISTS process_analytics.rework_alert_log (
    alert_id    SERIAL PRIMARY KEY,
    fact_id     UUID NOT NULL,
    l4_code     VARCHAR(20),
    rework_count SMALLINT,
    alerted_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION process_analytics.trg_rework_alert()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.rework_count >= 3 THEN
        INSERT INTO process_analytics.rework_alert_log (fact_id, l4_code, rework_count)
        VALUES (NEW.fact_id, NEW.l4_code, NEW.rework_count);
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_rework_alert
    AFTER INSERT OR UPDATE ON process_analytics.FACT_CARD
    FOR EACH ROW EXECUTE FUNCTION process_analytics.trg_rework_alert();
```

**关键要点**:
- **AFTER INSERT OR UPDATE，行级触发器**。
- Carrie 用 batch UPSERT 时，**每行触发 1 次**（行级特性）。
- 注意：`trg_rework_alert` 函数内部**没有做幂等**（同 fact_id 重复触发会插入多行）。但 Phase 1 `rework_count` 全 0，不会触发，不影响灌数。
- 如果后续需要幂等，建议在 `rework_alert_log` 上加 `UNIQUE(fact_id)` 或函数内加 `WHERE NOT EXISTS`。

---

## 五、C 组 · 字段语义 / 派生规则 — 转 Mark 确认

以下问题**数据字典 V1.0 和现有脚本中均未给出现成答案**，涉及业务规则层，**需 Mark 确认**。我作为字典维护者只能澄清字段级约束，无法定业务映射。

### C1. 一行粒度 — 一个保单产生多少行 fact_card?

**字典原始设计意图**: 字典 frontmatter 写"每行 = 一次 L4 活动的完整执行实例记录"，这是技术层面的表结构设计，**不限制**一保单对应多少行。

**→ 转 Mark 确认业务口径**：(a) 一保单一行 还是 (b) 一保单多行（经过多个 L4）。

### C2. FACT_POLICY → l4_code 映射规则

**现状**: 字典 FC-012 仅说明"从 DIM_PROCESS 复制"，`(policy_status, business_category) → l4_code` 的映射表**不存在于现有文件中**。

**→ 转 Mark**：请 Mark 提供或确认这张映射表。字典层只负责映射表定稿后的字段级约束。

### C3. execution_status 状态机映射表

**现状**: 字典 FC-016 列了 4 个枚举值（完成/进行中/阻断/逾期），但 `FACT_POLICY.policy_status → execution_status` 的完整映射表**不存在于现有文件中**。

**→ 转 Mark 确认**。以下是我个人的**临时建议**（供 Mark 修改/确认）：

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

**注意**：以上映射未经 Mark 确认，**仅供参考**，正式映射以 Mark 回复为准。

### C4. time_key 派生口径（dim_time 灌好后）

**依据**: 字典 FC-006 "按 start_date 自动转换"；FC-002 `record_date` 自动取当前日期。

**决策**: 按以下优先级 fallback（字典层可定，因为只涉及字段间派生逻辑）：
1. `start_date`（如果已有）→ 转 `time_key`
2. `start_date` 缺失 → 取 `record_date`（FC-002 自动生成当前日期）
3. 都不存在 → **不允许**，因为 FC-006 校验要求必须存在于 DIM_TIME，隐含 NOT NULL

**Phase 1 批量回填**: `record_date` 作为 fallback 是安全的（dim_time 覆盖 2024-2027）。

### C5. 非销售类 L4 的派生源 (~300 个)

**现状**: Mark D1 只覆盖了销售类派生规则，非销售类（合规/培训/产品准入/合作伙伴维护等）的派生源**在现有文件中未定义**。

**→ 转 Mark 确认**：Phase 1 是 (a) 只 cover 销售类、(b) 非销售类全 0 行、还是 (c) 有其他派生源？

### C6. dim_org 粒度差异 → org_key 怎么派生?

**依据**: `seed_dim_org.sql` 实际仅 8 行（岗位族级），字典 V1.0 frontmatter 声明"岗位级"。

**决策**: `org_key` **Phase 1 全部 NULL**，等 GAP-01 完成后统一补映射。理由：
- 8 个岗位族无法直接映射到保单的 partner_code（粒度太粗）
- 精确映射需要 `partner_code → org_key` 对照表，目前不存在

### C7. dim_kpi 重构后，kpi_key 派生规则

**依据**: `dim_kpi_insert_enterprise.sql` 已插入 32 企业 KPI（KPI_01~KPI_51），`已完成_dim_kpi_w8c_alter_update.sql` 已补 l1_code / l3_codes / formula 字段。

**现状**: 新 32 行 KPI 体系 **已基本稳定**（5-24 已上线，5-23 Mark 已 verify 公式口径）。

**Phase 1 决策**: **kpi_key 全 NULL**（保持 Mark D1 原决策）。理由: KPI 穿透矩阵尚在制作中，`fact_card.kpi_key` 的关联规则（按 vs_code? 按 l3_code? 按 strategy_level?）未最终定稿。Phase 2（Week 6+）再启用。

### C8. sla_hours_actual 复制时机

**依据**: 字典 FC-020 备注"DIM_PROCESS 版本更新时本字段不随之变更（保留历史标准）"。

**决策**: **按 `valid_from <= record_date < valid_to` 取历史快照**。Phase 1 回填 2026 Q1-Q2 历史保单时，取历史 SLA 版本，而非当前最新版。

---

## 六、D 组 · 字典规则冲突

### D1. Cross-field 约束 vs Mark D1 默认值冲突

**依据**: 字典 FC-028 + Mark D1 决策。

**决策**: **Phase 1 例外处理，字典层加注释，DB CHECK 不强制**。

具体处理:
- `agentifiability='Auto'` 且已完成时 `agent_assist_flag` 理论上应为 TRUE → Phase 1 允许 FALSE，字典 V2.0 加 `/* Phase 1 exception: AG07 未上线 */` 注释。
- FC-018 `end_date` 与 FC-016 `execution_status` 联动：历史回填时 `execution_status='完成'` 但 `end_date` 缺失 → **允许 `end_date` 在 Phase 1 为 NULL**，等后续业务系统补录。
- DB CHECK 约束 **不加硬限制**（保持现有 `chk_fc_complete_has_end` 不变，但批量导入时由 Carrie 的 ETL 做例外标记）。

### D2. data_source='批量导入' 时 entry_by 规则

**依据**: 字典 FC-035 只覆盖 3 种 data_source，未提及"批量导入"。

**决策**: 接受 Carrie 建议。

`entry_by` 填 `'CARRIE_BATCH_ETL_20260528'` 或类似格式（`{操作者}_{模式}_{YYYYMMDD}`）。

**V2.0 补充 FC-035 规则**: `"批量导入时 entry_by 填执行者标识，格式建议 {NAME}_BATCH_ETL_YYYYMMDD，用于审计回查。"`

### D3. fact_card 是否需要 source_notes 字段?

**依据**: DIM_PROCESS 有 `source_notes` (DP-034)，fact_card 当前无对应字段。

**决策**: **Phase 1 不新增字段**。理由：
- `entry_by + data_source + batch_id` 已能定位批次。
- 精确到单行的溯源（如 policy_id）可通过 Carrie ETL 的 `batch_id` 关联外部日志实现，不需要改事实表 schema。
- 如果后续有强需求，V2.0 再考虑加 `source_ref` 字段。

**→ 接受 Carrie 方案 (a)，不新增字段。**

---

## 七、E 组 · 运行决策（同意 Carrie 方案）

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

## 八、F1 · Phase 1 行数量级

**依据**: 无文件支撑，我作为字典维护者**没有明确的行数预期**。

**决策**: **(d) 不限制，等业务实际跑出来**。

原因：
- 当前 FACT_POLICY 基数我不掌握（没有权限/文件看到实际保单量）。
- C1（一保单一行还是多行）和 C5（非销售类 L4 是否进 fact_card）未定，行数无法估算。
- 建议 Carrie 按实际 FACT_POLICY 数据量 + Mark 确认后的映射规则，跑 `--dry-run` 后自然得出。

---

## 九、问题路由与状态总结

| 组 | 状态 | 依据 | 备注 |
|---|---|---|---|
| **B1** | ✅ **已解锁** | `create_process_schema.sql` 无 dim_time INSERT | Carrie 自行生成脚本 |
| **A1** | ✅ 确认出 V2.0 | 多项文件证据确认偏差 | Terresa 5-30 提交初稿 |
| **B2** | ⏳ **待 Carrie 补 SQL list** | `dim_deliverable_字典匹配结果.csv` 400 行 | 等 25 个缺失 L4 list |
| **B3** | ✅ 已答复 | `create_process_schema.sql` 第 448-469 行 | DDL 已提供 |
| **C1/C2/C3/C5** | ⏳ **转 Mark** | 现有文件中无业务映射规则 | Carrie 请同步给 Mark |
| **C4/C6/C7/C8** | ✅ 已答复 | 基于字典规则 + 文件证据 | 见第五节 |
| **D1/D2/D3** | ✅ 已答复 | 基于字典文本 | V2.0 同步更新 |
| **E1/E2** | ✅ 同意方案 | Carrie 提议 | 按提议执行 |
| **F1** | ✅ 已答复 | 无文件支撑，诚实说没预期 | 不限制，等实际跑出来 |

---

## 十、下一步行动

1. **Carrie**:
   - 立即执行 B1（dim_time 生成脚本）。
   - 执行 B2 SQL，把缺失的 25 个 `l4_code` list 贴给我（预计 10 分钟）。
   - 将 C1/C2/C3/C5 转交 Mark 确认（可引用本文档第五节）。

2. **Terresa (我)**:
   - 收到 B2 list 后，2h 内确认补录或留 NULL。
   - 5-30 前提交字典 V2.0 初稿，反映 A1/B3/C4/C6/C7/D1/D2 的修正。

3. **Mark**:
   - 确认 C1/C2/C3/C5 业务规则（建议 5-30 前回复）。

---

*本文档存档: `docs/mark协作/Terresa_回函_fact_card字典澄清_M4-W10_20260529_修正版.md`*
*依据文件: DICT_流程数据库数据字典_V1_项目交付.md + create_process_schema.sql + seed_dim_org.sql + dim_deliverable_字典匹配结果.csv + dim_kpi_insert_enterprise.sql + 已完成_dim_kpi_w8c_alter_update.sql*
