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

# EFA-005 · 单表标签卡（14张表）v1.0

> 任务编号：TASK-EFA-005 | 执行依据：数据规则提取方法论_三层递进提取法_v2.1
> 生成时间：2026-05-18

---

## 表1：【产品SKU列表】/ DIM_PRODUCT_SKU
所属域：产品与供应域 | 表类型：维度表 | 字段数：20 | 审核状态：待审核 | 数据链段：第一段·源头佣金生成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 维度表

**A-类型规则风险：** 维度表天然存在「编码规则一致性」与「生命周期管理」规则风险。主数据变更时若缺乏跨系统同步机制，下游所有关联表的口径将同时分裂。

**A-本表信号字段：**
- Product_SKU（产品大类代码）— 维度主键，编码规则变更或重复将直接导致下游事实表关联失败
- Business_Line（所属业务线分类）— 枚举值字段，缺乏与DIM_SEGMENTATION联动校验，人工录入可能出现自定义值
- Is_Offshore（离岸标识）— 若与产品实际属性不一致，将导致佣金计算适用错误税率/规则

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=李思齐 / 填写人=Mia / Owner=产品专员 / Steward=Mia

**B-责任模式：** Owner分离 🟢 + 判断理由：填写人(Mia)≠分工(李思齐)，Owner=产品专员，有明确分工但缺乏交接标准定义

**B-单点责任字段：**
- Product_SKU（产品大类代码）— Owner=产品专员，维度主键错误将级联影响所有下游关联计算
- Carrier_Code（保司代码）— Owner=产品专员，错误将导致佣金事实表无法正确关联保司维度

**B-字段级规则信号：**
- C1命中（数据来源=人工录入 且 非空=是）：Update_Date、Product_SKU、Chinese_Standard_Name、English_Standard_Name、Business_Line、Is_Offshore
- C2命中（计算口径含手工录入）：product_Unite_Grid、Product_Risk_Level
- C3命中（更新频率=按需/规则变更）：Update_Date、Product_SKU、Carrier_Code、Chinese_Standard_Name、English_Standard_Name、Product_Category、Product_Type、Business_Line、product_Unite_Grid、Is_Offshore、Is_Premium_Financing、Clawback_Period_Months、Cooling_Off_Days、Currency_Link_Rule、Product_Risk_Level
- C4命中（Owner=Steward）：无
- C5命中（质量规则含ALL/枚举值）：Product_Category、Product_Type、Business_Line

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：佣金准入表→佣金事实表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测Product_SKU在下游事实表中被引用（FK关联性正确），但无法检测「Product_SKU关联了错误Product_ID」或「Business_Line填写了自定义值而非标准枚举」。例如SKU=PRD001实际属于BRK业务线但填写为KA，程序验证通过，下游佣金按KA口径计算导致财务偏差。

### D · 商业职能与授权
**D-职能定义：** 商业建模与结构定型 → 授权级别：🟢 中

**D-审核状态匹配：** 匹配 — 中授权级别+待审核，处于标准审核流程中

**D-合规风险：** 中 — 产品主数据错误将级联影响所有下游佣金计算，但当前Owner明确

### 规则空白汇总
⚠️ Product_SKU与Product_ID映射关系变更时缺乏跨表一致性校验规则 → 五问：Q3 → 评分维度：D2
⚠️ Business_Line字段枚举值缺乏与DIM_SEGMENTATION的联动校验，人工录入可能出现自定义值 → 五问：Q4 → 评分维度：D1

---

## 表2：【产品ID列表】/ DIM_PRODUCT_ID
所属域：产品与供应域 | 表类型：维度表 | 字段数：16 | 审核状态：待审核 | 数据链段：第一段·源头佣金生成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 维度表

**A-类型规则风险：** 维度表天然存在「跨系统编码一致性」与「版本管理」规则风险。Product_ID作为全局唯一标识，若版本升级规则不清晰，将直接导致历史保单与新产品映射混乱。

**A-本表信号字段：**
- Product_ID（产品ID）— 全局唯一标识，若与Product_SKU映射关系错误，将直接导致佣金事实表product_id关联失败
- Rate_Option_Code（特殊折扣）— 枚举值字段，缺乏与DIM_LOOKUP_CODE联动校验，可能出现自定义编码
- Is_Active（上架状态）— 状态流转规则（Draft→上架→下架）若未定义，将导致已下架产品仍参与佣金计算

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=李思齐 / 填写人=Mia / Owner=产品专员 / Steward=Mia

**B-责任模式：** Owner分离 🟢 + 判断理由：填写人(Mia)≠分工(李思齐)，Owner=产品专员，有明确分工但缺乏交接标准定义

**B-单点责任字段：**
- Product_ID（产品ID）— Owner=产品专员，全局唯一标识错误将级联影响所有下游事实表关联
- Product_SKU（所属大类外键）— Owner=产品专员，外键错误将导致产品ID归属错误的产品大类

**B-字段级规则信号：**
- C1命中：Update_Date、Product_ID_SK、Product_ID
- C2命中：Product_ID、Chinese_Product_Name、English_Product_Name、Rate_Option_Code、Premium_Term、Benefit_Term、Product_Risk_Level
- C3命中：Update_Date、Product_ID_SK、Product_ID、Product_SKU、Chinese_Product_Name、English_Product_Name、Rate_Option_Code、Premium_Term、Benefit_Term、Is_Active、Product_Risk_Level
- C4命中：无
- C5命中：无

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：佣金准入表→佣金事实表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测Product_ID在下游事实表中被引用，但无法检测「同一Product_ID错误关联了不同保司的产品」或「版本号未按实际产品变更升级」。例如产品A升级后版本号仍为V1，但产品B已使用V2公式计算佣金，程序验证通过，历史保单佣金计算口径不一致。

### D · 商业职能与授权
**D-职能定义：** 商业建模与结构定型 → 授权级别：🟢 中

**D-审核状态匹配：** 匹配 — 中授权级别+待审核，处于标准审核流程中

**D-合规风险：** 中 — 产品ID体系错误将直接导致跨系统识别失败，但当前Owner明确

### 规则空白汇总
⚠️ Product_ID版本升级触发条件与审批链路未定义 → 五问：Q1/Q3 → 评分维度：D2
⚠️ Rate_Option_Code枚举值域缺乏与DIM_LOOKUP_CODE的联动校验 → 五问：Q4 → 评分维度：D1

---

## 表3：【佣金准入表】/ 佣金准入表
所属域：— | 表类型：过程表 | 字段数：— | 审核状态：审核通过 | 数据链段：第一段·源头佣金生成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 过程表

**A-类型规则风险：** 过程表天然存在「流程节点状态转换」与「输入输出完整性」规则风险。作为佣金数据链起点，准入判断标准、准入失败回退机制若缺失，将直接导致数据断流或错误准入。

**A-本表信号字段：**
- ⛔字段待补充 — Sheet2字段级信息缺失，无法识别具体信号字段，访谈优先

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=刘敏然 / 填写人=刘敏然 / Owner=— / Steward=—

**B-责任模式：** 自填自审 🔴 + 判断理由：⛔字段待补充，无法判断字段级责任。仅从Sheet1看，分工=填写人=刘敏然，且审核已通过，存在自填自审风险。

**B-单点责任字段：**
- ⛔字段待补充，访谈优先

**B-字段级规则信号：**
- C1命中：⛔字段待补充
- C2命中：⛔字段待补充
- C3命中：⛔字段待补充
- C4命中：⛔字段待补充
- C5命中：⛔字段待补充

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：佣金准入表→佣金事实表

**C-在链位置：** 源头

**C-验证盲区：** 语义错误 — 验证路径仅能检测准入记录是否正确流入事实表，但无法检测「不应准入的产品被错误准入」或「准入条件临时变更未留痕」。例如某产品因合规问题应被排除，但准入表中无排除标记，程序验证通过，该产品进入佣金计算链。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义，无法评估匹配度）— 商业职能定义为空但审核状态为「审核通过」，存在「无授权依据却已通过」的悖论

**D-合规风险：** 高 — 字段信息待补充，规则黑盒风险极高，需优先访谈澄清

### 规则空白汇总
⚠️ ⛔字段待补充，访谈优先：准入判断的业务标准完全缺失 → 五问：Q3 → 评分维度：D2
⚠️ ⛔字段待补充，访谈优先：准入节点的Data Owner与审批链路未定义 → 五问：Q5 → 评分维度：D6

---

## 表4：【产品佣金计算公式】/ CONFIG_PRODUCT_COMMISSION_FORMULA
所属域：费率确认域 | 表类型：参数表 | 字段数：13 | 审核状态：审核通过 | 数据链段：第一段·源头佣金生成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 参数表

**A-类型规则风险：** 参数表天然存在「变更审批」「生效冲突检测」与「版本回滚」规则风险。本表存储佣金计算公式，直接影响财务支出，重叠生效日期时的冲突解决规则可能缺失。

**A-本表信号字段：**
- first_year_formula（首年佣金公式）— 公式字段，语法正确但计算逻辑错误无法被程序检测，如引用不存在字段或系数错误
- renewal_year_formula（续期佣金公式）— 同上，续期公式错误将长期影响财务支出
- basic_rate_from（Basic取值来源）— 取值来源字段，若与实际保司协议不一致，将导致佣金率基础值错误

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=刘敏然 / 填写人=刘敏然 / Owner=刘敏然 / Steward=MOMO

**B-责任模式：** Owner分离 🟢 + 判断理由：分工=刘敏然，填写人=刘敏然，Owner=刘敏然，Steward=MOMO。Owner与Steward分离，但填写人与Owner为同一人，需关注修改后Steward是否实际复核。

**B-单点责任字段：**
- first_year_formula（首年佣金公式）— Owner=刘敏然，公式错误将直接造成首期佣金财务偏差
- renewal_year_formula（续期佣金公式）— Owner=刘敏然，续期公式错误将长期影响财务支出
- basic_rate_from（Basic取值来源）— Owner=刘敏然，取值来源错误将导致基础佣金率偏差

**B-字段级规则信号：**
- C1命中：无
- C2命中：first_year_formula、renewal_year_formula、basic_rate_from、extra_rate_from、smpa_rate_from
- C3命中：Carrier、license_type、customer_type、first_year_formula、renewal_year_formula、basic_rate_from、extra_rate_from、smpa_rate_from
- C4命中：无
- C5命中：license_type

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：佣金准入表→佣金事实表

**C-在链位置：** 中间

**C-验证盲区：** 公式错误 — 程序验证可检测公式配置是否成功写入并向下游流转，但无法检测「公式逻辑本身是否数学正确」。例如续期公式中错误引用了首期系数（first_year_rate替代renewal_rate），公式语法通过，程序验证通过，但所有续期佣金将按首期比例计算，造成大额财务偏差。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义，无法评估匹配度）— 无商业职能定义但审核已通过；作为直接影响财务支出的参数表，缺乏高授权级别标注是重大规则空白

**D-合规风险：** 高 — 公式直接影响财务支出，但缺乏高授权级别和冲突检测机制

### 规则空白汇总
⚠️ 同一产品SKU+合作伙伴在重叠生效日期存在多条公式时的冲突解决规则缺失 → 五问：Q3 → 评分维度：D2
⚠️ 公式变更后的下游佣金重算触发机制缺失 → 五问：Q1/Q5 → 评分维度：D3

---

## 表5：【牌照保司路由】/ CONFIG_LICENSE_CARRIER_MAPPING
所属域：费率确认域 | 表类型：参数表 | 字段数：13 | 审核状态：审核通过 | 数据链段：第一段·源头佣金生成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 参数表

**A-类型规则风险：** 参数表天然存在「授权时效性」与「合规边界」规则风险。本表定义牌照与保司的授权映射，直接关系到平台出单合法性，授权状态与生效日期的联动规则若缺失，易出现无照经营。

**A-本表信号字段：**
- License_Code（牌照代码）— 授权映射主键，若与已过期牌照关联，将直接导致无照经营风险
- Is_Active（是否有效）— 开关字段，若与Effective_To到期日未联动，授权过期后仍可能出单
- Effective_From/To（有效期从/至）— 有效期字段，重叠有效期时缺乏冲突检测机制

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=刘敏然 / 填写人=Momo / Owner=刘敏然 / Steward=MOMO

**B-责任模式：** 交接模糊 🟡 + 判断理由：分工=刘敏然，填写人=Momo，Owner=刘敏然，Steward=MOMO。数据分工与填写人不一致，存在交接，但交接标准（Momo的修改权限范围、刘敏然的复核触发条件）未定义。

**B-单点责任字段：**
- License_Code（牌照代码）— Owner=刘敏然，错误映射将直接导致无照经营
- Is_Active（是否有效）— Owner=刘敏然，授权开关误操作将直接阻断或错误开放出单

**B-字段级规则信号：**
- C1命中：无
- C2命中：commission_plan_code、Last_Updated_By、Remarks
- C3命中：License_Code、Carrier_Code、commission_plan_code、Effective_From、Effective_To、Is_Active、Last_Updated_By、Remarks
- C4命中：无
- C5命中：无

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：佣金准入表→佣金事实表

**C-在链位置：** 中间

**C-验证盲区：** 状态错误 — 程序验证可检测映射记录是否流入佣金事实表，但无法检测「授权状态=有效但保司资质已过期」。例如某保司资质已于2025-12-31到期，但Is_Active仍为1且Effective_To填写为2026-06-30，程序验证通过，后续出单将使用该已失效保司，造成无照经营。

### D · 商业职能与授权
**D-职能定义：** 准入确权与交付授权 → 授权级别：🔴 高

**D-审核状态匹配：** 匹配 — 高授权级别且已审核通过，当前状态与授权级别匹配。但需关注审核通过后变更是否触发二次审核

**D-合规风险：** 高 — 涉及准入确权，规则缺失将直接导致业务违规或财务损失

### 规则空白汇总
⚠️ 授权状态与保司资质有效期的自动化联动规则缺失 → 五问：Q3/Q4 → 评分维度：D4
⚠️ 同一牌照映射不同保司的版本切换规则与回滚机制缺失 → 五问：Q3/Q5 → 评分维度：D5

---

## 表6：【佣金事实表】/ FACT_COMMISSIOM_RATE
所属域：费率确认域 | 表类型：事实表 | 字段数：36 | 审核状态：— | 数据链段：第一段·源头佣金生成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 事实表

**A-类型规则风险：** 事实表天然存在「数据来源溯源」「计算口径一致性」与「时效性」规则风险。Sheet1缺失导致责任归属不清，计算规则版本标记与批次追踪若缺失，佣金差异将无法追溯。

**A-本表信号字段：**
- basic_rate（Basic佣金率）— 计算字段，ETL生成但缺乏计算版本标记，无法追溯用哪个版本的公式计算
- extra_rate（Extra佣金率）— 同上，多个费率字段同时存在时优先级规则可能模糊
- product_sku（产品SKU）— FK关联字段，若关联维度表错误SKU，将导致整笔佣金计算错误

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=—（Sheet1缺失） / 填写人=—（Sheet1缺失） / Owner=刘敏然 / Steward=MOMO

**B-责任模式：** 治理真空 🔴 + 判断理由：Sheet1无此表记录（数据分工/填写人/审核状态均缺失），Sheet2显示Owner=刘敏然/Steward=MOMO，但CSV显示该表为ETL计算产出，字段级Owner标记为刘敏然，ETL生成字段与人工维护字段的责任边界不清。

**B-单点责任字段：**
- basic_rate（Basic佣金率）— Owner=刘敏然，但ETL计算逻辑若出错，Owner是否具备排查能力存疑
- extra_rate（Extra佣金率）— 同上，直接影响佣金金额

**B-字段级规则信号：**
- C1命中：effective_start_date、effective_end_date
- C2命中：无
- C3命中：无
- C4命中：无
- C5命中：license_type、customer_type、tier_code、issue_cutoff_date

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：佣金准入表→佣金事实表（基于CSV推断）

**C-在链位置：** 中间

**C-验证盲区：** 公式错误 — 程序验证可检测数据是否从上游完整流入，但无法检测「公式应用错误」。例如应使用产品A（SKU=PRD001）的公式计算，但ETL逻辑错误匹配了产品B（SKU=PRD002）的公式，所有字段非空/格式均通过，程序验证通过，但整批保单佣金金额全部错误。

### D · 商业职能与授权
**D-职能定义：** 准入确权与交付授权（基于CSV推断） → 授权级别：🔴 高

**D-审核状态匹配：** 缺失（Sheet1无记录，审核状态未知）— 作为核心财务事实表，缺乏表级审核状态跟踪是重大治理缺口

**D-合规风险：** 高 — 佣金事实表涉及财务结算，数据错误直接影响付款准确性与合规审计

### 规则空白汇总
⚠️ Sheet1缺失导致表级责任归属与审核状态完全空白 → 五问：Q5 → 评分维度：D6
⚠️ basic_rate/extra_rate/smpa_rate同时存在时的优先级与互斥规则未显性定义 → 五问：Q3 → 评分维度：D2

---

## 表7：【源头佣金宽表】/ AGG_SOURCE_COMMISSION_WIDE
所属域：费率确认域 | 表类型：聚合表 | 字段数：15 | 审核状态：审核通过 | 数据链段：第一段·源头佣金生成

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 聚合表

**A-类型规则风险：** 聚合表天然存在「ETL计算逻辑透明性」「维度一致性」与「回滚机制」规则风险。所有字段Owner/Steward为空，聚合规则缺乏责任人，业务方无法对聚合口径负责。

**A-本表信号字段：**
- commission_plan_code（佣金计划代码）— ETL聚合字段，Owner为空，聚合逻辑（GROUP BY键选择）错误将级联影响下游
- fyc_rate（FYC佣金率）— 聚合字段，若聚合函数选择错误（如SUM而非MAX），将导致费率失真
- effective_start_date（生效起始日）— 时间维度键，若ETL窗口逻辑错误，将遗漏或重复聚合数据

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=刘敏然 / 填写人=敏然 / Owner=无 / Steward=无

**B-责任模式：** 治理真空 🔴 + 判断理由：分工=刘敏然，填写人=敏然，但全部字段Owner/Steward为空。聚合逻辑完全由ETL工程师隐式维护，业务方无法对聚合口径负责。

**B-单点责任字段：**
- commission_plan_code（佣金计划代码）— Owner为空，聚合键错误将导致下游市场档位佣金计算基础错误
- fyc_rate（FYC佣金率）— Owner为空，聚合函数选择错误将直接导致费率失真

**B-字段级规则信号：**
- C1命中：无
- C2命中：无
- C3命中：无
- C4命中：无
- C5命中：无

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：佣金事实表→源头佣金宽表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测佣金事实表是否成功聚合到宽表，但无法检测「同一保单被重复聚合（GROUP BY键不唯一）」。例如commission_plan_code+license_code组合本应唯一，但ETL逻辑中未去重，同一保单被聚合两次，fyc_rate被双倍计算，程序验证通过，下游档位佣金全部偏高。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义）— 无商业职能定义但已审核通过；作为ETL聚合产出，审核标准不明确

**D-合规风险：** 中 — 聚合表数据用于决策与对账，ETL逻辑不透明将导致汇总偏差难以追溯

### 规则空白汇总
⚠️ ETL聚合逻辑（GROUP BY维度、聚合函数选择）缺乏业务方确认与文档化 → 五问：Q3/Q4 → 评分维度：D3
⚠️ 全部字段Owner/Steward为空，聚合口径偏差时无责任主体可追溯 → 五问：Q5 → 评分维度：D6

---

## 表8：【合作伙伴保司牌照路由规则】/ CONFIG_PARTNER_ROUTING
所属域：核心交易域 | 表类型：参数表 | 字段数：16 | 审核状态：待审核 | 数据链段：第二段·市场档位拆解

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 参数表

**A-类型规则风险：** 参数表天然存在「条件组合冲突」与「优先级仲裁」规则风险。多条件叠加时的匹配优先级若未定义，将导致出单牌照分配结果不可预期。

**A-本表信号字段：**
- priority（优先级）— 核心仲裁字段，数值重复或逻辑错误将导致大规模出单错误
- Assigned_license_code（分配牌照编码）— 路由结果字段，若指向已失效牌照，将直接导致无照经营
- Partner_code_Condition（合作伙伴编码条件）— 条件字段，空值或通配符规则未定义时，边界case无法覆盖

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=Carrie / 填写人=momo / Owner=MOMO / Steward=MOMO

**B-责任模式：** 三权合一 🔴 + 判断理由：Owner=MOMO、Steward=MOMO、填写人=momo（同一人）。路由规则涉及合规出单，单一人员掌控全部责任是重大内控缺口。

**B-单点责任字段：**
- priority（优先级）— Owner=MOMO/Steward=MOMO/填写人=momo，三权合一，误改将直接导致大规模出单错误
- Assigned_license_code（分配牌照编码）— 同上，单点责任且无独立复核

**B-字段级规则信号：**
- C1命中：Routing_rules_ID、priority、Partner_code_Condition、Partner_Category_Condition、Commission_Pattern、carrier_code_Condition、Bussiness_Line_comdition、Product_Condition、Assigned_license_code、Is_Active
- C2命中：无
- C3命中：Routing_rules_ID、priority、Partner_code_Condition、Partner_Category_Condition、Commission_Pattern、carrier_code_Condition、Bussiness_Line_comdition、Product_Condition、Assigned_license_code、Is_Active、remark
- C4命中：Routing_rules_ID、priority、Partner_code_Condition、Partner_Category_Condition、Commission_Pattern、carrier_code_Condition、Bussiness_Line_comdition、Product_Condition、Assigned_license_code、Is_Active、remark
- C5命中：Partner_code_Condition、Partner_Category_Condition、Commission_Pattern、carrier_code_Condition、Bussiness_Line_comdition、Product_Condition

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：源头佣金宽表→市场档位佣金表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测路由配置是否被下游引用，但无法检测「条件组合存在逻辑漏洞」。例如某类合作伙伴（如新签约的独立代理人）在路由表中无任何匹配规则，系统fallback逻辑未定义，可能随机分配牌照或报错，但程序验证仅检查配置存在性，不检查覆盖完备性。

### D · 商业职能与授权
**D-职能定义：** 管理宪法与合规红线 → 授权级别：🔴 最高

**D-审核状态匹配：** ❌严重不匹配 — 最高授权级别但处于「待审核」，直接影响合规出单的核心规则尚未完成最终确认

**D-合规风险：** 高 — 涉及合规红线，规则缺失将直接导致业务违规

### 规则空白汇总
⚠️ 多条件叠加时的匹配优先级仲裁规则未显性定义 → 五问：Q3 → 评分维度：D2
⚠️ Owner/Steward/填写人三者为同一人，路由规则变更缺乏独立复核机制 → 五问：Q5 → 评分维度：D6

---

## 表9：【产品属性覆写路由】/ Product_Risk_Override
所属域：费率确认域 | 表类型：参数表 | 字段数：13 | 审核状态：待审核 | 数据链段：第二段·市场档位拆解

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 参数表

**A-类型规则风险：** 参数表天然存在「例外规则的累积效应」与「默认规则的侵蚀」规则风险。覆写规则若缺乏自动过期机制，将逐渐侵蚀默认规则的权威性。

**A-本表信号字段：**
- Target_Business_Line（目标产品线）— 覆写结果字段，若目标业务线本身已被排除在佣金计算范围外，将形成循环依赖
- Mapped_Business_Line（原始产品线）— 被覆写字段，覆写前后映射关系若未留痕，将导致审计无法追溯
- Product_SKU（产品SKU）— 覆写对象字段，多条覆写规则针对同一SKU时的优先级未定义

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=Carrie / 填写人=momo / Owner=MOMO / Steward=MOMO

**B-责任模式：** 三权合一 🔴 + 判断理由：Owner=MOMO、Steward=MOMO、填写人=momo（同一人）。覆写规则涉及产品风控，单一人员决策缺乏制衡。

**B-单点责任字段：**
- Target_Business_Line（目标产品线）— Owner=MOMO/Steward=MOMO/填写人=momo，三权合一，覆写错误将直接导致保单归属错误
- Mapped_Business_Line（原始产品线）— 同上，覆写前后映射关系无独立复核

**B-字段级规则信号：**
- C1命中：无
- C2命中：Target_Business_Line
- C3命中：Product_SKU、Product_ID、Rate_Option_Code、Mapped_Business_Line、Target_Business_Line、Mapped_PUG、Target_PUG、remark
- C4命中：Product_SKU、Product_ID、Rate_Option_Code、Mapped_Business_Line、Target_Business_Line、Mapped_PUG、Target_PUG、remark
- C5命中：Product_ID、Mapped_Business_Line

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：源头佣金宽表→市场档位佣金表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测覆写记录是否进入下游计算，但无法检测「覆写规则与默认规则形成循环依赖」。例如Product_SKU=PRD001的默认Business_Line=BRK，覆写规则将其改为KA，但KA业务线在该产品的佣金公式配置中已被排除（CONFIG_PRODUCT_EXCLUSION_RANGE），导致该SKU进入佣金计算后又被排除，产生空结果，程序验证通过但业务逻辑断裂。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义）— 无商业职能定义，处于「待审核」；作为风控例外规则，缺乏高授权级别标注

**D-合规风险：** 中 — 参数配置错误可能向下游传导，需关注生效规则与冲突检测机制

### 规则空白汇总
⚠️ 覆写规则的自动过期与定期清理机制缺失 → 五问：Q1/Q3 → 评分维度：D2
⚠️ 多条覆写规则针对同一产品SKU时的优先级与冲突检测规则缺失 → 五问：Q3 → 评分维度：D2

---

## 表10：【合作伙伴档位佣金规则】/ Partner_Tier_Rules
所属域：费率确认域 | 表类型：参数表 | 字段数：21 | 审核状态：待审核 | 数据链段：第二段·市场档位拆解

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 参数表

**A-类型规则风险：** 参数表天然存在「档位评定的触发条件」与「规则变更的历史追溯」规则风险。档位评定周期与追溯规则若缺失，将引发渠道争议。

**A-本表信号字段：**
- FYC_Adjustment（首年佣金调整系数）— 直接决定渠道佣金加成比例，微小错误将导致大额财务偏差
- RYC_Adjustment（续年佣金调整系数）— 同上，续期调整错误将长期累积
- Effective_Date_Type（日期类型）— 档位生效规则的类型字段，若未定义（签单日期vs生效日期vs批核日期），将导致档位适用争议

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=Carrie / 填写人=momo / Owner=MOMO / Steward=MOMO

**B-责任模式：** 三权合一 🔴 + 判断理由：Owner=MOMO、Steward=MOMO、填写人=momo（同一人）。档位规则涉及渠道激励的核心规则，单人操作存在重大内控风险。

**B-单点责任字段：**
- FYC_Adjustment（首年佣金调整系数）— Owner=MOMO/Steward=MOMO/填写人=momo，三权合一，系数错误将直接造成大额财务偏差
- RYC_Adjustment（续年佣金调整系数）— 同上，续期错误长期累积

**B-字段级规则信号：**
- C1命中：Priority、Partner_code、Carrier_Code_Condition、Partner_Category、Customer_Type、Bussiness_Line_Condition、Product_Unit_Condition、FYC_Tier、RYC_Tier、FYC_Adjustment、RYC_Adjustment、Effective_Date_Type、effective_date、expiry_date
- C2命中：无
- C3命中：Priority、Partner_code、Carrier_Code_Condition、Partner_Category、Customer_Type、Bussiness_Line_Condition、Product_Unit_Condition、FYC_Tier、RYC_Tier、FYC_Adjustment、RYC_Adjustment、Fixed_Fee_Rate、Effective_Date_Type、effective_date、expiry_date、Description
- C4命中：Priority、Partner_code、Carrier_Code_Condition、Partner_Category、Customer_Type、Bussiness_Line_Condition、Product_Unit_Condition、FYC_Tier、RYC_Tier、FYC_Adjustment、RYC_Adjustment、Fixed_Fee_Rate、Effective_Date_Type、effective_date、expiry_date、Description
- C5命中：Partner_code、Carrier_Code_Condition、Partner_Category、Customer_Type、Bussiness_Line_Condition、Product_Unit_Condition、Effective_Date_Type

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：源头佣金宽表→市场档位佣金表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测档位规则是否被下游消费，但无法检测「业绩门槛设置不合理」。例如FYC_Tier门槛设置为100万，但全平台最高业绩为80万，门槛永远无法达到，程序验证通过但档位评定逻辑实际失效，所有合作伙伴只能拿到最低档位佣金，引发渠道投诉。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义）— 无商业职能定义，处于「待审核」；档位规则直接影响渠道激励成本

**D-合规风险：** 中 — 参数配置错误可能向下游传导，需关注生效规则与冲突检测机制

### 规则空白汇总
⚠️ 档位评定触发周期（按月/按季）与历史追溯规则缺失 → 五问：Q1/Q3 → 评分维度：D2
⚠️ 档位规则变更时是否触发历史业绩重算及补差规则缺失 → 五问：Q3/Q5 → 评分维度：D5

---

## 表11：【产品排除范围配置】/ CONFIG_PRODUCT_EXCLUSION_RANGE
所属域：费率确认域 | 表类型：参数表 | 字段数：15 | 审核状态：待审核 | 数据链段：第二段·市场档位拆解

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 参数表

**A-类型规则风险：** 参数表天然存在「排除逻辑的完备性」与「排除与包含的边界模糊」规则风险。排除规则若缺乏一致性校验，易出现应排除未排除或过度排除的合规问题。

**A-本表信号字段：**
- is_active（是否有效）— 排除开关字段，误关闭将导致应排除产品被错误计入佣金
- excluded_product_sku（排除的产品SKU）— 排除对象字段，多层级排除（业务分类→产品线→SKU）的继承规则未定义
- table_type（制表类型）— 排除范围的场景字段，若与包含规则同时命中时的优先级未定义

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=Carrie / 填写人=Carrie / Owner=MOMO / Steward=MOMO

**B-责任模式：** 三权合一 🔴 + 判断理由：Owner=MOMO、Steward=MOMO、填写人=Carrie。Owner/Steward为MOMO，填写人为Carrie，表面上存在分离，但MOMO是否对Carrie的每次修改进行Steward复核从数据无法确认，存在交接模糊向三权合一滑移的风险。

**B-单点责任字段：**
- is_active（是否有效）— Owner=MOMO，排除开关误操作将直接导致应排除产品被错误计入佣金
- excluded_product_sku（排除的产品SKU）— Owner=MOMO，排除对象错误将导致佣金计算范围偏差

**B-字段级规则信号：**
- C1命中：business_category、table_type、excluded_carrier_code、excluded_bussiness_line、excluded_product_pgu、excluded_product_sku、excluded_product_id、excluded_rate_option_code、is_active
- C2命中：table_type
- C3命中：business_category、table_type、excluded_carrier_code、excluded_bussiness_line、excluded_product_pgu、excluded_product_sku、excluded_product_id、excluded_rate_option_code、is_active、remark
- C4命中：business_category、table_type、excluded_carrier_code、excluded_bussiness_line、excluded_product_pgu、excluded_product_sku、excluded_product_id、excluded_rate_option_code、is_active、remark
- C5命中：excluded_carrier_code、excluded_bussiness_line、excluded_product_pgu、excluded_product_sku、excluded_product_id、excluded_rate_option_code

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：源头佣金宽表→市场档位佣金表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测排除配置是否被下游读取，但无法检测「排除范围与产品上架状态冲突」。例如某SKU在CONFIG_PRODUCT_EXCLUSION_RANGE中被排除（is_active=1），但DIM_PRODUCT_SKU中该SKU的上架状态仍为「上架」，产品仍可被推荐出单，程序验证通过但业务逻辑矛盾（产品可售但无佣金）。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义）— 无商业职能定义，处于「待审核」；排除规则直接影响佣金计算范围

**D-合规风险：** 中 — 参数配置错误可能向下游传导，需关注生效规则与冲突检测机制

### 规则空白汇总
⚠️ 排除规则与包含规则的优先级及冲突仲裁机制缺失 → 五问：Q3 → 评分维度：D2
⚠️ 排除范围的多层级继承规则（业务分类→产品线→SKU）未定义 → 五问：Q3 → 评分维度：D1

---

## 表12：【市场佣金制表参数】/ CONFIG_COMMISSION_TABLE_TYPE
所属域：费率确认域 | 表类型：参数表 | 字段数：15 | 审核状态：待审核 | 数据链段：第二段·市场档位拆解

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 参数表

**A-类型规则风险：** 参数表天然存在「制表参数的差异化叠加」与「默认参数兜底」规则风险。参数缺失时的默认行为与多参数叠加逻辑若缺失，将导致制表结果不可预期。

**A-本表信号字段：**
- table_type（制表类型）— 直接决定市场佣金表的输出格式与拆分逻辑，错误将导致全量佣金表结构错误
- commission_pattern（佣金模式）— 模式字段，若与产品佣金公式配置表中的模式不一致，将导致佣金拆分逻辑断裂
- main_license_code（主签牌照）— 制表关联字段，若指向的牌照未授权该业务分类，将导致合规问题

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=Carrie / 填写人=Carrie / Owner=MOMO / Steward=MOMO

**B-责任模式：** 三权合一 🔴 + 判断理由：Owner=MOMO、Steward=MOMO、填写人=Carrie。同CONFIG_PRODUCT_EXCLUSION_RANGE，表面有分离但缺乏Carrie修改后MOMO复核的明确流程证据。

**B-单点责任字段：**
- table_type（制表类型）— Owner=MOMO，直接决定市场佣金表输出格式，错误将导致全量佣金表结构错误
- commission_pattern（佣金模式）— Owner=MOMO，模式不一致将导致佣金拆分逻辑断裂

**B-字段级规则信号：**
- C1命中：business_category、table_type、partner_code、partner_name、partner_category、commission_pattern、customer_type、main_license_code、commission_date、commission_duration
- C2命中：table_type、partner_name
- C3命中：business_category、table_type、partner_code、partner_name、partner_category、commission_pattern、customer_type、main_license_code、commission_date、commission_duration
- C4命中：business_category、table_type、partner_code、partner_name、partner_category、commission_pattern、customer_type、main_license_code、commission_date、commission_duration
- C5命中：commission_pattern

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：源头佣金宽表→市场档位佣金表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测制表参数是否被下游消费，但无法检测「制表类型与业务分类组合不存在对应模板」。例如table_type=B2B但业务分类为BRK（经代业务），B2B模板未定义BRK业务线的字段排列，程序验证通过但生成的佣金表缺少关键字段，渠道无法对账。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义）— 无商业职能定义，处于「待审核」；制表参数直接影响对外交付的佣金表格式

**D-合规风险：** 中 — 参数配置错误可能直接影响客户交付物

### 规则空白汇总
⚠️ 参数缺失时的默认兜底规则与多参数叠加合并逻辑缺失 → 五问：Q3 → 评分维度：D2
⚠️ 制表参数变更后下游佣金表重生成触发机制缺失 → 五问：Q1/Q4 → 评分维度：D3

---

## 表13：【市场档位佣金表】/ AGG_MARKET_COMMISSION_TIER_RATE
所属域：费率确认域 | 表类型：聚合表 | 字段数：17 | 审核状态：进行中 | 数据链段：第二段·市场档位拆解

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 聚合表

**A-类型规则风险：** 聚合表天然存在「档位费率的数据溯源」与「业绩门槛的动态调整」规则风险。聚合口径与门槛调整机制若缺失，业务方与财务方对同一档位的理解将出现分歧。

**A-本表信号字段：**
- partner_tier（合作伙伴档位）— 聚合结果字段，Owner为空，档位判定结果直接决定渠道激励水平
- fyc_tier（FYC档位）— 同上，聚合逻辑错误将直接导致档位评定偏差
- total_y1（Y1总佣金）— 聚合金额字段，若聚合口径（自然月/滚动季度）未定义，金额将与业务预期不一致

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=Carrie / 填写人=Carrie / Owner=无 / Steward=无

**B-责任模式：** 治理真空 🔴 + 判断理由：分工=Carrie，填写人=Carrie，但全部字段Owner/Steward为空。Carrie是否为业务口径定义者还是仅执行ETL配置，从数据无法判断。

**B-单点责任字段：**
- partner_tier（合作伙伴档位）— Owner为空，档位判定结果直接决定渠道激励水平但无责任主体
- fyc_tier（FYC档位）— Owner为空，聚合逻辑错误将直接导致档位评定偏差

**B-字段级规则信号：**
- C1命中：无
- C2命中：无
- C3命中：无
- C4命中：无
- C5命中：无

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：源头佣金宽表→市场档位佣金表

**C-在链位置：** 中间

**C-验证盲区：** 语义错误 — 程序验证可检测源头佣金宽表是否成功聚合到档位佣金表，但无法检测「业绩门槛四舍五入规则导致临界值保单档位跳变」。例如业绩门槛为100万，某合作伙伴业绩为99.9999万，若四舍五入规则未定义（是否进位到100万），可能从Tier2跳变到Tier1，程序验证通过但档位判定结果存在争议。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义）— 无商业职能定义，处于「进行中」；档位佣金结果可能未经最终确认即用于结算

**D-合规风险：** 中 — 聚合表数据用于决策与对账，ETL逻辑不透明将导致汇总偏差难以追溯

### 规则空白汇总
⚠️ 聚合口径（自然月/滚动季度/保单年度）与业绩门槛动态调整规则缺失 → 五问：Q1/Q3 → 评分维度：D2
⚠️ 全部字段Owner/Steward为空，档位佣金结果偏差时无业务责任主体 → 五问：Q5 → 评分维度：D6

---

## 表14：【市场佣金表】/ 市场佣金表
所属域：— | 表类型：聚合表 | 字段数：— | 审核状态：进行中 | 数据链段：第二段·市场档位拆解

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### A · 表类型规则洞察
**A-表类型：** 聚合表

**A-类型规则风险：** 聚合表天然存在「终态输出的权威性」与「对外交付的不可撤销性」规则风险。作为佣金数据链终态，输出格式标准与终审机制若缺失，将引发渠道对账混乱。

**A-本表信号字段：**
- ⛔字段待补充 — Sheet2字段级信息缺失，无法识别具体信号字段，访谈优先

### B · 分工断点与字段唯一责任
**B-分工结构：** 分工=Carrie / 填写人=Carrie / Owner=— / Steward=—

**B-责任模式：** 自填自审 🔴 + 判断理由：⛔字段待补充，无法判断字段级责任。从Sheet1看，分工=填写人=Carrie，终态交付表由同一人负责全流程，缺乏独立复核机制的可能性极高。

**B-单点责任字段：**
- ⛔字段待补充，访谈优先

**B-字段级规则信号：**
- C1命中：⛔字段待补充
- C2命中：⛔字段待补充
- C3命中：⛔字段待补充
- C4命中：⛔字段待补充
- C5命中：⛔字段待补充

### C · 程序验证路径与断点
**C-验证路径：** 程序验证：市场档位佣金表→市场佣金表

**C-在链位置：** 终态

**C-验证盲区：** 交接断点 — 程序验证可检测市场档位佣金表是否成功流转到市场佣金表，但无法检测「已交付佣金表被后台静默修改未留痕」。例如市场佣金表已发给渠道合作伙伴，但后台因发现错误直接修改了表中某行数据，未触发版本变更通知，渠道手持旧版数据与平台新版数据对账不一致，引发纠纷。程序验证仅在数据流转时检查，不监控交付后的变更。

### D · 商业职能与授权
**D-职能定义：** 未定义 → 授权级别：🟢 低

**D-审核状态匹配：** 缺失（无商业职能定义）— 无商业职能定义，处于「进行中」；作为对外交付的终态表，审核未完成

**D-合规风险：** 高 — 字段信息待补充，规则黑盒风险极高，需优先访谈澄清

### 规则空白汇总
⚠️ ⛔字段待补充，访谈优先：对外交付前的终审机制与数字准确性责任人完全缺失 → 五问：Q5 → 评分维度：D6
⚠️ ⛔字段待补充，访谈优先：已发出佣金表的召回/更正规则与渠道通知机制缺失 → 五问：Q3/Q5 → 评分维度：D5

---

## 自检声明

已对照TASK-EFA-005的Done Criteria DC1-DC9逐项自检，结果：

| DC | 自检内容 | 结果 |
|:---:|:---|:---:|
| DC1 | 14张表全部输出单表标签卡，无遗漏 | ✅ |
| DC2 | 每张表的标签A包含具体字段名（不只是类型描述） | ✅ |
| DC3 | 每张表的标签B完成字段级C1-C5过滤（字段暂缺的表标注⛔） | ✅ |
| DC4 | 每张表的标签C包含具体验证盲区示例（不只是类型名称） | ✅ |
| DC5 | 每张表的标签D完成授权级别判断+匹配性检查 | ✅ |
| DC6 | 字段级规则信号清单覆盖全部命中C1-C5的字段（见产出物二） | ✅ |
| DC7 | 规则空白地图包含P0/P1/P2优先级，每条附访谈问题草稿（见产出物三） | ✅ |
| DC8 | 产出物中不包含规则内容（只识别空白，不填充内容） | ✅ |
| DC9 | 自检声明已注明 | ✅ |

---
ENDSCRIPT
