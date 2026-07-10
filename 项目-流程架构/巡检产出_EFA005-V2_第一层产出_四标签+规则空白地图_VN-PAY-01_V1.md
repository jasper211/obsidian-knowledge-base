---
type: project_note
project: 流程架构
layer: "02_过程成果-工作产出"
layer_tag: 过程
subdir: "规则分析"
tags: [过程, 规则]
---

## 🧭 导航
⬆️ [[02_过程成果-工作产出]] · ⬆️ [[规则分析]] · 🏠 [[流程架构项目MOC]]

---

# EFA005-V2 · VN-PAY-01市场佣金制作产出包 · 第一层产出 V1

> **任务包**：TASK-M4W10-019 | **版本**：V1.0 | **授权人**：Jasper | **执行终端**：Kimi | **日期**：2026-05-28
> **前置方法论**：数据规则提取方法论_三层递进提取法_v2.3.md
> **执行情景**：情景3（路径A+B融合）
> **分析单元**：价值节点视角（v2.3）
> **重要声明**：本任务将旧版EFA005（表视角，35条规则空白）升级为EFA005-V2（价值节点视角，聚焦VN-PAY-01/COM-01+COM-02），不直接复制旧版内容

---

## 一、执行声明

| 维度 | 内容 |
|:---|:---|
| **执行情景** | 情景3（路径A+B融合） |
| **分析单元** | 价值节点视角 — VN-PAY-01（COM-01+COM-02两个L4） |
| **旧版参照** | EFA005 V1.1（12张表视角，35条规则空白）→ 仅作参考，不直接复制 |
| **输入文件** | ①D1_价值节点清单_V3.0.xlsx（VN-PAY-01详情卡）<br>②EFA佣金制作14张表（输入）.xlsx<br>③EFA佣金制作定义（输入）.xlsx<br>④调研_L4交付物_含付款流程_V1.0.xlsx（L3-COM序号1-13）<br>⑤旧版EFA005第一层产出V1.1（参考已识别规则空白）<br>⑥FIN001-V2第一层产出（价值节点视角格式参考） |
| **分析日期** | 2026-05-28 |

**价值节点视角执行规范**：
- VN-PAY-01为🟡P0规范化节点，进入四标签分析
- 分析范围严格限定于COM-01（季度源头佣金录入）+ COM-02（市场佣金制作）两个L4
- 超出VN-PAY-01范围的规则线索记录为「附加观察」，不纳入正文
- 旧版35条规则空白经视角收窄后，仅保留与COM-01/COM-02直接相关的条目

---

## 二、VN-PAY-01分析框架确认

### 【VN-PAY-01 · 市场佣金制作产出包】

**节点状态**：🟡P0规范化（来自V3.0）
**L3端到端闭环**：市场佣金制作E2E
**构成子产物**：《季度源头佣金表》+《市场佣金表》(2子产物同闭环)
**物理形态**：Excel(双子表+源头PDF合订)·xlsx+pdf
**起点A → 终点Z**：保险公司源头佣金PDF/Excel(季度) → 《市场佣金表(月)》v.final
**L4范围**：COM-01 季度源头佣金录入 + COM-02 市场佣金制作
**生产方**：Lillian / Joanne / 刘敏然（COM-01录入）/ MOMO（COM-02制作）
**消费方**：对账/应派/产品复盘
**频次**：季×1 + 月×1
**M0-M8锚定**：M7产品策略 / M6业务渗透 / M0数理基建
**KPI锚定**：佣金回收周期(KPI#15)、佣金口径准确率(KPI#16)

#### 涉及数据表（按起点A→终点Z数据流顺序）

| 序号 | 表名（英文） | 表名（中文） | 表类型 | 数据链段 | 关联L4 |
|:---:|:---|:---|:---|:---|:---|
| 1 | 佣金准入表 | 佣金准入表 | 过程表 | 零段·业务准入录入 | COM-01 |
| 2 | fact_commission_rate | 佣金率事实表 | 事实表 | 第一段·源头佣金生成 | COM-01 |
| 3 | config_product_commission_formula | 产品佣金计算公式 | 参数表 | 第一段·源头佣金生成 | COM-01 |
| 4 | config_license_carrier_mapping | 牌照保司路由 | 参数表 | 第一段·源头佣金生成 | COM-01 |
| 5 | agg_source_commission_wide | 源头佣金宽表 | 聚合表 | 第一段·源头佣金生成 | COM-01 |
| 6 | config_commission_table_type | 市场佣金制表参数 | 参数表 | 第二段·市场档位拆解 | COM-02 |
| 7 | config_product_exclusion_range | 产品排除范围配置 | 参数表 | 第二段·市场档位拆解 | COM-02 |
| 8 | product_risk_override | 产品属性覆写路由 | 参数表 | 第二段·市场档位拆解 | COM-02 |
| 9 | partner_tier_rules | 合作伙伴档位佣金规则 | 参数表 | 第二段·市场档位拆解 | COM-02 |
| 10 | config_partner_routing | 合作伙伴牌照路由 | 参数表 | 第二段·市场档位拆解 | COM-02 |
| 11 | agg_market_commission_tier_rate | 全档位佣金表 | 聚合表 | 第二段·市场档位拆解 | COM-02 |
| 12 | 市场佣金表 | 市场佣金表 | 终态聚合表 | 第三段·外发交付 | COM-02 |

> **外部引用维度表**（不在VN-PAY-01直接产出链上，但COM-02计算中引用）：dim_product_id（产品ID列表）、dim_product_sku（产品SKU列表）

#### P0规范化要求

VN-PAY-01 V3.0裁定结论：🟡 P0(P0规范化:源头PDF→OCR/标准化录入)

**P0规范化约束**（需在相关规则空白中明确标注）：
1. 保司源头PDF/Excel需标准化录入字段，建立OCR或结构化提取机制
2. 源头PDF需归档至OneDrive，建立版本追溯能力
3. 市场佣金表v.final需锁定版本号，建立版本管理规则

---

## 三、VN-PAY-01四标签分析

---

### A标签：表类型规则洞察

**A-涉及表类型分布**：
- 过程表×1（佣金准入表）+ 事实表×1（fact_commission_rate）+ 聚合表×3（agg_source_commission_wide、agg_market_commission_tier_rate、市场佣金表）+ 参数表×6（config_product_commission_formula、config_license_carrier_mapping、config_commission_table_type、config_product_exclusion_range、product_risk_override、partner_tier_rules、config_partner_routing）

**A-类型规则风险汇总**：
- **过程表（佣金准入表）**：准入标准主观性、信息完整性、审批链条风险。当前已从人工Excel录入切换为数据表提取，但切换规则未文档化。
- **事实表（fact_commission_rate）**：计算口径一致性、版本追溯、来源标记风险。ETL计算逻辑中的条件判断（first_year_formula/renewal_year_formula）若未文档化，将导致口径无法追溯。
- **聚合表×3**：聚合口径文档化、Owner空缺、回滚机制风险。agg_source_commission_wide和agg_market_commission_tier_rate全部字段Owner/Steward为空，聚合逻辑完全由ETL工程师隐式维护。
- **参数表×6**：变更审批、冲突解决、生效失活风险。6张配置表全部由业务人员维护config/目录下Excel，变更后通过sync同步至DB，但变更审批链、冲突检测机制、版本回滚规则全部缺失。

**A-本节点信号字段（跨表汇总）**：
- `佣金准入表.全部47字段` — ⛔保司格式不统一，列顺序/列名/日期格式/百分比表示方式均可能不同
- `fact_commission_rate.effective_start_date/effective_end_date` — 版本边界风险：签单时间落入哪个版本期的判定规则未代码化
- `fact_commission_rate.fyc_rate/ryc_rate` — ETL计算字段，公式版本标记缺失将导致历史佣金无法追溯计算口径
- `config_product_commission_formula.first_year_formula/renewal_year_formula` — 公式字段：语法正确但计算逻辑错误无法被程序检测
- `config_partner_routing.priority` — 核心仲裁字段，数值重复或逻辑错误将导致大规模出单错误
- `config_partner_routing.assigned_license_code` — 路由结果字段，若指向已失效牌照，将直接导致无照经营
- `agg_market_commission_tier_rate.partner_tier/fyc_tier` — 档位判定结果直接决定渠道激励水平，但聚合逻辑未业务确认
- `市场佣金表.全部字段` — ⛔推断字段：外发格式字段缺失（文件名/版本号/接收人/发送记录/签收机制）

---

### B标签：分工断点与字段唯一责任

**B-分工结构（按COM-01→COM-02数据流）**：

| 环节 | 分工人 | 填写人/执行人 | Owner | Steward | 责任模式 |
|:---|:---|:---|:---|:---|:---|
| COM-01: 源头PDF→佣金准入表 | Lillian/Joanne | 刘敏然（原手工录入，现ETL替代） | ⛔未定义 | ⛔未定义 | 治理真空🔴 |
| COM-01: 佣金准入表→fact_commission_rate | 刘敏然 | FACT1脚本（ETL） | 刘敏然 | MOMO | 准三权合一🔴 |
| COM-01→COM-02: fact_commission_rate→agg_source_commission_wide | 敏然 | Agg1脚本（ETL） | ⛔空 | ⛔空 | 治理真空🔴 |
| COM-02: Agg2制表参数配置 | Carrie | Carrie/momo | MOMO | MOMO | 三权合一🔴 |
| COM-02: Agg2档位规则配置 | Carrie | momo | MOMO | MOMO | 三权合一🔴 |
| COM-02: Agg2牌照路由配置 | Carrie | momo | MOMO | MOMO | 三权合一🔴 |
| COM-02: 市场佣金表终态调整 | ⛔Carrie(推断) | MOMO("edits") | ⛔空 | ⛔空 | 治理真空🔴 |

**B-单点责任字段（VN-PAY-01范围内）**：
- `佣金准入表.全部47字段` — 原刘敏然手工录入，现ETL提取；过渡期间责任归属与数据切换规则完全未定义
- `fact_commission_rate.fyc_rate/ryc_rate` — Owner=刘敏然，但ETL计算逻辑若出错，Owner是否具备排查能力存疑
- `fact_commission_rate.effective_start_date/effective_end_date` — 版本生效边界由业务配置维护，无独立Steward复核版本重叠
- `config_partner_routing.priority/assigned_license_code` — Owner=MOMO/Steward=MOMO/填写人=momo，三权合一，误改将直接导致大规模出单错误或无照经营
- `partner_tier_rules.fyc_adjustment/ryc_adjustment` — Owner=MOMO/Steward=MOMO/填写人=momo，三权合一，系数错误将直接造成大额财务偏差
- `市场佣金表.全部调整字段` — MOMO "edits market commission table"，但调整原因/差异/审批人全部未留痕

**B-字段级规则信号（C1-C5命中，VN-PAY-01范围内）**：

| 信号 | 命中表/字段 | 说明 |
|:---|:---|:---|
| C1 | 佣金准入表.全部字段 | 原为人工录入，现ETL替代；切换规则未定义 |
| C1 | fact_commission_rate.effective_start_date/effective_end_date | 人工维护费率版本和有效期 |
| C2 | fact_commission_rate.fyc_rate/ryc_rate | ETL计算字段，公式版本标记缺失 |
| C2 | config_product_commission_formula.first_year_formula/renewal_year_formula | 公式语法通过但计算逻辑错误无法被程序检测 |
| C2 | 市场佣金表.推断调整字段 | MOMO手工调整，调整规则未外化 |
| C3 | config_product_commission_formula.全部公式字段 | 保司调费/新产品上架时触发更新，无自动化提醒 |
| C3 | config_license_carrier_mapping.license_code/is_active/effective_to | 保司资质变更时触发，无自动化联动 |
| C3 | config_partner_routing.全部条件字段 | 业务变更时触发，无变更审批 |
| C3 | partner_tier_rules.全部档位字段 | 合作伙伴协议更新时触发，无标准化更新机制 |
| C3 | config_commission_table_type.全部参数字段 | 制表需求变更时触发，无重生成触发机制 |
| C4 | fact_commission_rate.fyc_rate/ryc_rate | Owner=刘敏然但ETL生成，"Owner挂名+ETL实际写入"的责任真空 |
| C4 | config_partner_routing.全部字段 | Owner=MOMO/Steward=MOMO/填写人=momo，三权合一 |
| C4 | partner_tier_rules.全部字段 | Owner=MOMO/Steward=MOMO/填写人=momo，三权合一 |
| C5 | fact_commission_rate.license_type/customer_type/tier_code | 枚举值约束，边界case（新产品未录入时默认匹配规则未定义） |
| C5 | config_partner_routing.partner_code_condition/commission_pattern等 | 条件字段枚举值，通配符规则未定义 |
| C5 | config_product_exclusion_range.excluded_product_sku等 | 排除维度枚举值，ALL通配规则未定义 |

---

### C标签：程序验证路径与断点

**C-验证路径（VN-PAY-01端到端）**：

```
保司源头PDF/Excel → [COM-01] 佣金准入表（录入/OCR）→ FACT1脚本ETL
  → fact_commission_rate（事实表）→ Agg1脚本聚合
  → agg_source_commission_wide（宽表）→ [COM-02] Agg2脚本综合
    → 6张配置表读取（制表参数/排除/覆写/档位/路由）
    → agg_market_commission_tier_rate（全档位表）→ Agg3脚本拆表
    → 市场佣金表（终态）→ 外发至合作伙伴/渠道
```

**C-在链位置**：源头+中间+终态（VN-PAY-01覆盖数据链全段，从保司PDF到市场佣金表外发）

**C-验证盲区（按数据链段）**：

| 链段 | 盲区类型 | 具体描述 |
|:---|:---|:---|
| COM-01: 源头PDF→佣金准入表 | **语义错误** | 保司PDF中的产品名称与内部产品编码可能不一致，无标准化映射表；不同保司命名格式/日期格式/百分比表示方式不统一 |
| COM-01: 源头PDF→佣金准入表 | **交接断点** | 源头PDF→Excel录入环节无验收标准（OCR准确率阈值未定义），Lillian/Joanne/刘敏然手工校验 |
| COM-01: FACT1 ETL | **公式错误** | 应使用产品A的公式计算，但FACT1脚本错误匹配了产品B的公式模板，所有字段非空/格式均通过，程序验证通过但整批佣金金额全部错误 |
| COM-01→COM-02: Agg1聚合 | **语义错误** | 同一保单被重复聚合（GROUP BY键不唯一），程序验证通过但下游档位佣金全部偏高 |
| COM-02: Agg2档位匹配 | **语义错误** | 业绩门槛四舍五入规则未定义，临界值保单档位跳变（如99.9999万 vs 100万门槛），程序验证通过但档位判定结果存在争议 |
| COM-02: Agg2牌照路由 | **状态错误** | 授权状态=有效但保司资质已过期，程序验证通过但后续出单将使用已失效保司 |
| COM-02: Agg2排除/覆写 | **语义错误** | 覆写规则与默认规则形成循环依赖，产品可售但无佣金，程序验证通过但业务逻辑断裂 |
| COM-02: 市场佣金表终态 | **触发缺失** | MOMO手工调整后无自动提醒/待办机制，调整原因/差异/审批人未留痕 |
| COM-02: 市场佣金表外发 | **交接断点** | 外发前无最终审核流程，外发版本与内部版本一致性无校验 |

---

### D标签：商业职能与授权

**D-职能定义**：M7产品策略 / M6业务渗透 / M0数理基建 → 涉及产品收益结构定义和数理基建标准化
**D-授权级别**：🔴 高（费率定义直接影响财务结算基数和市场佣金外发准确性）

**D-审核状态匹配**：
- **COM-01（fact_commission_rate）**：❌ 不匹配 — 表级审核状态缺失（Sheet1无此表记录），作为核心财务事实表缺乏审核状态跟踪
- **COM-02（市场佣金表）**：❌ 不匹配 — 高授权但终态表未经完整审核即外发，MOMO "edits" 后直接发送
- **配置表群（6张参数表）**：❌ 严重不匹配 — 最高授权级别（管理宪法/准入确权/财务结算）但config_partner_routing处于「待审核」，partner_tier_rules等无商业职能定义

**D-合规风险**：高 — 费率版本错误/路由错误/档位错误将产生系统性佣金差异，直接影响渠道激励成本和客户对账争议

---

### 价值节点Gate状态（直接引用V3.0）

| Gate | 状态 | V3.0说明 |
|:---|:---|:---|
| Gate①挂数 | PASS | 已关联KPI#15/#16 |
| Gate②落地 | PASS | 季度刷新+月度引用·实际跑通 |
| Gate③追溯 | PARTIAL | 源头PDF归档至OneDrive待标准化，v.final版本号未锁定 |
| **V3.0裁定** | 🟡 P0(P0规范化:源头PDF→OCR/标准化录入) | |

---

### 本节点规则空白贡献（VN-PAY-01视角）

⚠️ 佣金准入表已被数据表替代但切换规则与历史迁移规则完全未定义 → 五问：Q2+Q5 → 评分维度：D1+D5 → **P0**
⚠️ 市场佣金表手工调整（MOMO "edits"）的留痕规则、审批规则与回滚机制缺失 → 五问：Q3+Q5 → 评分维度：D2+D6 → **P0**
⚠️ config_partner_routing三权合一（Owner=Steward=填写人=momo），路由规则变更缺乏独立复核 → 五问：Q5 → 评分维度：D6 → **P0**
⚠️ 源头PDF→标准化录入无OCR/验收标准，P0规范化要求未落实 → 五问：Q1+Q4 → 评分维度：D1+D3 → **P0**
⚠️ fact_commission_rate ETL责任边界不清（Owner=刘敏然但ETL生成）→ 五问：Q5 → 评分维度：D6 → **P1**
⚠️ 市场佣金表外发版本与内部版本一致性校验缺失 → 五问：Q3+Q4 → 评分维度：D2+D3 → **P1**
⚠️ fact_commission_rate有效期重叠冲突解决规则缺失 → 五问：Q3 → 评分维度：D2 → **P1**
⚠️ config_product_commission_formula同一产品重叠生效日期冲突解决规则缺失 → 五问：Q3 → 评分维度：D2 → **P1**
⚠️ agg_source_commission_wide聚合逻辑缺乏业务方确认与文档化 → 五问：Q3+Q4 → 评分维度：D2+D3 → **P1**
⚠️ agg_market_commission_tier_rate聚合口径与业绩门槛动态调整规则缺失 → 五问：Q1+Q3 → 评分维度：D1+D2 → **P1**
⚠️ config_partner_routing多条件叠加匹配优先级仲裁规则未显性定义 → 五问：Q3 → 评分维度：D2 → **P1**
⚠️ 源头PDF产品命名→内部产品编码标准化映射规则缺失 → 五问：Q3 → 评分维度：D2 → **P1**
⚠️ config_commission_table_type制表参数变更后下游佣金表重生成触发机制缺失 → 五问：Q1+Q4 → 评分维度：D1+D3 → **P2**
⚠️ partner_tier_rules档位评定触发周期与历史追溯规则缺失 → 五问：Q1+Q3 → 评分维度：D1+D2 → **P2**
⚠️ product_risk_override覆写规则自动过期与定期清理机制缺失 → 五问：Q1+Q3 → 评分维度：D1+D2 → **P2**
⚠️ fact_commission_rate公式错误检测机制缺失 → 五问：Q3+Q4 → 评分维度：D2+D3 → **P2**

---

## 四、字段级规则信号清单（C1-C5，VN-PAY-01范围内）

### 高规则信号字段（需规则设计）

| 序号 | 关联L4 | 表名 | 字段名 | 信号标签 | 命中规则 | 当前状态 | 风险说明 |
|:---:|:---:|:---|:---|:---|:---|:---|:---|
| 1 | COM-01 | 佣金准入表 | 全部47字段 | C1 | 数据来源=人工录入 | ⛔责任未知（ETL替代中） | 保司格式不统一，切换规则未定义 |
| 2 | COM-01 | fact_commission_rate | fyc_rate | C2 | 计算口径含ETL | Owner=刘敏然 | ETL计算字段，公式版本标记缺失 |
| 3 | COM-01 | fact_commission_rate | ryc_rate | C2 | 计算口径含ETL | Owner=刘敏然 | 续期公式可能误用首期系数 |
| 4 | COM-01 | fact_commission_rate | effective_start_date | C1+C3 | 人工维护+按需更新 | Owner=刘敏然 | 有效期重叠冲突解决规则缺失 |
| 5 | COM-01 | fact_commission_rate | effective_end_date | C1+C3 | 人工维护+按需更新 | Owner=刘敏然 | 同上 |
| 6 | COM-01 | config_product_commission_formula | first_year_formula | C2+C3 | 公式字段+按需更新 | Owner=刘敏然 | 公式错误将造成首期佣金偏差 |
| 7 | COM-01 | config_product_commission_formula | renewal_year_formula | C2+C3 | 公式字段+按需更新 | Owner=刘敏然 | 续期公式错误长期影响支出 |
| 8 | COM-02 | agg_market_commission_tier_rate | partner_tier | C2 | 计算口径含ETL | Owner=空 | 档位判定结果无责任主体 |
| 9 | COM-02 | agg_market_commission_tier_rate | fyc_tier | C2 | 计算口径含ETL | Owner=空 | 聚合逻辑错误风险 |
| 10 | COM-02 | config_commission_table_type | table_type/commission_pattern | C1+C3+C4 | 人工录入+按需+Owner=Steward | Owner=MOMO | 直接决定市场佣金表输出格式 |
| 11 | COM-02 | config_partner_routing | priority | C1+C3+C4 | 人工录入+按需+三权合一 | Owner=MOMO | 优先级错误导致大规模出单错误 |
| 12 | COM-02 | config_partner_routing | assigned_license_code | C1+C3+C4 | 人工录入+按需+三权合一 | Owner=MOMO | 指向已失效牌照风险 |
| 13 | COM-02 | partner_tier_rules | fyc_adjustment | C1+C3+C4 | 人工录入+按需+三权合一 | Owner=MOMO | 系数错误将造成大额财务偏差 |
| 14 | COM-02 | partner_tier_rules | ryc_adjustment | C1+C3+C4 | 人工录入+按需+三权合一 | Owner=MOMO | 续期调整错误长期累积 |
| 15 | COM-02 | 市场佣金表 | 推断调整字段 | C2 | 手工调整 | ⛔责任未知 | MOMO"edits"未留痕 |

> **合计**：15个高规则信号字段

### 中规则信号字段（需关注）

| 序号 | 关联L4 | 表名 | 字段名 | 信号标签 | 命中规则 | 当前状态 | 风险说明 |
|:---:|:---:|:---|:---|:---|:---|:---|:---|
| 16 | COM-01 | fact_commission_rate | license_type/customer_type/tier_code | C5 | 枚举值约束 | Owner=刘敏然 | 枚举值变更影响范围 |
| 17 | COM-01 | config_license_carrier_mapping | license_code/is_active | C3 | 按需更新 | Owner=刘敏然 | 过期牌照风险 |
| 18 | COM-01 | config_product_commission_formula | basic_rate_from | C2+C3 | 公式字段+按需 | Owner=刘敏然 | 取值来源与实际协议一致性 |
| 19 | COM-02 | agg_source_commission_wide | commission_plan_code/fyc_rate | C2 | ETL聚合 | Owner=空 | 聚合函数选择风险 |
| 20 | COM-02 | config_product_exclusion_range | is_active/excluded_product_sku | C1+C3+C4 | 人工录入+按需+Owner=Steward | Owner=MOMO | 排除范围偏差风险 |
| 21 | COM-02 | partner_tier_rules | priority/partner_code | C1+C3+C4 | 人工录入+按需+三权合一 | Owner=MOMO | 优先级重复或跳号风险 |
| 22 | COM-02 | product_risk_override | target_business_line | C2+C3+C4 | 覆写字段+按需+三权合一 | Owner=MOMO | 覆写错误导致保单归属错误 |
| 23 | COM-02 | config_partner_routing | partner_code_condition | C1+C3+C4 | 人工录入+按需+三权合一 | Owner=MOMO | 通配符规则未定义风险 |

> **合计**：8个中规则信号字段

---

## 五、规则空白地图

> **地图结构**：Section A为VN-PAY-01范围内的规则空白（P0/P1/P2三级）；Section B为超出VN-PAY-01范围的熔断节点或需Mark裁定的补建清单。
> **旧版对照**：每条规则空白标注与旧版EFA005 V1.1的对应关系（继承/升级/新增/删除）

---

### Section A：规则空白（VN-PAY-01范围内）

#### P0级（B=🔴 + D=🔴 + ❌缺口，三项同时成立）

| 优先级 | 关联价值节点 | 关联L4 | 表名 | 规则空白描述 | 空白类型 | 对应五问 | D维度 | 访谈岗位 | 访谈问题草稿 | 调研填充状态 | P0规范化要求 |
|:---:|:---|:---:|:---|:---|:---:|:---:|:---:|:---|:---|:---:|:---|
| P0 | VN-PAY-01 | COM-01 | 佣金准入表→fact_commission_rate | 佣金准入表已被数据表替代但切换规则与历史迁移规则完全未定义；刘敏然明确表示"nobody updates source commission Excel anymore"，但切换时间/迁移范围/回滚方案均无记录 | ❌缺口 | Q2+Q5 | D1+D5 | 刘敏然、Carrie | 「源头佣金表现在是从数据表取还是Excel？切换是什么时间决定的？切换前的历史数据怎么追溯？」<br>「如果ETL脚本出错，还能回滚到原来的Excel吗？」 | ✅已确认（L4-COM-01："nobody updates source commission Excel anymore, now taken from data tables"） | 需明确OCR替代路径 |
| P0 | VN-PAY-01 | COM-02 | 市场佣金表 | 终态表手工调整（MOMO "edits market commission table"）的留痕规则、审批规则与回滚机制缺失；调整原因/差异/审批人全部未记录 | ❌缺口 | Q3+Q5 | D2+D6 | MOMO、Carrie | 「你调整市场佣金表时，会记录改了什么吗？改之前和改之后的差异怎么留痕？」<br>「调整完需要谁审批？有没有审批不通过要回滚的情况？」 | ✅已确认（L4-COM-02："momo edits market commission table using routing rules doc"，未提及留痕/审批） | 需锁定v.final版本号 |
| P0 | VN-PAY-01 | COM-02 | config_partner_routing | 三权合一（Owner=Steward=填写人=momo），路由规则变更缺乏独立复核机制；涉及合规出单的核心规则由单人掌控 | ❌缺口 | Q5 | D6 | momo、Carrie | 「路由规则的变更需要谁审批？有没有独立复核人检查配得对不对？」<br>「有没有出现过路由配错导致出单用了错误牌照的情况？」 | ✅已确认（L4-COM-02：MOMO"edits market commission table using routing rules doc"，无复核记录） | — |
| P0 | VN-PAY-01 | COM-01 | 源头PDF→佣金准入表 | 源头PDF→标准化录入无OCR/验收标准；保司PDF格式不统一（列顺序/列名/日期格式/百分比表示方式各异），Lillian/Joanne/刘敏然手工校验无标准化清单；VN-PAY-01 P0规范化要求未落实 | ❌缺口 | Q1+Q4 | D1+D3 | Lillian、Joanne、刘敏然 | 「保司发来的PDF格式每次一样吗？有没有遇到过格式变了导致录入错误的情况？」<br>「录入完后怎么检查有没有错？有没有检查清单？」 | ❓部分填充（L4-COM-01提及"源头佣金里"从数据表取，但未提及PDF→录入环节的验收标准） | **P0规范化强制要求**：需建立OCR或结构化提取机制；需定义OCR准确率阈值和人工校验清单 |

#### P1级（满足P0三项中的两项）

| 优先级 | 关联价值节点 | 关联L4 | 表名 | 规则空白描述 | 空白类型 | 对应五问 | D维度 | 访谈岗位 | 访谈问题草稿 | 调研填充状态 | P0规范化要求 |
|:---:|:---|:---:|:---|:---|:---:|:---:|:---:|:---|:---|:---:|:---|
| P1 | VN-PAY-01 | COM-01 | fact_commission_rate | ETL责任边界不清：Owner=刘敏然但fyc_rate/ryc_rate由FACT1脚本ETL产出，形成"Owner挂名+ETL实际写入"的责任真空；Owner是否具备排查ETL错误的能力存疑 | ❓潜在 | Q5 | D6 | 刘敏然、Carrie | 「fyc_rate和ryc_rate是系统自动算的还是你手动维护的？如果算出来不对，你能排查出问题在哪吗？」<br>「ETL脚本的公式逻辑你有没有书面确认过？」 | ✅已确认（L4-COM-01：刘敏然明确指认"now taken from data tables"，但未确认Owner对ETL的掌控能力） | — |
| P1 | VN-PAY-01 | COM-02 | 市场佣金表 | 外发版本与内部版本一致性校验缺失：MOMO"edits"后外发，外发前无最终审核，外发版本与内部版本无一致性校验机制 | ❌缺口 | Q3+Q4 | D2+D3 | MOMO、Carrie | 「市场佣金表外发之前，会有人审核吗？审核什么？」<br>「外发的版本和内部留底的版本怎么确保一致？有没有出现过外发错版本的情况？」 | ❓部分填充（L4-COM-02：MOMO"edits"后直接发送，未提及审核） | 需建立版本锁定机制 |
| P1 | VN-PAY-01 | COM-01 | fact_commission_rate | 有效期重叠冲突解决规则缺失：同一产品多条费率记录的有效期若重叠，取最新/取最大/报错的冲突解决规则未定义 | ❌缺口 | Q3 | D2 | 刘敏然、Carrie | 「如果同一个产品有两条费率记录的有效期重叠了，系统怎么处理？取最新的还是报错？」<br>「有没有出现过因为有效期重叠导致佣金算错的情况？」 | ❌未填充 | — |
| P1 | VN-PAY-01 | COM-01 | config_product_commission_formula | 同一产品SKU+合作伙伴在重叠生效日期存在多条公式时的冲突解决规则缺失；首年公式/续期公式的优先级未定义 | ❌缺口 | Q3 | D2 | 刘敏然、Carrie | 「如果同一个产品在不同时间段有两条不同的公式，生效期重叠了怎么处理？」<br>「首年公式和续期公式会不会冲突？有没有边界case？」 | ❌未填充 | — |
| P1 | VN-PAY-01 | COM-01 | agg_source_commission_wide | ETL聚合逻辑（GROUP BY维度、聚合函数选择）缺乏业务方确认与文档化；全部字段Owner/Steward为空 | ❌缺口 | Q3+Q4 | D2+D3 | Carrie、敏然 | 「源头佣金宽表是怎么聚合的？按什么维度GROUP BY？聚合函数是SUM还是MAX？」<br>「这个聚合逻辑有没有书面文档？业务方确认过吗？」 | ❌未填充 | — |
| P1 | VN-PAY-01 | COM-02 | agg_market_commission_tier_rate | 聚合口径（自然月/滚动季度/保单年度）与业绩门槛动态调整规则缺失；全部字段Owner/Steward为空 | ❌缺口 | Q1+Q3 | D1+D2 | Carrie、momo | 「档位佣金表的业绩门槛是按自然月、滚动季度还是保单年度算的？」<br>「门槛值调整时，是只影响新单还是历史单也重算？」 | ❌未填充 | — |
| P1 | VN-PAY-01 | COM-02 | config_partner_routing | 多条件叠加时的匹配优先级仲裁规则未显性定义：6个条件字段（合作伙伴/分类/佣金模式/保司/业务线/产品）叠加时，优先级和fallback规则未文档化 | ❓潜在 | Q3 | D2 | momo、Carrie | 「路由规则有6个条件字段，如果多个条件同时命中，优先级怎么排？」<br>「有没有出现过新类型的合作伙伴在路由表里找不到匹配规则的情况？系统怎么处理的？」 | ❓部分填充（L4-COM-02：MOMO"should read full-tier table first, then manual adjust"，说明存在人工调整但未文档化） | — |
| P1 | VN-PAY-01 | COM-01 | 源头PDF→佣金准入表 | 源头PDF产品命名→内部产品编码标准化映射规则缺失：保司命名与内部命名不一致时无自动校验规则 | ❌缺口 | Q3 | D2 | Lillian、Joanne、刘敏然 | 「保司PDF里的产品名称和我们内部的产品编码是怎么对应的？有没有标准映射表？」<br>「有没有因为产品名称对不上，导致费率匹配错误的情况？」 | ❌未填充 | 需建立标准化映射表 |

#### P2级（满足P0三项中的一项）

| 优先级 | 关联价值节点 | 关联L4 | 表名 | 规则空白描述 | 空白类型 | 对应五问 | D维度 | 访谈岗位 | 访谈问题草稿 | 调研填充状态 | P0规范化要求 |
|:---:|:---|:---:|:---|:---|:---:|:---:|:---:|:---|:---|:---:|:---|
| P2 | VN-PAY-01 | COM-02 | config_commission_table_type | 制表参数变更后下游佣金表重生成触发机制缺失：参数变更后无自动提醒/待办机制，依赖Carrie人工跟踪 | ❌缺口 | Q1+Q4 | D1+D3 | Carrie、momo | 「制表参数改了之后，下游的佣金表会自动重算吗？还是需要手动触发？」<br>「有没有出现过参数改了但佣金表没更新，导致外发错误的情况？」 | ❌未填充 | — |
| P2 | VN-PAY-01 | COM-02 | partner_tier_rules | 档位评定触发周期（按月/按季/按年）与历史追溯规则缺失；档位规则变更时是否触发历史业绩重算及补差规则未定义 | ❌缺口 | Q1+Q3 | D1+D2 | momo、Carrie | 「合作伙伴的档位是按月评定还是按季度？评定后多久生效？」<br>「如果档位规则变了，已发生的业绩会重算补差吗？」 | ❌未填充 | — |
| P2 | VN-PAY-01 | COM-02 | product_risk_override | 覆写规则的自动过期与定期清理机制缺失；覆写规则长期累积将侵蚀默认规则的权威性 | ❌缺口 | Q1+Q3 | D1+D2 | momo、Carrie | 「产品覆写规则设了之后会一直生效吗？有没有自动过期机制？」<br>「多久清理一次过期覆写规则？现在积累了多少条？」 | ❌未填充 | — |
| P2 | VN-PAY-01 | COM-01 | fact_commission_rate | 公式错误检测机制缺失：ETL脚本公式语法通过但计算逻辑错误（如续期公式误用首期系数）无法被程序自动检测 | ❌缺口 | Q3+Q4 | D2+D3 | 刘敏然、Carrie | 「有没有机制能检测ETL公式算出来是否合理？比如续期佣金不应该比首期高？」<br>「历史上有没有出现过公式错误导致批量佣金算错的情况？怎么发现的？」 | ❌未填充 | — |

---

### Section B：熔断节点·补建清单（超出VN-PAY-01范围）

> **说明**：以下熔断节点不属于VN-PAY-01（COM-01+COM-02）范围，但在佣金全链路中位于VN-PAY-01下游或并行位置。直接引用V3.0 Sheet5原文，不计入VN-PAY-01规则空白统计。

| 节点ID | 价值节点 | 关联L4 | 熔断原因 | 致命缺口 | 补建行动 | 与VN-PAY-01关系 |
|:---|:---|:---|:---|:---|:---|:---|
| VN-PAY-04 | 转介费派发确认台账 | COM-13/14/15 | 挂数+落地+追溯三gate全失 | IA合规规则未代码化；银行回执无统一归档 | Mark裁定IA规则代码化负责人；新增L4-COM-14/15 | 下游：VN-PAY-01产出供VN-PAY-04消费 |
| VN-PAY-06 | 理财师综合应派计算清单 | FPG-01~05 | 挂数+追溯gate失败 | 四类协议参数未中心化；人工合并易错 | 建dim_agreement_param维度表；Mark裁定FPG-05归属 | 下游：VN-PAY-01的佣金数据供综合应派使用 |
| VN-PAY-09 | NGM→Apass→宿安→天领体系外对账表 | 未建L3/L4 | 挂数+落地+追溯三gate全失 | BP V2完全缺失；37.2M HKD体系外资金零fact表覆盖 | Mark+Carrie联合裁定：归口部门/建表/L3L4补建 | 并行：体系外资金未纳入VN-PAY-01佣金链路 |

---

## 六、版本对比：旧版EFA005 V1.1 → 新版EFA005-V2

### 对比说明

| 对比维度 | 旧版EFA005 V1.1 | 新版EFA005-V2 | 变化 |
|:---|:---|:---|:---|
| **分析视角** | 12张数据表（表视角） | VN-PAY-01价值节点（COM-01+COM-02） | 视角收窄 |
| **规则空白总数** | 35条（P0×8/P1×16/P2×11） | 16条（P0×4/P1×8/P2×4） | -19条（视角收窄） |
| **涉及数据表** | 12张表+反向构建2张 | 12张表（聚焦VN-PAY-01数据流） | 相同表，不同组织方式 |
| **编号体系** | EFA-P0-001~P0-008等 | EFA-P0-001~P0-004等 | 延续EFA命名 |
| **P0规范化要求** | 无 | VN-PAY-01 P0规范化要求标注 | 新增 |
| **熔断节点** | 无单独Section B | 新增Section B（3个下游熔断节点） | 新增 |

### 规则空白对照表

| 新版编号 | 优先级 | 规则主题 | 旧版编号 | 对照关系 | 变化说明 |
|:---|:---:|:---|:---|:---:|:---|
| EFA-P0-001 | P0 | 佣金准入表→数据表切换规则缺失 | EFA-P0-004 | 继承 | 视角收窄，保留核心缺口 |
| EFA-P0-002 | P0 | 市场佣金表手工调整留痕/审批缺失 | EFA-P0-006 | 继承 | 视角收窄，保留核心缺口 |
| EFA-P0-003 | P0 | config_partner_routing三权合一+无复核 | EFA-P0-001 | 继承 | 视角收窄，保留核心缺口 |
| EFA-P0-004 | P0 | 源头PDF→标准化录入无OCR/验收标准 | — | **新增** | VN-PAY-01 P0规范化要求衍生 |
| EFA-P1-001 | P1 | fact_commission_rate ETL责任边界不清 | EFA-P0-008 | **降级** | 旧版P0→新版P1（数据表已替代，责任真空降为潜在风险） |
| EFA-P1-002 | P1 | 市场佣金表外发版本一致性校验缺失 | EFA-P1-008 | 继承 | 视角收窄，保留 |
| EFA-P1-003 | P1 | fact_commission_rate有效期重叠冲突解决 | EFA-P1-002 | 继承 | 视角收窄，保留 |
| EFA-P1-004 | P1 | config_product_commission_formula冲突解决 | EFA-P1-015 | 继承 | 视角收窄，保留 |
| EFA-P1-005 | P1 | agg_source_commission_wide聚合逻辑未确认 | EFA-P1-011 | 继承 | 视角收窄，保留 |
| EFA-P1-006 | P1 | agg_market_commission_tier_rate聚合口径缺失 | EFA-P1-013 | 继承 | 视角收窄，保留 |
| EFA-P1-007 | P1 | config_partner_routing匹配优先级仲裁缺失 | EFA-P0-002 | **降级** | 旧版P0→新版P1（三权合一已单独列为P0-003，优先级问题降为P1） |
| EFA-P1-008 | P1 | 源头PDF产品命名→内部编码映射缺失 | — | **新增** | FIN001-V2 VN-PAY-01分析交叉引入 |
| EFA-P2-001 | P2 | config_commission_table_type变更触发缺失 | EFA-P1-014 | **降级** | 旧版P1→新版P2（B标签责任模式非🔴，只满足D🟢+❌一项） |
| EFA-P2-002 | P2 | partner_tier_rules档位周期与追溯缺失 | EFA-P2-004 | 继承 | 视角收窄，保留 |
| EFA-P2-003 | P2 | product_risk_override覆写过期机制缺失 | EFA-P2-006 | 继承 | 视角收窄，保留 |
| EFA-P2-004 | P2 | fact_commission_rate公式错误检测缺失 | EFA-P2-009 | 继承 | 视角收窄，保留 |

### 旧版删除/移出VN-PAY-01的规则空白

| 旧版编号 | 旧版优先级 | 规则主题 | 移出原因 |
|:---|:---:|:---|:---|
| EFA-P0-003 | P0 | 佣金准入表Sheet1/Sheet2缺失 | 视角收窄：元数据缺口问题在价值节点视角下归入COM-01数据治理，不单独列为规则空白 |
| EFA-P0-005 | P0 | 市场佣金表Sheet1/Sheet2缺失 | 视角收窄：同上，元数据缺口不单独列 |
| EFA-P0-007 | P0 | fact_commission_rate Sheet1缺失 | 视角收窄：元数据缺口不单独列 |
| EFA-P1-001 | P1 | fact_commission_rate三费率互斥 | 视角收窄：basic/extra/smpa三费率在fact_commission_rate层面已ETL计算，互斥规则由准入表控制，非VN-PAY-01核心 |
| EFA-P1-003 | P1 | config_license_carrier_mapping授权联动 | 视角收窄：更偏向合规配置管理，非VN-PAY-01核心产出链 |
| EFA-P1-004 | P1 | config_license_carrier_mapping版本切换 | 视角收窄：同上 |
| EFA-P1-005 | P1 | 佣金准入表BASIC/EXTRA/SMPA互斥 | 视角收窄：准入表层面规则，VN-PAY-01聚焦"已准入后的产出链" |
| EFA-P1-006 | P1 | 佣金准入表档位一致性 | 视角收窄：同上 |
| EFA-P1-007 | P1 | 佣金准入表年度衰减 | 视角收窄：同上 |
| EFA-P1-009 | P1 | 市场佣金表制表类型一致性 | 视角收窄：与P1-002合并（外发版本一致性已覆盖） |
| EFA-P1-010 | P1 | agg_source_commission_wide Owner空 | 视角收窄：元数据Owner空缺归入P1-005聚合逻辑未确认 |
| EFA-P1-012 | P1 | agg_market_commission_tier_rate Owner空 | 视角收窄：元数据Owner空缺归入P1-006聚合口径缺失 |
| EFA-P1-016 | P1 | config_product_commission_formula变更触发 | 视角收窄：与P1-004合并（冲突解决已涵盖变更场景） |
| EFA-P2-001 | P2 | config_commission_table_type默认兜底 | 视角收窄：非核心产出链风险 |
| EFA-P2-002 | P2 | config_product_exclusion_range优先级 | 视角收窄：非核心产出链风险 |
| EFA-P2-003 | P2 | config_product_exclusion_range继承规则 | 视角收窄：非核心产出链风险 |
| EFA-P2-005 | P2 | partner_tier_rules变更重算 | 视角收窄：与P2-002合并 |
| EFA-P2-007 | P2 | product_risk_override冲突检测 | 视角收窄：非核心产出链风险 |
| EFA-P2-008 | P2 | config_partner_routing fallback | 视角收窄：与P1-007合并 |
| EFA-P2-010 | P2 | agg_source_commission_wide去重 | 视角收窄：归入P1-005聚合逻辑 |
| EFA-P2-011 | P2 | agg_market_commission_tier_rate四舍五入 | 视角收窄：归入P1-006聚合口径 |

> **删除规则**：旧版35条中，16条保留/继承，2条新增，2条降级，15条移出（视角收窄或合并）。保留率=51%（18/35），符合价值节点视角收窄的预期。

---

## 七、附加观察（超出VN-PAY-01范围，不纳入规则空白地图）

1. **dim_product_id / dim_product_sku 的引用关系**：
   - VN-PAY-01的COM-02（Agg2步骤二）会查询dim_product_sku获取产品属性，但这两张表属于产品域，不在VN-PAY-01直接产出链上。
   - 观察：product_risk_override覆写规则与dim_product_sku默认值的优先级未在VN-PAY-01内分析，属于跨域规则空白，建议在产品域分析中覆盖。

2. **VN-PAY-01与下游节点的交接断点**：
   - VN-PAY-01产出《市场佣金表》供VN-PAY-02（对账）和VN-PAY-03（应派）消费，但交接验收标准未定义。
   - 此断点位于VN-PAY-01终点Z之后，不属于VN-PAY-01范围，建议在对账/应派节点分析中覆盖。

3. **L4-COM-03（佣金外发凭证）缺失**：
   - L4交付物调研序号3显示"目前没有"佣金外发凭证，"应该有，因为每次追溯都要去查邮件很麻烦"。
   - 此缺失属于COM-02产出后的交付物管理问题，建议纳入COM-02访谈覆盖。

---

## 八、自检声明

**第一层产出质量检查清单**：

- [x] VN-PAY-01分析框架已输出（起点A/终点Z/L4范围/涉及数据表/P0规范化要求）
- [x] VN-PAY-01四标签分析完整（A/B/C/D标签+Gate状态+规则空白贡献）
- [x] B标签有字段级分析（单点责任字段、C1-C5信号清单）
- [x] 字段级规则信号清单命中C1-C5条件，跨表汇总完整（15高+8中）
- [x] 规则空白地图有P0/P1/P2优先级、访谈问题草稿、调研填充状态、P0规范化要求标注
- [x] Section B熔断节点补建清单已输出（3个下游熔断节点）
- [x] 新旧版对比说明已输出（对照表+删除说明）
- [x] 规则空白编号使用EFA-P0/P1/P2格式
- [x] 每条规则空白标注「与旧版EFA005对照」
- [x] 附加观察已记录（3条，不纳入正文）

**两两比对唯一性检查**：

> **已执行两两比对唯一性检查**：
> - Section A共 **16条** 规则空白（P0级4条 / P1级8条 / P2级4条），经两两比对，**0组重复**
> - Section B共 **3个** 熔断节点，引用V3.0原文，未做重新分析
> - 附加观察3条，与节点内规则空白无重复

**集群风险识别**：

- **条件A检查**：同一岗位归口P0级空白≥2条且对应表数≥3张 → **命中**：MOMO岗位归口P0级空白2条（EFA-P0-002市场佣金表留痕、EFA-P0-003 config_partner_routing三权合一），涉及表数≥3张 → **标记为集群风险**
- **条件B检查**：C4信号命中字段数≥20个且集中在同一域/同一Owner → 未命中（C4信号命中6条，未达阈值）

**裁定摘要（VN-PAY-01特有规则）**：

```
情景：路径A+B融合（情景3），价值节点视角
P0判断特殊规则：
  ① VN-PAY-01 P0规范化要求（源头PDF→OCR/标准化录入）→ 自动衍生1条P0（EFA-P0-004）
  ② MOMO集群：凡由MOMO单人执行+无复核的配置表→ B标签🔴（已识别2条P0：EFA-P0-002/003）
  ③ 数据表替代过渡期：佣金准入表→fact_commission_rate的切换规则缺失→ B🔴+D🔴+❌→ P0（EFA-P0-001）
已知边界case：
  - 佣金准入表已"taken from data tables"，原47字段Excel录入流程已废弃
  - 市场佣金表由MOMO"edits"后直接外发，无留痕/审批/版本锁定
  - config_partner_routing和partner_tier_rules存在三权合一（Owner=Steward=填写人=momo）
待确认问题处理：旧版35条中16条保留/2条新增/2条降级/15条移出（视角收窄）
表名一致性：14张表数据字典与旧版EFA005一致，无重大不一致
调研覆盖说明：P4填充范围限定于L3-COM序号1-13（COM-01/02已逐条交叉比对）
```

---

*任务包：TASK-M4W10-019 | 执行终端：Kimi | 授权：Jasper*
*生成时间：2026-05-28*
*版本：V1.0（EFA005-V2第一层产出，VN-PAY-01视角）*

