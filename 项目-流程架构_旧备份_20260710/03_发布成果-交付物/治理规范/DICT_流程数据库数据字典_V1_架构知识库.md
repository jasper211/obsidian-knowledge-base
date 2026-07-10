---
type: 项目笔记
source: 03_发布成果-交付物/治理规范
synced: 2026-06-15
tags: [项目]
---

# 流程数据库数据字典 V1.0

> 文档类型: 数据字典
> 版本: V1.0 (2026-04-22)
> 所属: 流程数据库星型模型 · process_analytics schema
> 负责人: Terresa（维护）/ Carrie（技术实施）
> 数据标准依据: VS-CSV列结构规范_V1.md · L3-definition-schema.yaml · L4-Agent化评估框架.md
> 校验工具: validate_kb.py（知识库侧）/ PostgreSQL CHECK约束（数据库侧）

---

## 阅读说明

| 列 | 说明 |
|----|------|
| **字段ID** | 格式 `<表前缀>-<三位序号>`，全库唯一。前缀：FC=事实表，DP=流程维度，DV=价值流维度，DO=组织维度，DT=时间维度，DA=Agent维度，DS=战略维度，DK=KPI维度，DD=交付物维度 |
| **数据标准** | 数据类型、长度、是否必填、默认值 |
| **校验规则** | 数据库层 CHECK 约束或应用层校验逻辑，格式：`规则描述 → 违反处理` |
| **取值来源** | 具体到文件名/列名，标注可用状态：✅已有数据 / ⚠️部分有数据 / ❌需新建采集 |

---

## 一、FACT_CARD — 流程运行事实表

> 每行 = 一次 L4 活动的完整执行实例记录
> schema: `process_analytics.FACT_CARD`

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| FC-001 | fact_id | 事实记录唯一标识符，全表主键 | 系统自动生成 ✅ | UUID, NOT NULL, PRIMARY KEY | 必须全局唯一；`gen_random_uuid()` 自动生成，不允许手工填写 |
| FC-002 | record_date | 本条记录的登记日期（非活动执行日期） | 手工录入时系统取当前日期 ✅ | DATE, NOT NULL | 不能早于 2026-01-01；不能晚于当前日期 + 1天（防误填未来日期） |
| FC-003 | process_key | 关联 DIM_PROCESS 的代理键 | 按 l4_code 查询 DIM_PROCESS 自动回填 ✅ | INT, FK → DIM_PROCESS(process_key) | 必须存在于 DIM_PROCESS；仅取 is_current=TRUE 的记录 |
| FC-004 | vs_key | 关联 DIM_VS 的代理键 | 按 vs_code + stage_code 查询 DIM_VS 自动回填 ✅ | INT, FK → DIM_VS(vs_key) | 必须存在于 DIM_VS；vs_code 须与 FC-013 一致 |
| FC-005 | org_key | 关联 DIM_ORG 的代理键 | 按 position_family + executor_id 查询 DIM_ORG ⚠️ | INT, FK → DIM_ORG(org_key), NULLABLE | 若 GAP-01 未完成，允许为 NULL；人员映射完成后补填 |
| FC-006 | time_key | 关联 DIM_TIME 的时间键（YYYYMMDD整数） | 按 start_date 自动转换 ✅ | INT, FK → DIM_TIME(time_key) | 格式必须为 YYYYMMDD；必须存在于 DIM_TIME |
| FC-007 | agent_key | 关联 DIM_AGENT 的代理键 | 按 agent_code 查询 DIM_AGENT ⚠️ | INT, FK → DIM_AGENT(agent_key), NULLABLE | 当 agentifiability='Human' 时须为 NULL；当 agent_assist_flag=TRUE 时须 NOT NULL |
| FC-008 | strategy_key | 关联 DIM_M_STRATEGY 的代理键 | 按 l3_code 关联 M0-M8 映射表查询 DIM_M_STRATEGY ✅ | INT, FK → DIM_M_STRATEGY(strategy_key), NULLABLE | 必须存在于 DIM_M_STRATEGY；取值 M0~M8 |
| FC-009 | kpi_key | 关联 DIM_KPI 的代理键 | KPI穿透矩阵完成后（Week 6）自动关联 ❌ | INT, FK → DIM_KPI(kpi_key), NULLABLE | 允许为 NULL（Phase 1/2），DIM_KPI 建立后逐步填入 |
| FC-010 | deliverable_key | 关联 DIM_DELIVERABLE 的代理键 | 按 l4_code 查询 DIM_DELIVERABLE 自动回填 ✅ | INT, FK → DIM_DELIVERABLE(deliverable_key), NULLABLE | 必须存在于 DIM_DELIVERABLE；一个 l4_code 对应唯一一条交付物 |
| FC-011 | l3_code | 流程 L3 编码（冗余字段，用于无 JOIN 聚合） | 从 DIM_PROCESS 复制 ✅ | VARCHAR(20), NOT NULL | 格式：`^L3-[A-Z]{2,6}$`；必须存在于 DIM_PROCESS.l3_code |
| FC-012 | l4_code | 活动 L4 编码（冗余字段） | 从 DIM_PROCESS 复制 ✅ | VARCHAR(20), NOT NULL | 格式：`^L4-[A-Z]{2,6}-\d{2}[a-z]?$`；必须存在于 DIM_PROCESS.l4_code |
| FC-013 | vs_code | 价值流编码（冗余字段） | 从 DIM_VS 复制 ✅ | VARCHAR(10), NOT NULL | 枚举值：VS-1 / VS-2 / VS-3 / VS-4 / VS-5 / L1-05 |
| FC-014 | position_family | 岗位族编码（冗余字段） | 从 DIM_ORG 复制 ⚠️ | VARCHAR(5), NULLABLE | 枚举值：A / B / C / D / E / F / G / 职能；GAP-01未完成前允许为NULL |
| FC-015 | agentifiability | 该 L4 的 Agent 化级别（冗余字段） | 从 DIM_PROCESS 复制 ✅ | VARCHAR(10), NOT NULL | 枚举值：Auto / Aug / Hybrid / Human |
| FC-016 | execution_status | 本次 L4 活动的执行状态 | 手工录入（每次流程完成后由执行人填写） ❌ | VARCHAR(20), NOT NULL（手工录入时） | 枚举值：完成 / 进行中 / 阻断 / 逾期；end_date 有值时 execution_status 不能为"进行中" |
| FC-017 | start_date | 本次 L4 活动实际开始日期 | 手工录入 ❌ | DATE, NULLABLE | 不能晚于 end_date；不能早于 2026-01-01 |
| FC-018 | end_date | 本次 L4 活动实际完成日期 | 手工录入 ❌ | DATE, NULLABLE | 不能早于 start_date；execution_status='完成' 时 NOT NULL |
| FC-019 | duration_hours | 本次 L4 活动实际耗时（小时） | 手工录入，精确到 0.5 小时 ❌ | FLOAT, NULLABLE, CHECK > 0 | 必须 > 0；建议上限 2000 小时（超出需人工确认）；与 start_date/end_date 的自然时差相差不超过 50%（净工时 vs 日历时差） |
| FC-020 | sla_hours_actual | 记录写入时从 DIM_PROCESS 复制的 SLA 标准时限（冗余，防历史失真） | 从 DIM_PROCESS.sla_hours 自动复制 ⚠️ | FLOAT, NULLABLE | 与 DIM_PROCESS.sla_hours 一致；DIM_PROCESS 版本更新时本字段不随之变更（保留历史标准） |
| FC-021 | sla_breach_flag | 是否违反 SLA（自动计算字段） | GENERATED ALWAYS AS (duration_hours > sla_hours_actual) STORED ✅ | BOOLEAN, GENERATED | 不允许手工修改；duration_hours 或 sla_hours_actual 任一为 NULL 时结果为 NULL（不判断） |
| FC-022 | rework_count | 本次 L4 活动因质量问题被退回重做的次数 | 手工录入 ❌ | SMALLINT, DEFAULT 0, CHECK >= 0 | 必须 >= 0；rework_count >= 3 时系统自动触发预警标记（不阻断写入，但写日志） |
| FC-023 | handoff_count | 本次 L4 活动在不同岗位/人员之间的交接次数（反映协同复杂度） | 手工录入或任务系统自动推导 ⚠️ | SMALLINT, DEFAULT 0, CHECK >= 0 | 必须 >= 0；参考值：同岗位内流转不计入，跨岗位族流转 +1 |
| FC-024 | error_flag | 本次 L4 活动是否出现质量问题（输出被退回或发现错误） | 手工录入 ❌ | BOOLEAN, DEFAULT FALSE | error_flag=TRUE 时，error_description 须 NOT NULL |
| FC-025 | error_description | 质量问题描述（error_flag=TRUE 时必填） | 手工录入 ❌ | TEXT, NULLABLE | error_flag=FALSE 时须为 NULL 或空字符串；最大 500 字符 |
| FC-026 | escalation_flag | 本次 L4 活动是否升级至 Mark 裁定 | 从 Mark 裁定记录提取或手工录入 ⚠️ | BOOLEAN, DEFAULT FALSE | escalation_flag=TRUE 时，escalation_reason 须 NOT NULL；Mark 减负清单中的 11 条保留项，理论上 escalation_flag 率应接近 100% |
| FC-027 | escalation_reason | 升级 Mark 裁定的原因描述 | 手工录入 ❌ | TEXT, NULLABLE | escalation_flag=FALSE 时须为 NULL |
| FC-028 | agent_assist_flag | 本次 L4 活动是否有 Agent 介入辅助 | mga-data-platform/agents/ 运行日志自动写入（Week 8+）❌→✅ | BOOLEAN, DEFAULT FALSE | agentifiability='Human' 时 agent_assist_flag 须为 FALSE；agentifiability='Auto' 且活动已完成时，agent_assist_flag 理论上须为 TRUE（预警，不阻断） |
| FC-029 | agent_assist_hours | Agent 在本次活动中实际介入时长（小时） | Agent 运行日志自动解析 ❌ | FLOAT, NULLABLE, CHECK >= 0 | agent_assist_flag=FALSE 时须为 NULL；agent_assist_hours 不能超过 duration_hours |
| FC-030 | agent_save_hours | Agent 节省的人工时估算（= sla_hours_actual - duration_hours，仅当 agent_assist_flag=TRUE 时有意义） | 系统计算字段 ❌ | FLOAT, NULLABLE | agent_assist_flag=FALSE 时须为 NULL；可为负值（Agent 介入反而增加时间，需人工审核） |
| FC-031 | human_override_flag | 人工是否覆盖/推翻了 Agent 的输出决策 | Agent 运行日志自动解析 ❌ | BOOLEAN, DEFAULT FALSE | agent_assist_flag=FALSE 时须为 FALSE；human_override_flag=TRUE 时系统记录日志供 Agent 质量分析 |
| FC-032 | ape_contribution | 本次 L4 活动对 APE（年化保费当量）的贡献量（元） | 从 FACT_POLICY/Agg4 通过 l3_code 关联查询（Week 9+）✅→自动 | FLOAT, NULLABLE | 允许为 NULL（大多数非销售类 L4）；允许为 0；不能为负值（负值用 rework 字段体现）；仅佣金/销售类 L3 有意义 |
| FC-033 | efficiency_score | 人效综合得分（0-100），基于任务 3.4-B 定义的公式计算 | 系统计算（Week 8 公式确认后启用）❌ | FLOAT, NULLABLE, CHECK BETWEEN 0 AND 100 | 公式暂定：SLA达标50分 + 返工率25分 + Agent使用率25分；Week 8 前为 NULL；公式变更后历史数据不追溯 |
| FC-034 | data_source | 本条记录的数据来源渠道 | 录入系统自动标记 ✅ | VARCHAR(20), NOT NULL, DEFAULT '手工录入' | 枚举值：手工录入 / Agent日志 / 系统自动 / 批量导入；不允许为空 |
| FC-035 | entry_by | 录入人的工号或系统账号 | 录入系统自动获取登录用户 ✅ | VARCHAR(50), NULLABLE | 手工录入时须 NOT NULL；Agent日志/系统自动时可为 NULL（记录为系统账号） |
| FC-036 | created_at | 记录创建时间戳 | 系统自动生成 ✅ | TIMESTAMP, NOT NULL, DEFAULT NOW() | 不允许手工修改；写入后不可更新 |
| FC-037 | updated_at | 记录最后更新时间戳 | 系统自动维护 ✅ | TIMESTAMP, NOT NULL, DEFAULT NOW() | 每次 UPDATE 时自动更新；须配置触发器维护 |

---

## 二、DIM_PROCESS — 流程维度表

> 覆盖 L1→L2→L3→L4→L5 完整层级，含 Agent 化6维评分
> 数据来源主文件：`00_治理与元模型/L4-Agent化清单.csv` + `00_治理与元模型/L4-Agent化严谨评分.csv`
> SCD Type 2：L4 定义随里程碑迭代，保留历史版本

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DP-001 | process_key | 维度表代理主键 | 系统自动生成 SERIAL ✅ | SERIAL, PRIMARY KEY | 自增，不允许手工设置 |
| DP-002 | l1_code | L1 飞轮节点编码 | 手工对照 CLAUDE.md L1-01~05 定义补入 ✅ | VARCHAR(10), NOT NULL | 枚举值：L1-01 / L1-02 / L1-03 / L1-04 / L1-05；L1-05 专指权益中台横切能力层 |
| DP-003 | l1_name | L1 飞轮节点名称 | CLAUDE.md 定义 ✅ | VARCHAR(50) | 对应 DP-002 枚举，如 L1-01=保司资源管理；更新 DP-002 时同步更新 |
| DP-004 | l2_code | L2 业务能力编码 | L3 协同框架中的业务能力归属 ⚠️ | VARCHAR(10), NULLABLE | 格式参考业务能力地图；当前业务能力地图岗位列空率100%（GAP-11），允许为 NULL |
| DP-005 | l2_name | L2 业务能力名称 | 业务能力地图（`A3_价值链与能力地图/`）⚠️ | VARCHAR(80), NULLABLE | 与 DP-004 联动；DP-004 有值时 DP-005 须 NOT NULL |
| DP-006 | l3_code | L3 流程编码（知识库 SSOT 主键） | `L4-Agent化清单.csv` 第1列 ✅ | VARCHAR(20), NOT NULL | 格式：`^L3-[A-Z]{2,6}$`；必须存在于 L3 注册表 CSV；不带序号后缀（如 -01/-02）|
| DP-007 | l3_name | L3 流程名称 | L3 注册表 CSV / 协同框架文件名 ✅ | VARCHAR(100), NOT NULL | 与 DP-006 一一对应；更新 DP-006 时须同步更新 |
| DP-008 | l3_domain | L3 所属业务域 | L3-definition-schema.yaml 的 enum 值 ✅ | VARCHAR(20), NOT NULL | 枚举值：KA / 权益 / 经代 / 代理人 / 佣金 / MGA / 设计细分 / 经代联合 / 跨域 |
| DP-009 | l3_status | L3 流程生命周期状态 | L3 注册表 CSV 状态列 ✅ | VARCHAR(10), NOT NULL, DEFAULT 'active' | 枚举值：active / draft / retired / merged；status='retired' 或 'merged' 时，该 L3 下所有 L4 的 is_current 须设为 FALSE |
| DP-010 | l3_trigger | L3 流程触发事件（外部触发条件） | L3 协同框架.txt 第1节提取 ⚠️ | TEXT, NULLABLE | 文本内容不能是内部部门触发（违反外部性检验规则）；触发者必须是 VS-*.csv 中的合法外部利益相关者 |
| DP-011 | l3_exit_condition | L3 流程退出条件（可视化完成标志） | L3 协同框架.txt 第1节提取 ⚠️ | TEXT, NULLABLE | 须描述具体的物理完成标志（如"签署合同"而非"完成工作"）；与对应 DIM_VS.stage_exit_condition 保持语义一致 |
| DP-012 | l4_code | L4 活动编码 | `L4-Agent化清单.csv` 第2列 ✅ | VARCHAR(20), NOT NULL | 格式：`^L4-[A-Z]{2,6}-\d{2}[a-z]?$`（如 L4-COM-03 / L4-BME-05a）；在 l3_code 范围内唯一；拆分活动用小写字母后缀（05a/05b/05c）|
| DP-013 | l4_name | L4 活动名称 | `L4-Agent化清单.csv` 第3列 ✅ | VARCHAR(100), NOT NULL | 须为动宾结构（如"佣金整合与外发"）；不能与同一 L3 下其他 L4 名称重复 |
| DP-014 | l4_deliverable | L4 物理交付物全名（唯一物理价值交付物原则） | `L4-Agent化清单.csv` 第4列 ✅ | TEXT, NOT NULL | 每个 L4 有且仅有一个物理交付物（L4唯一物理交付物原则，CLAUDE.md 5.0节）；禁止填写"完成某动作"或"状态变化"类描述；须可被他人接收/审计/引用 |
| DP-015 | l4_deliverable_type | 物理交付物类型分类 | 按 l4_deliverable 内容归类 ✅（导入时自动分类脚本）| VARCHAR(30), NULLABLE | 枚举值：报告 / 合同 / 凭证 / 数据表 / 决议 / 方案 / 系统记录 / 签字文件；分类逻辑：含《》且为分析结论→报告，含合同/协议→合同，含外发/申报/凭证→凭证，含清单/配置→数据表，含决议/裁定→决议 |
| DP-016 | l4_accountable_role | L4 活动的唯一 A 责任人岗位名称 | `L4_Auto_JD_Mapping_V1.csv` （GAP-01，Week 2产出）❌ | VARCHAR(80), NULLABLE | 每个 L4 只能有一个 A 责任人（RACI 原则）；Mark 保留的 11 条活动，accountable_role 须填写 'Mark（CEO）'；GAP-01 完成前允许为 NULL |
| DP-017 | l4_accountable_family | A 责任人所属岗位族 | `L4_Auto_JD_Mapping_V1.csv` ❌ | VARCHAR(5), NULLABLE | 枚举值：A / B / C / D / E / F / G / 职能 / Mark；与 DP-016 联动，须一致 |
| DP-018 | l5_step | L5 步骤描述（可选，L4 内部操作序列） | L5活动汇总CSV（`04_项目工作区/*/L5活动汇总_02.csv`）⚠️ | VARCHAR(200), NULLABLE | 允许为 NULL（空率 36.7%，GAP-12）；格式建议：步骤序号+动词，如"1. 接收佣金政策文件" |
| DP-019 | agentifiability | L4 活动的 Agent 化分级 | `L4-Agent化清单.csv` 第5列（Tier）✅ | VARCHAR(10), NOT NULL | 枚举值：Auto / Aug / Hybrid / Human；与 `L4-Agent化严谨评分.csv` 的"推导Tier"列一致性须达 100%（当前 253/253 已验证）|
| DP-020 | agent_human_touchpoint | 人工介入点描述（agentifiability≠Auto 时的人工职责说明） | `L4-Agent化清单.csv` 第7列"人介入点" ✅ | TEXT, NULLABLE | agentifiability='Auto' 时须为 NULL 或填写"异常才介入"；agentifiability='Human' 时须 NOT NULL |
| DP-021 | agent_d1_input_struct | Agent 化评估维度D1：输入结构化程度（0-3分） | `L4-Agent化严谨评分.csv` 列 D1 输入结构化 ✅ | SMALLINT, NULLABLE, CHECK BETWEEN 0 AND 3 | 0=完全非结构化/非数字；1=部分结构化；2=大部分结构化；3=完全结构化/API可调；须与同行其他D字段共同决定 agentifiability |
| DP-022 | agent_d2_rule_clear | Agent 化评估维度D2：规则清晰程度（0-3分） | `L4-Agent化严谨评分.csv` 列 D2 规则清晰 ✅ | SMALLINT, NULLABLE, CHECK BETWEEN 0 AND 3 | 0=规则依赖主观判断；1=规则部分可编码；2=规则基本可编码；3=规则完全可编码 |
| DP-023 | agent_d3_output_verify | Agent 化评估维度D3：输出可验证程度（0-3分） | `L4-Agent化严谨评分.csv` 列 D3 输出可验 ✅ | SMALLINT, NULLABLE, CHECK BETWEEN 0 AND 3 | 0=输出需人工主观评价；1=部分可量化验证；2=大部分可量化；3=输出完全可量化验证 |
| DP-024 | agent_d4_api_reach | Agent 化评估维度D4：API 可达程度（0-3分） | `L4-Agent化严谨评分.csv` 列 D4 API可达 ✅ | SMALLINT, NULLABLE, CHECK BETWEEN 0 AND 3 | 0=系统完全不可程序化访问；1=有部分API；2=大部分API可用；3=全链路API可达 |
| DP-025 | agent_d5_fallback | Agent 化评估维度D5：降级可用程度（0-3分） | `L4-Agent化严谨评分.csv` 列 D5 降级可用 ✅ | SMALLINT, NULLABLE, CHECK BETWEEN 0 AND 3 | 0=Agent失败无法降级，必须人工重做全程；1=降级成本高；2=降级成本可接受；3=降级透明，人工无感知接管 |
| DP-026 | agent_d6_compliance | Agent 化评估维度D6：合规可编码程度（0-3分） | `L4-Agent化严谨评分.csv` 列 D6 合规可编码 ✅ | SMALLINT, NULLABLE, CHECK BETWEEN 0 AND 3 | 0=合规要求需人工解读；1=部分合规规则可编码；2=大部分；3=全部合规规则可程序化实现 |
| DP-027 | agent_score_total | Agent 化6维评分总分（D1~D6之和，0-18分） | `L4-Agent化严谨评分.csv` 列"总分" ✅ | SMALLINT, NULLABLE, CHECK BETWEEN 0 AND 18 | 须等于 D1+D2+D3+D4+D5+D6 之和（数据库层 CHECK 约束）；Auto 通常 ≥ 14；Human 通常 ≤ 4 |
| DP-028 | sla_hours | SLA 标准时限（小时），从 L3 协同框架中提取 | 任务3.4-A：从 L3 协同框架.txt 提取（Week 4）⚠️ | FLOAT, NULLABLE, CHECK > 0 | 必须 > 0；提取时须注明来源段落（见 sla_source）；若协同框架未定义 SLA，允许为 NULL（初始化阶段）；NULL 则 FACT_CARD 的 sla_breach_flag 自动为 NULL |
| DP-029 | sla_source | SLA 时限数据的来源说明（协同框架文件名+段落） | 任务3.4-A 填写 ⚠️ | VARCHAR(100), NULLABLE | 格式建议：`L3-XXX/协同实施框架.txt:监控体系-时限要求`；sla_hours 有值时须 NOT NULL |
| DP-030 | version | 本条 L4 定义记录的版本号（SCD Type 2） | 系统自动维护 ✅ | SMALLINT, NOT NULL, DEFAULT 1 | 初始为 1；每次 L4 定义变更（如里程碑升版）时新建一行，版本号 +1；同一 l4_code 只能有一条 is_current=TRUE |
| DP-031 | valid_from | 本版本 L4 定义的生效日期 | 系统自动取更新日期 ✅ | DATE, NOT NULL, DEFAULT CURRENT_DATE | 须 ≤ valid_to（若 valid_to 不为 NULL）；首版为建库日期 2026-04-22 |
| DP-032 | valid_to | 本版本 L4 定义的失效日期（NULL 表示仍为当前版本） | 系统在新版本生效时自动更新旧版 ✅ | DATE, NULLABLE | NULL 仅允许存在于 is_current=TRUE 的行；有值时须 ≥ valid_from |
| DP-033 | is_current | 是否为当前有效版本 | 系统自动维护 ✅ | BOOLEAN, NOT NULL, DEFAULT TRUE | 同一 l4_code 下有且仅有一条记录 is_current=TRUE（唯一约束）；历史版本 is_current=FALSE |
| DP-034 | source_notes | 数据来源补充说明（如 G3-1补充 / 原BMC-01 等历史溯源） | `L4-Agent化清单.csv` 第8列"备注" ✅ | TEXT, NULLABLE | 无格式约束；用于记录 M2 裁定中的分组标注（G3-1~G7-X）和合并来源 |

---

## 三、DIM_VS — 价值流维度表

> 数据来源：`02_架构全景/A_业务架构/A2_价值流全景/VS-*.csv`（按 VS-CSV列结构规范_V1.md 10列格式）
> 每行 = 一个价值流（VS）的一个价值阶段（Stage），粒度为 VS × Stage

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DV-001 | vs_key | 维度表代理主键 | 系统自动生成 SERIAL ✅ | SERIAL, PRIMARY KEY | 自增，不允许手工设置 |
| DV-002 | vs_code | 价值流编码 | VS-*.csv 第1列 ✅ | VARCHAR(10), NOT NULL | 枚举值：VS-1 / VS-2 / VS-3 / VS-4 / VS-5 / L1-05；L1-05 为权益中台横切能力层（非外部价值流，特殊处理）|
| DV-003 | vs_name | 价值流名称 | VS-*.csv 第2列 ✅ | VARCHAR(80), NOT NULL | VS-1=保司资源投放旅程 / VS-2=机构合作伙伴旅程 / VS-3=KA上架旅程 / VS-4=理财师发展旅程 / VS-5=终端客户服务旅程；**禁用旧术语**：不得使用 MORM/SMPS/MDF/PACE/CESV 等废弃命名 |
| DV-004 | vs_stakeholder | 价值流外部利益相关者 | VS-*.csv 第3列 ✅ | VARCHAR(50), NOT NULL | 合法值：保险公司/保司 / TOB机构/经代机构/家办/同行经代 / KA/TOA/个人IP / 理财师/代理人 / 终端客户/客户；**禁止填写内部角色**：中台/支撑组织/业务部门/业务中台（违反外部性检验规则，validate_kb.py 强制拦截）|
| DV-005 | s2b2a_layer | 在 S2B2A 商业模式中的层级定位 | 按 vs_stakeholder 对照 S2B2A 模型推导 ✅ | VARCHAR(5), NOT NULL | 枚举值：S（平台/中台）/ B（TOB机构）/ A（理财师/代理人）/ C（终端客户）/ 横切（L1-05）；VS-1=S / VS-2=B / VS-3=B / VS-4=A / VS-5=C / L1-05=横切 |
| DV-006 | vs_trigger | 价值流整体触发条件（外部触发事件） | VS-*.csv 第4列 ✅ | TEXT, NULLABLE | 只在 stage_sequence=1 的行填写，其余阶段为 NULL；触发方必须是外部利益相关者；如：保司评估MGA合作机会 |
| DV-007 | stage_code | 价值阶段编号，在 vs_code 范围内唯一 | VS-*.csv 第5列 ✅ | VARCHAR(10), NOT NULL | 格式：`S\d+`（如 S1/S2/S7）；不允许跳号（若 VS-1 有7阶段，必须 S1~S7 连续）|
| DV-008 | stage_name | 价值阶段名称 | VS-*.csv 第6列 ✅ | VARCHAR(80), NOT NULL | 不能与同一 vs_code 下其他阶段名称重复；须描述该阶段的核心价值交付主题 |
| DV-009 | stage_sequence | 价值阶段在价值流中的顺序编号（整数） | VS-*.csv 第5列转换 ✅ | SMALLINT, NOT NULL, CHECK > 0 | 在同一 vs_code 内从 1 连续递增；不允许重复；用于排序和趋势分析 |
| DV-010 | stage_exit_condition | 价值阶段的退出条件（该阶段完成的可视化标志） | VS-*.csv 第10列 ✅ | TEXT, NULLABLE | 须描述具体物理标志（如"签署MGA授权合同"）；不能是模糊描述（如"工作完成"）；与 DIM_PROCESS.l3_exit_condition 语义一致 |
| DV-011 | l3_primary | 本阶段的直属主要 L3 流程编码 | VS-*.csv 第8列"直属L3" ✅ | VARCHAR(20), NULLABLE | 格式：`^L3-[A-Z]{2,6}$`；必须存在于 DIM_PROCESS.l3_code；一个阶段可对应多个 L3（用逗号分隔，如 L3-IAO,L3-IAC），但建议拆行处理 |
| DV-012 | l1_05_consumed | 本阶段消费的 L1-05 权益中台横切能力 L3 列表（JSON 数组） | VS-*.csv 第9列"消费L1-05能力" ✅ | TEXT（JSON数组格式）, NULLABLE | 格式：`["L3-SRA","L3-RPD"]`；若不消费横切能力则为 NULL 或 `[]`；数组中每个 L3 编码须属于 L1-05 业务域；L1-05 自身行此字段为 NULL |
| DV-013 | stage_deliverable | 阶段结束时的可视交付物（可选，VS-*.csv 第11列） | VS-*.csv 第11列（可选列）⚠️ | VARCHAR(200), NULLABLE | 可选字段；填写时须与 DIM_PROCESS.l4_deliverable 中对应 L4 的交付物语义一致 |
| DV-014 | stage_kpi | 阶段级度量指标（可选，VS-*.csv 第12列） | VS-*.csv 第12列（可选列）⚠️ | VARCHAR(200), NULLABLE | 可选字段；填写时建议与 DIM_KPI 中的 kpi_code 关联 |
| DV-015 | coverage_status | 本阶段数据覆盖状态（用于识别分析盲区） | Terresa 手工维护 ⚠️ | VARCHAR(10), NOT NULL, DEFAULT 'PARTIAL' | 枚举值：OK（阶段完整，L3框架+RACI+流程图均齐备）/ PARTIAL（有框架但流程图为空或RACI冲突）/ GAP（缺失阶段，需新建 L3）|

---

## 四、DIM_ORG — 组织维度表

> 数据来源：`04_项目工作区/M3_组织重组/JD_*.md`（7族）+ `M3.1核心介入点聚类分析.md` + `HR基线数据模板_M3.xlsx`（Ivan回传后）
> 粒度：岗位级（同一岗位族内可有多个岗位；同一岗位可有多个执行人，每人一行）

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DO-001 | org_key | 维度表代理主键 | 系统自动生成 SERIAL ✅ | SERIAL, PRIMARY KEY | 自增，不允许手工设置 |
| DO-002 | position_family | 岗位族编码（M3.4组织架构图定义的7族） | JD_*.md 文件命名 ✅ | VARCHAR(5), NOT NULL | 枚举值：A / B / C / D / E / F / G / 职能；A=保司交付 / B=保司关系 / C=机构业务 / D=代理人事业部（运营）/ E=代理人事业部（辅导）/ F=权益中台 / G=佣金合规 |
| DO-003 | position_family_name | 岗位族名称 | JD_*.md 标题 ✅ | VARCHAR(50), NOT NULL | 与 DO-002 枚举一一对应，不可自定义 |
| DO-004 | position_code | 岗位编码（岗位族内唯一） | 岗位设计方案 / JD内部定义 ⚠️ | VARCHAR(20), NULLABLE | 格式建议：`<族编码>-<两位序号>`，如 A-01（保司交付规则执行器）；GAP-01完成前允许为 NULL |
| DO-005 | position_name | 岗位名称 | JD_*.md 标题中的岗位名称 ✅ | VARCHAR(80), NULLABLE | 如：保司交付规则执行器 / 保司战略官 / 保司关系经理 / 佣金合规专家 |
| DO-006 | position_nature | 岗位本质属性（M3原则2：执行/战略/专业） | JD_*.md 内容描述推导 ✅ | VARCHAR(10), NULLABLE | 枚举值：执行 / 战略 / 专业；执行型岗位只能承接：执行/分析/谈判/评估，不能承接战略设计/创意判断/规则定义（M3原则2）|
| DO-007 | ep_count | 本岗位覆盖的核心肉身介入点数量 | `M3.1核心介入点聚类分析.md` + `核心介入点清单.csv` ✅ | SMALLINT, NULLABLE, CHECK >= 0 | 全公司合计~126条EP（M3.2锁定）；单岗位EP数量不超过30（超出则岗位设计可能有问题）|
| DO-008 | headcount_target_min | 本岗位最小编制目标人数 | M3.4组织架构图V0 ✅ | SMALLINT, NULLABLE, CHECK >= 0 | 须 ≤ headcount_target_max；全公司合计 27-34 人（M3.4锁定）|
| DO-009 | headcount_target_max | 本岗位最大编制目标人数 | M3.4组织架构图V0 ✅ | SMALLINT, NULLABLE, CHECK >= 0 | 须 ≥ headcount_target_min |
| DO-010 | mark_retained | Mark 是否将本岗位相关决策纳入减负清单保留项 | `Mark减负清单V0.3.md`（29→11条保留）✅ | BOOLEAN, NOT NULL, DEFAULT FALSE | 全公司 mark_retained=TRUE 的岗位/决策类型不超过 11 条（Mark减负清单V0.3锁定）；TRUE 时该岗位对应 L4 的 escalation_flag 高概率为 TRUE |
| DO-011 | executor_id | 实际执行人工号 | `HR基线数据模板_M3.xlsx`（Ivan回传后填入）❌ | VARCHAR(20), NULLABLE | 格式：公司员工工号格式；允许为 NULL（过渡期）；填写后须验证在公司 HR 系统存在 |
| DO-012 | executor_name | 实际执行人姓名 | `HR基线数据模板_M3.xlsx` ❌ | VARCHAR(50), NULLABLE | 允许为 NULL；须与 executor_id 一一对应 |
| DO-013 | reports_to_family | 汇报线所属岗位族 | M3.4组织架构图V0 ✅ | VARCHAR(5), NULLABLE | 枚举值同 DO-002；跨族汇报须在 JD 中明确声明 |
| DO-014 | is_active | 岗位是否当前有效 | 系统维护 ✅ | BOOLEAN, NOT NULL, DEFAULT TRUE | 过渡期废弃的旧岗位设为 FALSE；FALSE 的岗位不参与 FACT_CARD 的新记录写入 |
| DO-015 | effective_date | 本岗位设定的生效日期 | 组织架构图版本日期 ✅ | DATE, NULLABLE | 建议填写 M3.4 组织架构图V0 的批准日期 |

---

## 五、DIM_TIME — 时间维度表

> 纯脚本生成，覆盖 2024-01-01 至 2027-12-31（约 1461 行）
> 无外部数据依赖，Week 3 一次性初始化

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DT-001 | time_key | 时间维度主键（整数格式 YYYYMMDD） | 脚本自动生成 ✅ | INT, PRIMARY KEY | 格式：YYYYMMDD 8位整数，如 20260422；全表唯一；2024~2027 年连续不断档 |
| DT-002 | full_date | 完整日期 | 脚本自动生成 ✅ | DATE, NOT NULL, UNIQUE | 与 time_key 一一对应：time_key = CAST(TO_CHAR(full_date,'YYYYMMDD') AS INT) |
| DT-003 | year | 年份 | 脚本自动生成 ✅ | SMALLINT, NOT NULL | 取值范围：2024~2027；EXTRACT(YEAR FROM full_date) |
| DT-004 | quarter | 季度 | 脚本自动生成 ✅ | SMALLINT, NOT NULL, CHECK BETWEEN 1 AND 4 | EXTRACT(QUARTER FROM full_date) |
| DT-005 | month | 月份 | 脚本自动生成 ✅ | SMALLINT, NOT NULL, CHECK BETWEEN 1 AND 12 | EXTRACT(MONTH FROM full_date) |
| DT-006 | week | ISO 周数 | 脚本自动生成 ✅ | SMALLINT, NOT NULL, CHECK BETWEEN 1 AND 53 | EXTRACT(WEEK FROM full_date)；ISO 8601 标准，跨年周归属按 ISO 规则 |
| DT-007 | day_of_week | 星期几（1=周一，7=周日） | 脚本自动生成 ✅ | SMALLINT, NOT NULL, CHECK BETWEEN 1 AND 7 | EXTRACT(ISODOW FROM full_date)；不使用 PostgreSQL 默认的 0=周日 |
| DT-008 | day_of_year | 一年中的第几天 | 脚本自动生成 ✅ | SMALLINT, NOT NULL, CHECK BETWEEN 1 AND 366 | EXTRACT(DOY FROM full_date) |
| DT-009 | is_weekday | 是否为工作日（周一至周五，不考虑节假日） | 脚本自动生成 ✅ | BOOLEAN, NOT NULL | day_of_week BETWEEN 1 AND 5 → TRUE；不处理法定节假日（当前精度够用）|

---

## 六、DIM_AGENT — Agent 维度表

> 数据来源：`L4-Agent化清单.csv`（评估分级）+ `mga-data-platform/agents/`（已上线）+ `M4_Agent建设优先级V0.md`（规划）

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DA-001 | agent_key | 维度表代理主键 | 系统自动生成 SERIAL ✅ | SERIAL, PRIMARY KEY | 自增，不允许手工设置 |
| DA-002 | agent_code | Agent 唯一编码（技术层面标识符） | `mga-data-platform/agents/` 目录名 / 规划命名 ✅ | VARCHAR(30), NOT NULL, UNIQUE | 格式：`agent-[a-z-]+`（小写字母和连字符）；如 agent-process-mapper；须与 mga-data-platform 代码库中的实际命名一致 |
| DA-003 | agent_name | Agent 业务名称（可读性强） | `02_Agent配置/agents/` 配置文件 ✅ | VARCHAR(100), NOT NULL | 如：流程Agent映射器；须与 `agent_roadmap.md` 中记录的名称一致 |
| DA-004 | agent_type | Agent 处理模式 | `L4-Agent化清单.csv` Tier 列（取值 Auto/Aug/Hybrid）✅ | VARCHAR(10), NOT NULL | 枚举值：Auto（完全自动，人监督）/ Aug（Agent主导+人审批）/ Hybrid（人主导+Agent辅助）；不包含 Human（Human不是Agent，是人工）|
| DA-005 | agent_status | Agent 建设状态 | `M4_Agent建设优先级V0.md` + 实际部署情况 ✅ | VARCHAR(20), NOT NULL | 枚举值：已上线 / 开发中 / 规划中 / 已停用；当前唯一已上线：agent-process-mapper（上线日期 2026-04-21）|
| DA-006 | l3_primary | Agent 主要覆盖的 L3 流程编码 | `agent_roadmap.md` + `02_Agent配置/agents/` 配置文件 ✅ | VARCHAR(20), NULLABLE | 格式：`^L3-[A-Z]{2,6}$`；必须存在于 DIM_PROCESS.l3_code；一个 Agent 可覆盖多个 L3（主L3填此字段，其余在 l4_codes_json 体现）|
| DA-007 | l4_codes_json | Agent 覆盖的全部 L4 编码列表（JSON 数组） | `L4-Agent化清单.csv` 按 agent_code 聚合 ⚠️ | TEXT（JSON数组格式）, NULLABLE | 格式：`["L4-COM-03","L4-COM-05"]`；数组中每个 l4_code 须存在于 DIM_PROCESS.l4_code；初始化时可为 NULL（先建框架，再补充）|
| DA-008 | l4_count_covered | Agent 覆盖的 L4 活动数量 | l4_codes_json 数组长度计算 ✅ | SMALLINT, NULLABLE, CHECK >= 0 | 须等于 JSON_ARRAY_LENGTH(l4_codes_json)；系统自动计算，不允许手工设置 |
| DA-009 | tech_stack | Agent 使用的技术栈描述 | `mga-data-platform/agents/` 代码库 ⚠️ | VARCHAR(100), NULLABLE | 如：Claude API + PostgreSQL + Webhook；Carrie 技术实施后填入 |
| DA-010 | platform_path | Agent 代码在 mga-data-platform 中的相对路径 | `mga-data-platform/agents/` 目录 ✅ | VARCHAR(200), NULLABLE | 如：agents/position_mapper/wechat_bot.py；已上线 Agent 须 NOT NULL |
| DA-011 | owner_position_family | Agent 的责任岗位族（负责监督和维护的人类岗位） | `L4_Auto_JD_Mapping_V1.csv` ❌ | VARCHAR(5), NULLABLE | 枚举值同 DO-002；GAP-01 完成后填入；Auto 类 Agent 的 owner 须明确（M4.2启动条件）|
| DA-012 | m4_priority | M4 建设优先级 | `M4_Agent建设优先级V0.md` ✅ | VARCHAR(5), NULLABLE | 枚举值：P0（M4.1第一批，80条Auto L4）/ P1（M4.1同步，Aug类）/ P2（M4.2后续）|
| DA-013 | go_live_date | Agent 实际上线日期 | 系统部署记录 ✅ | DATE, NULLABLE | agent_status='已上线' 时须 NOT NULL；不能晚于当前日期 |
| DA-014 | baseline_accuracy | Agent 上线后基线准确率（0-1浮点数），与人工判断对比 | Agent 运行日志统计（Week 8+）❌ | FLOAT, NULLABLE, CHECK BETWEEN 0 AND 1 | M4 质量标准暂定：Auto 类准确率须 ≥ 0.95 才可减少人工监督；低于 0.85 须触发人工接管 |
| DA-015 | baseline_throughput | Agent 日均处理量（条/天） | Agent 运行日志统计（Week 8+）❌ | INT, NULLABLE, CHECK >= 0 | 上线4周后填入基线值；用于估算人效提升（agent_save_hours 计算基础）|

---

## 七、DIM_M_STRATEGY — 战略维度表

> 数据来源：CLAUDE.md M0-M8 定义 + `05_分析与决策报告/架构诊断/市场反馈×中台M0-M8交叉覆盖分析报告.pdf`
> 9行静态数据，Week 3 一次性手工录入

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DS-001 | strategy_key | 维度表代理主键 | 系统自动生成 SERIAL ✅ | SERIAL, PRIMARY KEY | 自增 |
| DS-002 | strategy_level | 战略层级编码（M0~M8） | CLAUDE.md + 市场反馈分析报告 ✅ | VARCHAR(5), NOT NULL, UNIQUE | 枚举值：M0 / M1 / M2 / M3 / M4 / M5 / M6 / M7 / M8；全表唯一；不允许新增 M9 及以上（须Mark裁定）|
| DS-003 | strategy_name | 战略层级名称 | CLAUDE.md + 市场反馈分析报告 ✅ | VARCHAR(80), NOT NULL | 如：M0=市场定位 / M1=价值主张 / M2=商业模式 / M3=组织能力 / M4=产品服务 / M5=渠道获客 / M6=运营流程 / M7=数据技术 / M8=绩效合规 |
| DS-004 | strategy_description | 战略层级的业务含义描述 | 市场反馈×中台M0-M8分析报告 ✅ | TEXT, NULLABLE | 可参考"市场反馈×中台M0-M8交叉覆盖分析报告.pdf"中的层级定义段落 |
| DS-005 | claude_v2_domain | 关联的 CLAUDE_V2 七大域 | CLAUDE.md 中的域定义 ✅ | VARCHAR(20), NULLABLE | 如：D4中台与数据 / D6组织与人才；一个 M 层级可关联多个 D 域（用逗号分隔）|
| DS-006 | sequence | 战略层级排序（用于报表展示） | 按 M0~M8 顺序固定 ✅ | SMALLINT, NOT NULL | CHECK BETWEEN 0 AND 8；与 strategy_level 中的数字一致，M0→0，M8→8 |

---

## 八、DIM_KPI — KPI 维度表

> 数据来源：**尚未产出**，依赖任务3.4-B（效率分公式）+ KPI穿透矩阵（Phase 2产物，约 Week 6）
> 当前建空表结构，Week 6 前批量导入

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DK-001 | kpi_key | 维度表代理主键 | 系统自动生成 SERIAL ✅ | SERIAL, PRIMARY KEY | 自增 |
| DK-002 | kpi_code | KPI 唯一编码 | KPI穿透矩阵产出 ❌ | VARCHAR(20), NOT NULL, UNIQUE | 格式建议：`KPI-<VS或层级>-<序号>`，如 KPI-VS1-001（VS-1对应KPI001）/ KPI-ORG-001（岗位级KPI）|
| DK-003 | kpi_name | KPI 名称 | KPI穿透矩阵产出 ❌ | VARCHAR(100), NOT NULL | 如：APE达成率 / 人效（万/人/年）/ SLA达标率；名称须与绩效体系文档一致 |
| DK-004 | kpi_type | KPI 分类 | KPI穿透矩阵产出 ❌ | VARCHAR(20), NOT NULL | 枚举值：企业KPI / 岗位KPI / 流程KPI；企业KPI=全公司追踪 / 岗位KPI=与岗位绩效挂钩 / 流程KPI=流程效率度量 |
| DK-005 | kpi_level | KPI 挂载层级 | KPI穿透矩阵产出 ❌ | VARCHAR(10), NOT NULL | 枚举值：企业 / L2 / L3 / 岗位；与 kpi_type 联动：企业KPI→企业 / 流程KPI→L2或L3 / 岗位KPI→岗位 |
| DK-006 | kpi_formula | KPI 计算公式（文字描述） | 任务3.4-B产出 ❌ | TEXT, NULLABLE | 如：APE达成率 = 实际APE / 目标APE × 100%；须Mark确认后写入 |
| DK-007 | kpi_target | KPI 目标值 | 经营目标文件 / Mark裁定 ❌ | FLOAT, NULLABLE | 须配合 kpi_unit 解读；如人效目标 = 400（万元/人/年），目标态 = 800 |
| DK-008 | kpi_unit | KPI 度量单位 | KPI穿透矩阵产出 ❌ | VARCHAR(20), NULLABLE | 枚举建议：万元 / % / 次 / 小时 / 人 / 万元/人/年；须在系统内统一（避免混用元和万元）|
| DK-009 | measurement_cycle | KPI 统计周期 | KPI穿透矩阵产出 ❌ | VARCHAR(10), NOT NULL | 枚举值：日 / 周 / 月 / 季 / 年；与 FACT_CARD 的时间粒度对齐 |
| DK-010 | vs_code | KPI 关联的价值流 | KPI穿透矩阵产出 ❌ | VARCHAR(10), NULLABLE | 枚举值同 DV-002；跨价值流的企业KPI此字段为 NULL |
| DK-011 | position_family | KPI 关联的岗位族 | KPI穿透矩阵产出 ❌ | VARCHAR(5), NULLABLE | 枚举值同 DO-002；企业级KPI此字段为 NULL |
| DK-012 | strategy_level | KPI 关联的战略层级 | KPI穿透矩阵产出 ❌ | VARCHAR(5), NULLABLE | 枚举值同 DS-002；如人效KPI关联 M3组织能力 |
| DK-013 | is_mark_kpi | 是否属于 Mark 保留的顶层 KPI（不可下放代理）| `Mark减负清单V0.3.md` ✅ | BOOLEAN, NOT NULL, DEFAULT FALSE | Mark保留11条中的 KPI 类条目设为 TRUE；TRUE 的 KPI 不得在 Agent 报告中自动裁定，须提交 Mark |

---

## 九、DIM_DELIVERABLE — 交付物维度表

> 数据来源：`L4-Agent化清单.csv` 第4列"物理交付物"（253条），Week 3 与 DIM_PROCESS 同批导入
> 依据 L4 唯一物理交付物原则（CLAUDE.md 5.0节）：一个 L4 = 一个物理交付物 = DIM_DELIVERABLE 一行

| 字段ID | 字段名称 | 含义 | 取值来源 | 数据标准 | 校验规则 |
|--------|---------|------|---------|---------|---------|
| DD-001 | deliverable_key | 维度表代理主键 | 系统自动生成 SERIAL ✅ | SERIAL, PRIMARY KEY | 自增 |
| DD-002 | deliverable_name | 物理交付物完整名称 | `L4-Agent化清单.csv` 第4列 ✅ | TEXT, NOT NULL | 须与 DIM_PROCESS.l4_deliverable 完全一致（1:1 关系）；禁止填写行为描述（如"完成XX工作"），须为可被接收/审计/引用的实体产物名称 |
| DD-003 | deliverable_type | 交付物类型（细分类） | 按 deliverable_name 内容自动分类 ✅ | VARCHAR(30), NOT NULL | 枚举值：报告 / 合同 / 凭证 / 数据表 / 决议 / 方案 / 系统记录 / 签字文件；分类规则见下方"交付物分类规则表" |
| DD-004 | deliverable_category | 交付物大类（粗分类，用于跨类型对比分析） | 按 deliverable_type 映射 ✅ | VARCHAR(20), NOT NULL | 枚举值：文档（含报告/方案）/ 签约文件（含合同/签字文件）/ 数字产物（含数据表/系统记录）/ 决策产物（含决议/凭证）|
| DD-005 | l4_code | 关联的 L4 活动编码（1:1 关系） | `L4-Agent化清单.csv` 第2列 ✅ | VARCHAR(20), NOT NULL, UNIQUE | 在全表唯一（一个 L4 只对应一个物理交付物）；格式：`^L4-[A-Z]{2,6}-\d{2}[a-z]?$`；须存在于 DIM_PROCESS.l4_code |
| DD-006 | l3_code | 关联的 L3 流程编码 | `L4-Agent化清单.csv` 第1列 ✅ | VARCHAR(20), NOT NULL | 格式：`^L3-[A-Z]{2,6}$`；须存在于 DIM_PROCESS.l3_code |
| DD-007 | vs_code | 关联的价值流编码（从 DIM_PROCESS 通过 l3_code 推导） | DIM_VS 关联查询 ✅ | VARCHAR(10), NULLABLE | 枚举值同 DV-002；通过 l3_code → DIM_VS.l3_primary 关联得出；一个 L3 可归属多个 VS 时，取主 VS |
| DD-008 | agentifiability | 该交付物所在 L4 的 Agent 化级别（冗余，用于交付物维度的 Agent 分析） | 从 DIM_PROCESS.agentifiability 复制 ✅ | VARCHAR(10), NOT NULL | 枚举值：Auto / Aug / Hybrid / Human；须与 DIM_PROCESS 中对应 l4_code 的 agentifiability 一致 |

---

### 附：交付物分类规则表

| 触发条件（deliverable_name 特征）| deliverable_type | deliverable_category |
|-------------------------------|-----------------|---------------------|
| 含《》且内容为分析/评估/调研结论 | 报告 | 文档 |
| 含《》且内容为方案/框架/计划 | 方案 | 文档 |
| 含"合同"/"协议"/"授权书" | 合同 | 签约文件 |
| 含"已签署"/"签字" | 签字文件 | 签约文件 |
| 含"凭证"/"申报"/"外发" | 凭证 | 决策产物 |
| 含"决议"/"裁定"/"纪要" | 决议 | 决策产物 |
| 含"清单"/"配置"/"记录"/"数据流" | 数据表 | 数字产物 |
| 含"系统"/"日志"/"数据"（无《》）| 系统记录 | 数字产物 |

---

## 十、数据字典版本与变更规则

| 项目 | 说明 |
|------|------|
| **当前版本** | V1.0（2026-04-22）|
| **下次更新触发条件** | ①新增维度表字段；②枚举值变更（需 Mark 裁定）；③validate_kb.py 校验规则扩展；④KPI穿透矩阵完成（DIM_KPI 批量录入，约 Week 6）|
| **变更流程** | Terresa 起草变更说明 → Carrie 评估技术影响 → 若涉及枚举值扩展提 Mark 裁定 → 更新本文件并同步 DDL 变更脚本 |
| **与 DDL 的一致性** | 本数据字典与 `mga-data-platform/etl/process/create_process_schema.sql` 须保持字段级一致；DDL 变更时须同步更新本字典 |
| **校验责任** | 数据库层：Carrie（CHECK 约束 + 触发器）；应用层：手工录入表单校验（Terresa 设计）；知识库层：validate_kb.py（l3_code/l4_code格式+枚举）|

---

*本数据字典是流程数据库建设的权威字段规范。任何与本字典不符的建表脚本或录入行为均视为缺陷。*
*与 TMPL_流程数据库FACT_Card_V1.md 冲突时，以本字典为准（本字典更新）。*
