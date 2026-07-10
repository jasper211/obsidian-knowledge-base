---
文档类型: 02_过程成果-工作产出 / 规则分析 / 延展_同行经代NBRD
文档编号: IBRD001
版本: V1.0
创建日期: 2026-06-04
执行终端: Kimi
任务包: TASK-M4W10-060
输入文件:
  - 上下文_数据规则提取方法论_三层递进提取法_v2.4.md
  - D1_价值节点清单_V3.14.xlsx
  - 调研_同行合作需求诊断_V1.1.xlsx
  - 合作伙伴相关表.xlsx
  - A-02_合作路径决策树_JFUNIVIN_v1.2.md
  - B-01_转介信息标准模板_v1.1.md
  - A-03_尽职调查执行记录_v1.1.md
  - VN-IBRD-01_Gate重新验证报告_v1.0.md
---

# IBRD 第一层产出：四标签分析 + 规则空白地图

> **分析范围**：IBRD（同行经代）价值节点及相关数据表
> **分析视角**：价值节点视角（方法论v2.3新增）
> **输出阶段**：Phase 0评估 + 第一层四标签（规则空白地图）
> **不进入范围**：KA专属数据表、IBEC/URD四标签产出、访谈执行

---

## 一、Phase 0：价值节点评估

### 1.1 评估依据

- 方法论v2.4附录G：V3.0裁定状态 → Phase 0评级映射表
- VN-IBRD-01_Gate重新验证报告v1.0：补建后三Gate全PASS，覆盖V3.14原始P0熔断状态
- D1_价值节点清单_V3.14.xlsx：IBRD/IBEC/URD/EQ相关节点原始Gate状态

### 1.2 Phase 0评估表

| 节点编号 | 节点名称 | V3.14原始状态 | 补建后状态 | D评级 | 进入三层递进 | 备注 |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **VN-IBRD-01** | 合作伙伴尽调记录 | 🔴 P0熔断（Gate3 FAIL） | 🟢 三Gate全PASS | **D2** | ✅ 直接进入 | 引用Gate重新验证报告v1.0：A-02/B-01/A-03三件套补建完成，三重Gate全部通过，原熔断状态已解除 |
| VN-EQ-01 | 同行经代服务方案 | 🔴 P1熔断 | — | D4 | ❌ 先走补建 | Gate①FAIL+Gate③FAIL，个性化方案缺失，数据验证未通过。属EQ域，不纳入IBRD主体分析 |
| VN-URD-01 | 联合运营需求诊断报告 | 🔴 P1熔断 | — | D4+ | ❌ 先走补建 | 三Gate全FAIL，流程完全缺失，概念阶段。属URD域，仅作参考 |

> **特别说明**：VN-IBRD-01的Phase 0评级**不以V3.14原始P0熔断状态为准**，而是以Gate重新验证报告v1.0的补建结果为准。补建后三重Gate全部PASS，按方法论v2.4映射为🟢通过→D2，直接进入三层递进。

---

## 二、IBRD数据表归口分析

### 2.1 判断原则

- **IBRD相关**：表中有`partner_category`条件且适用「同行经代」分类，或字段直接支撑IBRD业务（牌照核查、协议签署、佣金路由）
- **KA专属表排除**：`dim_ka`、`bridge_partner_ka`等仅服务KA业务，与同行经代无关
- **两者共用表**：标注「共用表·IBRD视角」，只分析IBRD相关字段
- **建议新建表**：三件套或调研中发现但数据表清单无记录的实体工具

### 2.2 IBRD数据表索引

| 序号 | 表名 | 表类型 | IBRD相关字段 | 备注 |
|:---:|:---|:---:|:---|:---|
| 1 | **dim_partner**（合作伙伴维度） | 维度表 | `partner_code`, `partner_category`, `partner_status`, `first_contract_date`, `parent_partner_code`, `ops_fixed_rate` | 共用表·IBRD视角。`partner_category`定义同行经代分类，`partner_status`驱动状态流转 |
| 2 | **dim_license**（牌照维度） | 维度表 | `license_code`, `license_type`, `license_end_date`, `is_external`, `license_business_scope` | IBRD相关。`license_type`驱动A-02判断节点0（资管牌→DW/经纪行→JF/UNIVIN） |
| 3 | **dim_binder_agreement**（协议维度） | 维度表 | `binder_id`, `agreement_type`, `partner_code`, `sign_entity`, `payment_entity`, `effective_date`, `expiry_date`, `license_code` | 共用表·IBRD视角。`agreement_type`枚举值含"同行推荐"，驱动结算逻辑 |
| 4 | **config_partner_routing**（合作伙伴牌照路由） | 配置表 | `routing_rules_id`, `priority`, `partner_category_condition`, `commission_pattern`, `assigned_license_code`, `is_active` | 共用表·IBRD视角。`partner_category_condition`匹配同行经代分类，决定牌照覆写 |
| 5 | **partner_tier_rules**（合作伙伴档位规则） | 配置表 | `priority`, `partner_code`, `partner_category`, `fyc_tier`, `ryc_tier`, `fixed_fee_rate` | 共用表·IBRD视角。`partner_category`匹配同行经代档位，`fixed_fee_rate`适用固定费率场景 |
| 6 | **map_partner_payee**（合作伙伴收款人映射） | 映射表 | `partner_code`, `payee_sk`, `split_ratio` | 共用表·IBRD视角。同行经代佣金拆分到多个收款主体 |
| 7 | **dim_payee**（收款人维度） | 维度表 | `payee_sk`, `legal_entity_name_en`, `bank_name`, `bank_account_number`, `min_payout_threshold` | 共用表·IBRD视角。`min_payout_threshold`影响同行经代佣金起付金额 |
| 8 | dim_comm_scheme（佣金方案维度） | 维度表 | `scheme_id`, `scheme_type` | 共用表·IBRD视角。战略激励体系顶层维度，IBRD适用 |
| 9 | dim_strategy（策略维度） | 维度表 | `strategy_id`, `strategy_tag` | 共用表·IBRD视角。策略激励体系执行单元 |
| 10 | bridge_strategy_routing（策略路由桥接表） | 桥接表 | `scheme_id`, `partner_category`, `target_strategy_id` | 共用表·IBRD视角。`partner_category`匹配同行经代策略 |
| 11 | fact_target（目标业绩表） | 事实表 | `period_key`, `segment_code`, `target_ape`, `target_revenue` | 共用表·IBRD视角。同行经代业绩目标通过`segment_code`关联 |
| — | ~~dim_ka~~（关键客户维度） | 维度表 | — | **KA专属·已排除** |
| — | ~~bridge_partner_ka~~（合作伙伴-KA匹配表） | 桥接表 | — | **KA专属·已排除** |
| — | **SLHK同行登记表**（建议新建） | 过程表 | `partner_name`, `broker_name`, `license_no`, `contact_info`, `profile_desc`, `source_line`, `registration_date`, `follow_up_status` | 建议新建。调研确认实际管理工具（MoMo/菲菲/Mark三人同步），dim_process未定义，未纳入数据表清单 |
| — | **合约跟进表**（建议新建） | 过程表 | `partner_code`, `contract_status`, `contract_send_date`, `contract_return_date`, `sign_entity`, `follow_up_reminder` | 建议新建。调研批次8确认存在，记录合约发送-签回-跟进状态，当前为Excel/邮件形式 |

---

## 三、第一层：四标签 + 规则空白地图

### 3.1 分析说明

- **分析对象**：可进入三层递进的VN-IBRD-01节点
- **分析单元**：价值节点视角，在VN-IBRD-01内识别涉及的表和字段
- **已覆盖规则不重复纳入**：三件套（A-02/B-01/A-03）中已书面化的流程规则，只做「与三件套对照」标注，不作为规则空白重复提取
- **数据表规则为主**：第一层聚焦数据表字段级规则缺口，流程规则缺口由三件套覆盖

### 3.2 单表四标签摘要（支撑规则空白优先级判定）

#### 【dim_partner】四标签摘要
- **A·表类型规则洞察**：维度表。信号字段：`partner_category`（编码规则风险：同行经代枚举未定义）、`partner_status`（状态流转风险：与尽调结论对接规则缺失）、`first_contract_date`（业务规则：首次签约日期对合作优先级的影响未定义）
- **B·分工断点**：分工结构：填写人=业务人员维护config / Owner=业务人员 / Steward=未定义 → **责任模式：自填自审🔴**。单点责任字段：`partner_category`（一人维护，直接影响下游佣金计算和路由匹配）
- **C·程序验证路径**：源头（业务人员维护Excel）→ sync同步至DB → 被Agg2/FACT2/BRIDGE引用。验证盲区：交接断点（维护后下游无签收）、语义错误（partner_status值与尽调结论不匹配）
- **D·商业职能**：合作伙伴准入确权 → **授权级别：🔴高**。审核状态匹配：不匹配（自填自审无独立复核）
- **综合优先级**：**P0**（B=🔴 + D=🔴 + ❌规则缺口）

#### 【dim_license】四标签摘要
- **A·表类型规则洞察**：维度表。信号字段：`license_type`（枚举：经纪/代理/资管，驱动合作路径判断）、`license_end_date`（有效期规则：当前无硬性门槛，但过期后处理规则未定义）、`is_external`（外部牌照标识规则）
- **B·分工断点**：填写人=业务人员维护config → **责任模式：自填自审🔴**。单点责任字段：`license_type`（直接影响A-02决策树判断节点0）
- **C·程序验证路径**：源头→被fact_commission_rate/config_partner_routing引用。验证盲区：语义错误（Is_Active=1但牌照已过期）、触发缺失（牌照到期无系统预警）
- **D·商业职能**：牌照准入确权（合作前提）→ **授权级别：🔴高**
- **综合优先级**：**P0**

#### 【config_partner_routing】四标签摘要
- **A·表类型规则洞察**：配置表。信号字段：`priority`（冲突解决：新增规则优先级分配未定义）、`partner_category_condition`（条件规则：同行经代分类匹配规则未定义）、`assigned_license_code`（覆写规则：与JF/UNIVIN/DW路径的映射未定义）、`is_active`（生效失活规则）
- **B·分工断点**：填写人=业务人员维护config → **责任模式：自填自审🔴**。单点责任字段：`priority`（冲突时取首个命中，新增规则可能覆盖旧规则）
- **C·程序验证路径**：Agg2步骤四按优先级遍历。验证盲区：公式错误（两条规则同时命中时的fallback逻辑）、触发缺失（规则变更后下游佣金计算无通知）
- **D·商业职能**：商业建模与结构定型（牌照分配策略）→ **授权级别：🟢中**
- **综合优先级**：**P1**（B=🔴 + ❌缺口，D=🟢不满足🔴）

#### 【partner_tier_rules】四标签摘要
- **A·表类型规则洞察**：配置表。信号字段：`priority`（冲突解决）、`partner_category`（枚举规则：同行经代档位匹配条件未定义）、`fyc_tier`/`ryc_tier`（档位规则）、`fixed_fee_rate`（固定费率规则）
- **B·分工断点**：填写人=业务人员维护config → **责任模式：自填自审🔴**
- **C·程序验证路径**：Agg2步骤三按优先级遍历。验证盲区：公式错误（档位计算逻辑未文档化）
- **D·商业职能**：财务结算（佣金档位决定支付金额）→ **授权级别：🟡高**
- **综合优先级**：**P1**（B=🔴 + D=🟡 + ❌缺口，D非🔴）

#### 【dim_binder_agreement】四标签摘要
- **A·表类型规则洞察**：维度表。信号字段：`agreement_type`（枚举：转介/同行推荐/个人推荐/获客服务，与IBRD场景的精确映射未定义）、`effective_date`/`expiry_date`（有效期规则：续约触发机制未定义）
- **B·分工断点**：填写人=业务人员维护config → **责任模式：自填自审🔴**
- **C·程序验证路径**：被payable_commission.py读取。验证盲区：触发缺失（协议到期无提醒导致结算错误）
- **D·商业职能**：财务结算（协议驱动结算逻辑）→ **授权级别：🟡高**
- **综合优先级**：**P1**

#### 【map_partner_payee】四标签摘要
- **A·表类型规则洞察**：映射表。信号字段：`split_ratio`（分配比例规则：多收款人时之和为1的校验规则未定义）
- **B·分工断点**：填写人=业务人员维护config → **责任模式：自填自审🔴**
- **C·程序验证路径**：被payable_commission.py读取用于佣金分配。验证盲区：公式错误（split_ratio之和校验逻辑）
- **D·商业职能**：财务结算 → **授权级别：🟡高**
- **综合优先级**：**P1**

#### 【dim_payee】四标签摘要
- **A·表类型规则洞察**：维度表。信号字段：`min_payout_threshold`（最低起付金额规则：同行经代场景的起付标准未定义）、`bank_account_number`（敏感信息校验规则）
- **B·分工断点**：填写人=业务人员维护config → **责任模式：自填自审🔴**
- **C·程序验证路径**：被payable_commission.py读取。验证盲区：语义错误（银行账户错误导致付款失败）
- **D·商业职能**：财务结算 → **授权级别：🟡高**
- **综合优先级**：**P1**

---

### 3.3 规则空白地图

---

#### P0 · 核心规则空白

---
**规则空白编号：IBRD-P0-001**
**优先级：P0**
**规则主题：dim_partner.partner_category 同行经代分类枚举与映射规则**
**关联L3：L3-IBRD**
**关联L4：L4-IBRD-03 尽职调查执行**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：dim_partner.partner_category, dim_partner.partner_name**

**A·固定锚点**：
- 表名：dim_partner（合作伙伴维度）
- 字段：partner_category, partner_name
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- B-01 v1.1模板中B类字段定义业务模式为：转借/FA/兼业代理/其他。这与partner_category的枚举值（个人顾问/机构合作伙伴/关键客户等）尚未建立映射关系。
- 调研批次8确认存在"同行经代"业务分类，但数据字典中partner_category的精确枚举值未明确。
- A-02 v1.2决策树判断节点0（牌照类型判断）和判断节点0b（来源线判断）的输出需要映射到partner_category字段。
- 来源：B-01 v1.1 + 调研批次8 + A-02 v1.2

**C·存在性确认**：
- 字段存在（dim_partner.partner_category）。
- 但"同行经代"作为partner_category的精确枚举值未确认，且与B-01业务模式字段的映射规则缺失。
- 来源：数据表清单 + 调研记录差异项#10（SLHK登记表未纳入流程库）

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
- 需定义partner_category中"同行经代"的精确枚举值（如"broker_agency"）
- 需建立B-01业务模式（转借/FA/兼业代理）与partner_category的映射表
- 需明确江通线/白博文线在partner_category中的区分方式（或是否通过其他字段区分）

**与三件套对照**：
B-01已覆盖业务模式分类（流程规则），但未映射到数据表枚举值（数据规则空白）。→ **补充**

---
**规则空白编号：IBRD-P0-002**
**优先级：P0**
**规则主题：dim_partner.partner_status 状态流转与IBRD尽调结论对接规则**
**关联L3：L3-IBRD**
**关联L4：L4-IBRD-03 尽职调查执行**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：dim_partner.partner_status, dim_partner.first_contract_date**

**A·固定锚点**：
- 表名：dim_partner
- 字段：partner_status, first_contract_date
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- B-01 v1.1 Q-16已明确退回与关闭机制：退回后一季度观察期无进展→确认无合作意向后关闭。
- A-03 v1.1 J类尽调结论包含"合作路径建议"（JF/UNIVIN/DW/暂不推进）和"合作优先级"（高/中/低）。
- 但partner_status的枚举值（如潜在/意向/签约/活跃/暂停/终止）与尽调结论的输出未建立映射。
- 调研批次7确认"签完不出单"现象普遍，但partner_status如何标记"签约后未出单"状态未定义。
- 来源：B-01 v1.1 Q-16 + A-03 v1.1 J类 + 调研批次7

**C·存在性确认**：
- partner_status字段存在，但状态流转规则（状态机）未定义。
- first_contract_date字段存在，但与partner_status的联动规则（如签约后自动赋值）未定义。
- 来源：数据表清单 + 调研记录差异项#7（合同后置）

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
- 需定义partner_status完整状态机（至少包含：潜在→意向→尽调中→签约→活跃→暂停→终止）
- 需明确A-03 J类尽调结论"暂不推进"映射到哪个状态（暂停？观察期？）
- 需定义first_contract_date的自动赋值触发条件（合同签署完成？系统归档？）

**与三件套对照**：
B-01/A-03已覆盖流程层面的退回/关闭机制和尽调结论，但未映射到数据表状态字段。→ **补充**

---
**规则空白编号：IBRD-P0-003**
**优先级：P0**
**规则主题：dim_license.license_type 与IBRD合作路径的数据表映射规则**
**关联L3：L3-IBRD**
**关联L4：L4-IBRD-03 尽职调查执行**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：dim_license.license_type, dim_license.license_end_date, dim_license.is_external**

**A·固定锚点**：
- 表名：dim_license
- 字段：license_type, license_end_date, is_external
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- A-02 v1.2判断节点0已明确牌照类型判断：资管牌照→DW合作；经纪行牌照→进入JF/UNIVIN判断。
- A-02 v1.2边界Case2明确多牌照场景处理（经纪牌+资管牌并存时的优先级）。
- B-01 v1.1 A类字段包含"牌照类型"（保险经纪/保险代理/资管/其他）。
- 但dim_license.license_type的枚举值如何映射到A-02的三条路径（DW/JF/UNIVIN），当前无数据表级规则。
- B-01 v1.1 Q-11确认"牌照有效期当前无硬性门槛"，但数据表中license_end_date的业务规则（是否预警、过期后是否自动阻断合作）未定义。
- 来源：A-02 v1.2 + B-01 v1.1 + 调研批次6/8

**C·存在性确认**：
- dim_license字段完整存在。
- license_type到config_partner_routing.assigned_license_code的自动映射规则未建立。
- license_end_date的预警/阻断规则未定义。
- 来源：数据表清单 + 调研记录

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
- 需定义license_type枚举值与A-02三条合作路径的精确映射（如"资管"→DW，"经纪"→JF/UNIVIN判断）
- 需明确多牌照并存时（边界Case2）config_partner_routing的匹配优先级规则
- 需定义license_end_date过期后的系统处理规则（预警？阻断？人工复核？）

**与三件套对照**：
A-02已覆盖流程层面的牌照类型判断规则，但未建立到dim_license数据表的自动映射机制。→ **补充**

---
**规则空白编号：IBRD-P0-004**
**优先级：P0**
**规则主题：config_partner_routing + partner_tier_rules 同行经代路由与档位联动规则**
**关联L3：L3-IBRD**
**关联L4：L4-IBRD-03 尽职调查执行 / L4-NG-01 合同谈判与审核**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：config_partner_routing.partner_category_condition, config_partner_routing.assigned_license_code, config_partner_routing.priority, partner_tier_rules.partner_category, partner_tier_rules.fyc_tier, partner_tier_rules.fixed_fee_rate**

**A·固定锚点**：
- 表名：config_partner_routing, partner_tier_rules
- 字段：partner_category_condition, assigned_license_code, priority, fyc_tier, fixed_fee_rate
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- A-02 v1.2已明确三条合作路径及切换规则（JF↔UNIVIN需取消永明合约）。
- 调研批次8确认："档位由BD首要判断+合作后按贡献度调整"，MOMO录音"很多是烟雾弹"。
- config_partner_routing按6个条件字段匹配assigned_license_code，但partner_category_condition中"同行经代"的匹配条件未定义。
- partner_tier_rules中同行经代的FYC/RYC档位及fixed_fee_rate适用场景未定义。
- 两条配置表的priority字段冲突检查依赖人工，无系统自动校验。
- 来源：A-02 v1.2 + 调研批次8 + 数据表清单

**C·存在性确认**：
- config_partner_routing和partner_tier_rules表结构存在。
- 但partner_category_condition中同行经代的精确匹配条件未配置。
- assigned_license_code与JF/UNIVIN/DW牌照代码的映射未定义。
- partner_tier_rules中同行经代专属档位规则行未配置。
- 来源：数据表清单

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
- 需定义config_partner_routing中partner_category_condition="同行经代"时的完整路由规则集（含ALL通配规则、特例规则）
- 需明确assigned_license_code与JF牌照/UNIVIN牌照/DW牌照的系统编码映射
- 需定义partner_tier_rules中同行经代的默认档位及fixed_fee_rate触发条件
- 需建立priority冲突检查的自动化校验规则（防止两条规则同时命中同一同行经代）

**与三件套对照**：
A-02已覆盖流程层面的路径判断和档位逻辑（口头规则），但未沉淀为config_partner_routing和partner_tier_rules的数据表配置规则。→ **未覆盖**

---

#### P1 · 重要规则空白

---
**规则空白编号：IBRD-P1-001**
**优先级：P1**
**规则主题：dim_binder_agreement.agreement_type 同行经代协议类型与结算逻辑映射**
**关联L3：L3-IBRD**
**关联L4：L4-IBRD-03 尽职调查执行 / L4-NG-02 合同签署与信息同步**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：dim_binder_agreement.agreement_type, dim_binder_agreement.sign_entity, dim_binder_agreement.payment_entity**

**A·固定锚点**：
- 表名：dim_binder_agreement
- 字段：agreement_type, sign_entity, payment_entity
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- 数据表定义：agreement_type枚举值包括转介/同行推荐/个人推荐/获客服务，不同协议类型驱动不同结算逻辑。
- A-02 v1.2已明确JF/UNIVIN/DW三条路径的签约主体差异（JF=久富牌照，UNIVIN=UNIVIN牌照，DW=DW牌照）。
- 但"同行推荐"协议类型如何精确映射到JF/UNIVIN/DW路径，以及sign_entity/payment_entity的自动赋值规则未定义。
- 调研批次8确认合同签回周期1-2个月，但effective_date/expiry_date的自动计算规则未定义。
- 来源：数据表清单 + A-02 v1.2 + 调研批次8

**C·存在性确认**：
- 维度表存在，agreement_type字段存在。
- 但同行经代场景下的agreement_type精确映射规则未定义。
- sign_entity/payment_entity与A-02路径的自动关联未建立。
- 来源：数据表清单

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无（P1级，不阻塞SOP产出）

**与三件套对照**：
A-02已覆盖签约主体规则（流程层），但未映射到dim_binder_agreement字段（数据层）。→ **补充**

---
**规则空白编号：IBRD-P1-002**
**优先级：P1**
**规则主题：config_partner_routing.priority 路由规则优先级冲突检查机制**
**关联L3：L3-IBRD**
**关联L4：L4-IBRD-03 尽职调查执行**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：config_partner_routing.priority, config_partner_routing.partner_category_condition, config_partner_routing.is_active**

**A·固定锚点**：
- 表名：config_partner_routing
- 字段：priority, partner_category_condition, is_active
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- 数据表定义：按优先级定义牌照分配规则，6个条件字段精确匹配，支持ALL通配，仅匹配is_active=1的规则。
- Agg2步骤四按优先级遍历匹配，取首个命中的规则行覆写assigned_license_code。
- 但priority字段的分配规则未定义（新增规则时如何确定priority不冲突）。
- 调研未直接覆盖路由配置细节，但从数据表结构可推断存在冲突风险（多条规则同时命中同一合作伙伴时，系统取priority最小值，但无冲突预警）。
- 来源：数据表清单

**C·存在性确认**：
- 配置表存在，priority字段存在。
- 但priority冲突检查依赖人工，无系统自动校验机制。
- 无规则变更审批流程（谁有权新增/修改/删除路由规则）。
- 来源：数据表清单

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无

**与三件套对照**：
三件套未覆盖config_partner_routing的配置管理规则。→ **未覆盖**

---
**规则空白编号：IBRD-P1-003**
**优先级：P1**
**规则主题：partner_tier_rules.partner_category 同行经代档位匹配与调整规则**
**关联L3：L3-IBRD**
**关联L4：L4-IBRD-03 尽职调查执行**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：partner_tier_rules.partner_category, partner_tier_rules.fyc_tier, partner_tier_rules.ryc_tier, partner_tier_rules.fixed_fee_rate**

**A·固定锚点**：
- 表名：partner_tier_rules
- 字段：partner_category, fyc_tier, ryc_tier, fixed_fee_rate
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- 调研批次8确认：档位由BD首要判断，合作后按实际贡献度调整。MOMO录音"很多是烟雾弹"（同行自述规模不可信）。
- A-02 v1.2边界Case1确认佣金率已有不影响路径判断，但需记录以备档位匹配。
- 数据表定义：按5个条件字段（partner_code、保司、partner_category、客户类型、业务线+PGU）匹配档位及调整系数。
- 但partner_category="同行经代"时的默认FYC/RYC档位、fixed_fee_rate触发条件、调整周期未定义。
- 来源：调研批次8 + A-02 v1.2 + 数据表清单

**C·存在性确认**：
- 配置表存在，但partner_category中同行经代的专属档位规则行未配置。
- fixed_fee_rate适用场景（何时用固定费率替代阶梯档位）未定义。
- 来源：数据表清单

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无

**与三件套对照**：
A-02提及佣金率记录但不影响路径判断，未覆盖档位配置规则。→ **未覆盖**

---
**规则空白编号：IBRD-P1-004**
**优先级：P1**
**规则主题：map_partner_payee.split_ratio 同行经代佣金拆分规则**
**关联L3：L3-IBRD**
**关联L4：L4-NG-02 合同签署与信息同步**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：map_partner_payee.split_ratio, map_partner_payee.partner_code, map_partner_payee.payee_sk**

**A·固定锚点**：
- 表名：map_partner_payee
- 字段：split_ratio, partner_code, payee_sk
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- 数据表定义：split_ratio表示该合作伙伴的佣金中有多少比例支付给该收款人，多收款人时split_ratio之和为1。
- 调研未明确提及同行经代的佣金拆分场景（是否公司账户+个人账户拆分）。
- A-02 v1.2未涉及佣金拆分细节。
- 但数据表结构中split_ratio的校验规则（之和为1）未确认是否由系统强制执行。
- 来源：数据表清单

**C·存在性确认**：
- 映射表存在，但同行经代场景下的split_ratio赋值规则未确认。
- 多收款人拆分是否适用于同行经代（尤其是个人顾问型同行）未明确。
- 来源：数据表清单

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无

**与三件套对照**：
三件套未覆盖佣金拆分规则。→ **未覆盖**

---
**规则空白编号：IBRD-P1-005**
**优先级：P1**
**规则主题：dim_binder_agreement.effective_date / expiry_date 协议有效期管理与续约触发规则**
**关联L3：L3-IBRD**
**关联L4：L4-NG-02 合同签署与信息同步 / L4-IRR-04 续约谈判或终止**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：dim_binder_agreement.effective_date, dim_binder_agreement.expiry_date, dim_binder_agreement.binder_id**

**A·固定锚点**：
- 表名：dim_binder_agreement
- 字段：effective_date, expiry_date, binder_id
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- A-03 v1.1 Q-25建议参照DW建立年度DD更新机制，同行经代合作未满一年。
- 调研未明确提及同行经代协议的有效期标准（一般签多久？自动续约还是手动续约？）。
- 数据表定义包含effective_date和expiry_date，但续约触发条件（提前多久提醒？到期后自动失效还是自动延期？）未定义。
- 来源：A-03 v1.1 Q-25 + 数据表清单

**C·存在性确认**：
- 字段存在，但有效期管理与续约触发规则未定义。
- 无协议到期预警机制（数据表无提醒字段，依赖人工）。
- 来源：数据表清单

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无

**与三件套对照**：
A-03 Q-25提及年度更新机制建议，但未覆盖协议有效期管理规则。→ **未覆盖**

---

#### P2 · 补充规则空白

---
**规则空白编号：IBRD-P2-001**
**优先级：P2**
**规则主题：dim_payee.min_payout_threshold 同行经代最低起付金额规则**
**关联L3：L3-IBRD**
**关联L4：L4-NG-02 合同签署与信息同步**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：dim_payee.min_payout_threshold, dim_payee.default_currency**

**A·固定锚点**：
- 表名：dim_payee
- 字段：min_payout_threshold, default_currency
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- 数据表定义：min_payout_threshold表示最低起付金额，default_currency为默认货币。
- 调研未提及同行经代的最低起付标准（是否与个人顾问/KA不同？）。
- 来源：数据表清单

**C·存在性确认**：
- 字段存在，但同行经代场景的min_payout_threshold标准未定义。
- 来源：数据表清单

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无

**与三件套对照**：
三件套未覆盖最低起付规则。→ **未覆盖**

---
**规则空白编号：IBRD-P2-002**
**优先级：P2**
**规则主题：SLHK同行登记表数据化（建议新建表）**
**关联L3：L3-IBRD / L3-IBEC**
**关联L4：L4-IBEC-XX 前端渠道接触 / L4-IBRD-03 尽职调查执行**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：[建议新建表] slhk_partner_registry**

**A·固定锚点**：
- 建议表名：slhk_partner_registry（SLHK同行登记表）
- 字段：partner_name, broker_name, license_no, contact_info, profile_desc, source_line, registration_date, follow_up_status
- L3编码：L3-IBRD / L3-IBEC
- VN编码：VN-IBRD-01

**B·调研前预填**：
- 调研批次8确认SLHK同行登记表为实际管理工具，MoMo/菲菲/Mark三人同步维护，记录所有接触过的同行及画像描述。
- B-01 v1.1中C类字段包含"前端渠道内部编号"，与SLHK登记表的编号功能类似。
- 但dim_process中未定义此工具，数据表清单中无对应表。
- 来源：调研批次8 + VN-IBRD-01详情卡备注 + B-01 v1.1

**C·存在性确认**：
- 有实体交付物（Excel），但无数据表定义，未纳入流程库。
- 来源：调研批次8

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无

**与三件套对照**：
三件套未覆盖SLHK登记表的数据化。B-01提及前端渠道内部编号，但未关联到登记表。→ **未覆盖**

---
**规则空白编号：IBRD-P2-003**
**优先级：P2**
**规则主题：合约跟进表数据化（建议新建表）**
**关联L3：L3-IBRD**
**关联L4：L4-NG-02 合同签署与信息同步**
**关联价值节点：VN-IBRD-01**
**关联数据表/字段：[建议新建表] contract_follow_up**

**A·固定锚点**：
- 建议表名：contract_follow_up（合约跟进表）
- 字段：partner_code, contract_status, contract_send_date, contract_return_date, sign_entity, follow_up_reminder, contract_version
- L3编码：L3-IBRD
- VN编码：VN-IBRD-01

**B·调研前预填**：
- 调研批次8确认存在合约跟进表（签合约后使用），记录合约发送-签回-跟进状态。
- 调研批次7确认合同签回周期1-2个月，合同后置根因为内商务岗位缺失。
- A-02 v1.2判断节点2（签约是否完成）依赖合同管理系统归档记录，但当前无统一跟进表。
- 来源：调研批次7/8 + A-02 v1.2

**C·存在性确认**：
- 有实体交付物（Excel/邮件记录），但未标准化，未纳入数据表清单。
- 来源：调研批次8

**D·规则层记录**：
[空白，待访谈]

**P0规范化要求**：
无

**与三件套对照**：
A-02已覆盖签约完成判断标准，但未覆盖合约跟进的数据化。→ **未覆盖**

---

#### 熔断节点 · 不纳入规则空白地图

---
**规则空白编号：IBRD-熔断-001**
**优先级：熔断**
**规则主题：VN-EQ-01 同行经代服务方案（P1熔断，不进入分析）**
**关联L3：L3-SSD（同行经代服务方案E2E）**
**关联L4：SSD-01 服务方案框架设计 / SSD-02 个性化方案编写与评审**
**关联价值节点：VN-EQ-01**
**关联数据表/字段：—**

**A·固定锚点**：
- VN编码：VN-EQ-01
- V3.14状态：🔴 P1熔断（Gate①FAIL / Gate②PARTIAL / Gate③FAIL）
- 物理形态：Word/PPT方案文件

**B·调研前预填**：
- 价值节点清单裁定：P1熔断（个性化方案缺失，数据验证未通过）。
- 构成子产物：《服务方案框架设计》+《个性化方案编写与评审》。
- 生产方：权益/BD团队。
- 来源：D1_价值节点清单_V3.14 Sheet1 + Sheet2

**C·存在性确认**：
- 框架方案可能存在，但个性化方案缺失，无数据验证机制。
- 来源：D1_价值节点清单_V3.14

**D·规则层记录**：
[熔断节点，不进入三层递进。需先补建物理产物模板，完成首次交付后复评解除熔断。]

**P0规范化要求**：
不适用

**与三件套对照**：
三件套聚焦VN-IBRD-01，未覆盖VN-EQ-01。

---
**规则空白编号：IBRD-熔断-002**
**优先级：熔断**
**规则主题：VN-URD-01 联合运营需求诊断报告（P1熔断，仅参考）**
**关联L3：L3-URD（联合运营需求诊断E2E）**
**关联L4：L4-URD-05 联合运营需求诊断**
**关联价值节点：VN-URD-01**
**关联数据表/字段：—**

**A·固定锚点**：
- VN编码：VN-URD-01
- V3.14状态：🔴 P1熔断（三Gate全FAIL）
- 物理形态：Word/PDF报告包（五报告合订）

**B·调研前预填**：
- 价值节点清单裁定：P1熔断，蓝图V1.2确认流程完全缺失，概念阶段。
- 调研批次8确认：联合运营需合作很长一段时间后才能判断，无前置诊断标准；很多同行是"烟雾弹"。
- 起点A依赖L3-IBRD输出《尽职调查执行记录》+《业务目标量化》。
- 来源：D1_价值节点清单_V3.14 + 调研批次8

**C·存在性确认**：
- 五份报告均无标准模板，无历史交付记录，无数据挂钩。
- 来源：D1_价值节点清单_V3.14

**D·规则层记录**：
[熔断节点，不进入三层递进。需先完成产品定义与客户画像，再决定是否纳入流程库。]

**P0规范化要求**：
不适用

**与三件套对照**：
三件套未覆盖VN-URD-01。

---

## 四、汇总统计

### 4.1 规则空白优先级分布

| 优先级 | 条数 | 核心主题 |
|:---:|:---:|:---|
| **P0** | 4 | dim_partner分类与状态流转(2条)、dim_license牌照映射(1条)、config+partner路由档位联动(1条) |
| **P1** | 5 | dim_binder_agreement协议映射(2条)、config_routing冲突检查(1条)、partner_tier档位规则(1条)、map_payee佣金拆分(1条) |
| **P2** | 3 | dim_payee最低起付(1条)、SLHK登记表数据化(1条)、合约跟进表数据化(1条) |
| **熔断** | 2 | VN-EQ-01服务方案(1条)、VN-URD-01联合运营诊断(1条) |
| **合计** | **14** | — |

### 4.2 数据表覆盖分布

| 数据表 | P0 | P1 | P2 | 备注 |
|:---|:---:|:---:|:---:|:---|
| dim_partner | 2 | 0 | 0 | 准入分类+状态流转 |
| dim_license | 1 | 0 | 0 | 牌照映射+有效期 |
| config_partner_routing | 1 | 1 | 0 | 路由联动+冲突检查 |
| partner_tier_rules | 1 | 1 | 0 | 档位联动+匹配规则 |
| dim_binder_agreement | 0 | 2 | 0 | 协议映射+有效期管理 |
| map_partner_payee | 0 | 1 | 0 | 佣金拆分 |
| dim_payee | 0 | 0 | 1 | 最低起付 |
| [建议新建] | 0 | 0 | 2 | SLHK登记表+合约跟进表 |

### 4.3 三件套已覆盖 vs 新识别对比说明

#### 已覆盖（三件套已书面化，不重复纳入规则空白地图）

| 规则内容 | 三件套出处 | 覆盖状态 |
|:---|:---|:---:|
| JF/UNIVIN/DW三条合作路径判断标准 | A-02 v1.2 §2.2 | ✅ 已覆盖 |
| 牌照类型判断（资管→DW/经纪→JF/UNIVIN） | A-02 v1.2 判断节点0 | ✅ 已覆盖 |
| 永明合约状态查询流程（Alice查询） | A-02 v1.2 判断节点1 + B-01 v1.1 Q-12 | ✅ 已覆盖 |
| JF↔UNIVIN切换规则（取消永明合约） | A-02 v1.2 判断节点1a | ✅ 已覆盖 |
| 前端→中台转介信息标准（A/B/C/D类字段） | B-01 v1.1 §三 | ✅ 已覆盖 |
| 最低准入门槛（4条） | B-01 v1.1 §二 | ✅ 已覆盖 |
| 中台收件确认5步流程 | B-01 v1.1 §四 | ✅ 已覆盖 |
| 尽调执行记录6类字段（E/F/G/H/I/J） | A-03 v1.1 §三 | ✅ 已覆盖 |
| 尽调审核链（Terresa+RO2） | A-03 v1.1 J类 + Q-24 | ✅ 已覆盖 |
| 尽调归属L3-IBRD裁定 | A-03 v1.1 Q-05 | ✅ 已覆盖 |
| 退回与关闭机制（一季度观察期） | B-01 v1.1 Q-16 | ✅ 已覆盖 |
| 江通线/白博文线来源分流 | A-02 v1.2 §2.4 + Case3 | ✅ 已覆盖 |
| 交付经理职责边界（艾米/陈浩凯不参与） | A-02 v1.2 Case4 + Q-09 | ✅ 已覆盖 |

#### 新识别（三件套未覆盖，本次第一层产出）

| 规则空白编号 | 规则主题 | 缺口类型 |
|:---|:---|:---:|
| IBRD-P0-001 | dim_partner.partner_category同行经代枚举定义 | ❌ 数据规则缺口 |
| IBRD-P0-002 | dim_partner.partner_status状态流转与尽调结论映射 | ❌ 数据规则缺口 |
| IBRD-P0-003 | dim_license.license_type与IBRD路径数据表映射 | ❌ 数据规则缺口 |
| IBRD-P0-004 | config_partner_routing + partner_tier_rules同行经代联动配置 | ❌ 数据规则缺口 |
| IBRD-P1-001 | dim_binder_agreement.agreement_type同行经代协议映射 | ❌ 数据规则缺口 |
| IBRD-P1-002 | config_partner_routing.priority冲突检查机制 | ❌ 数据规则缺口 |
| IBRD-P1-003 | partner_tier_rules.partner_category档位匹配规则 | ❌ 数据规则缺口 |
| IBRD-P1-004 | map_partner_payee.split_ratio佣金拆分规则 | ❌ 数据规则缺口 |
| IBRD-P1-005 | dim_binder_agreement有效期管理与续约触发 | ❌ 数据规则缺口 |
| IBRD-P2-001 | dim_payee.min_payout_threshold最低起付规则 | ❌ 数据规则缺口 |
| IBRD-P2-002 | SLHK同行登记表数据化 | ❌ 新表建议 |
| IBRD-P2-003 | 合约跟进表数据化 | ❌ 新表建议 |

**对比说明**：
- 三件套（A-02/B-01/A-03）已完整覆盖IBRD**流程层面**的规则（合作路径判断、转介标准、尽调执行、审核链等），共计13条核心规则。
- 本次第一层分析新识别**数据表层面**规则空白12条（P0=4 / P1=5 / P2=3），主要集中在：
  1. **合作伙伴分类与状态**：dim_partner的partner_category和partner_status字段规则缺失，导致数据表无法支撑IBRD准入和生命周期管理；
  2. **牌照与路径映射**：dim_license到config_partner_routing的自动映射未建立，A-02决策树无法直接驱动数据表配置；
  3. **佣金计算核心配置**：config_partner_routing和partner_tier_rules中同行经代的专属配置规则缺失，直接影响佣金结算准确性；
  4. **协议与拆分规则**：dim_binder_agreement和map_partner_payee中同行经代的业务规则未定义；
  5. **实体工具数据化**：SLHK登记表和合约跟进表为实际管理工具但无数据表支撑。

---

## 五、附加观察

> 以下发现不纳入规则空白地图正文，仅作记录供后续任务参考。

### 5.1 建议新建的IBRD专属表

| 建议表名 | 表类型 | 核心字段 | 建议来源 | 优先级 |
|:---|:---|:---|:---|:---:|
| slhk_partner_registry（SLHK同行登记表） | 过程表 | partner_name, broker_name, license_no, source_line, profile_desc, registration_date, follow_up_status, registered_by | 调研批次8（MoMo确认存在，三人同步维护） | P2 |
| contract_follow_up（合约跟进表） | 过程表 | partner_code, contract_status, contract_send_date, contract_return_date, sign_entity, follow_up_reminder, contract_version, reminder_30d, reminder_60d, reminder_90d | 调研批次7/8（合同签回周期1-2个月，需激活提醒） | P2 |
| dd_form_registry（DD Form归档索引） | 过程表 | partner_code, dd_form_version, dd_send_date, dd_return_date, dd_status, co_risk_level, terresa_review_date, ro_sign_date | A-03 v1.1（DD Form为核心交付物，需结构化归档） | P2 |

### 5.2 调研记录中超出VN-IBRD范围的线索

| 线索 | 涉及L3/VN | 说明 | 建议处理 |
|:---|:---|:---|:---|
| 联合运营产品化不足 | L3-URD / VN-URD-01 | 无客户画像、无PPT、无触发条件 | 纳入URD域补建任务 |
| 白博文线合同后置 | L3-IBRD / L3-NG | 根因为内商务岗位缺失，非策略选择 | 已在三件套A-02 Case3记录，建议Mark决策岗位设置 |
| 喇叭位系统bug多 | L3-IBRD / L3-NG | 录单困难，权益发放纯手工 | IT问题，建议纳入系统优化清单 |
| BD画像表填不回来 | L3-IBEC / L3-IBRD | 前端渠道筛选标准不明，信息质量参差 | 已在B-01 v1.1准入门槛和退回机制中覆盖 |

### 5.3 IBEC/URD与IBRD的交叉点（仅参考标注）

| 交叉点 | IBRD侧 | IBEC/URD侧 | 影响 |
|:---|:---|:---|:---|
| SLHK登记表归属 | VN-IBRD-01备注提及，建议纳入IBRD数据化 | L3-IBEC实际为前端流程，但MoMo深度参与牌照核查 | **边界模糊**：SLHK登记表应归属IBRD还是IBEC？建议按"首次接触后建档"归属IBRD |
| 联合运营判断输入 | VN-IBRD-01输出《尽职调查执行记录》为VN-URD-01起点A | VN-URD-01依赖IBRD输出作为输入 | **依赖关系**：URD无法独立运行，需IBRD先完成补建 |
| 合同后置根因 | IBRD调研确认内商务岗位缺失导致合同后置 | KA侧（VN-KASC-01）同样存在合同后置 | **共性问题**：合同后置是跨域现象，根因相同（内商务岗位缺失），建议统一决策 |

---

## 六、自检声明

### 6.1 Done Criteria 逐项自检

| # | 检查项 | 状态 | 依据 |
|:---:|:---|:---:|:---|
| 1 | 全部输入文件已完整读取 | ✅ | 方法论v2.4 + D1_V3.14 + 调研V1.1 + 合作伙伴数据表 + 三件套 + Gate报告 |
| 2 | Phase 0评估表已输出，含D评级和进入判定 | ✅ | §一 Phase 0评估表 |
| 3 | VN-IBRD-01补建后状态已正确标注 | ✅ | D评级=D2（🟢通过），引用Gate重新验证报告v1.0，不以V3.14原始熔断状态为准 |
| 4 | IBRD数据表索引已输出，KA专属表已排除 | ✅ | §二 数据表索引，dim_ka和bridge_partner_ka已排除，标注"KA专属·已排除" |
| 5 | 每条规则空白含A/B/C/D四组列+P0规范化+与三件套对照 | ✅ | §三 规则空白地图，每条均含A·固定锚点/B·调研前预填/C·存在性确认/D·规则层记录/P0规范化要求/与三件套对照 |
| 6 | 规则空白编号使用IBRD-P0/P1/P2格式 | ✅ | P0=4条（IBRD-P0-001~004），P1=5条（IBRD-P1-001~005），P2=3条（IBRD-P2-001~003） |
| 7 | 汇总统计表已输出 | ✅ | §四 汇总统计（优先级分布/数据表覆盖/三件套对比） |
| 8 | 三件套已覆盖vs新识别的对比说明已输出 | ✅ | §4.3 对比说明，含已覆盖13条清单 + 新识别12条清单 |
| 9 | 附加观察已产出 | ✅ | §五 附加观察（建议新建表/调研超出线索/IBEC-URD交叉点） |
| 10 | 输出文件已存入延展_同行经代NBRD/路径 | ✅ | 本文件路径：02_过程成果-工作产出/规则分析/延展_同行经代NBRD/ |
| 11 | 自检声明：已对照Done Criteria逐项自检 | ✅ | 本声明 |

### 6.2 边界合规确认

- [x] 未修改任何输入文件
- [x] KA数据分析不在本次范围（dim_ka/bridge_partner_ka已排除）
- [x] IBEC/URD只作参考，未产出其四标签（仅作交叉点标注）
- [x] 未执行访谈，仅产出规则空白地图（D列留空）
- [x] 三件套中已识别的流程规则只做标注，未重复纳入规则空白地图
- [x] VN-IBRD-01已引用Gate重新验证报告v1.0，不以V3.14原始熔断状态为准

---

> **任务包**：TASK-M4W10-060 | **执行终端**：Kimi | **授权人**：Jasper（待确认）
> **生成时间**：2026-06-04
> **版本**：V1.0
