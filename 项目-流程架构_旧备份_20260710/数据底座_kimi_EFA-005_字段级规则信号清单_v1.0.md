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

# EFA-005 · 字段级规则信号清单 v1.0

> 任务编号：TASK-EFA-005 | 执行依据：数据规则提取方法论_三层递进提取法_v2.1
> 命中规则：C1=数据来源=人工录入且非空=是 | C2=计算口径含手工录入 | C3=更新频率=按需/规则变更 | C4=Owner=Steward | C5=质量规则含ALL/枚举值

| 表名英文 | 表名中文 | 字段英文名 | 字段中文名 | 数据来源 | Data Owner | Data Steward | 命中规则信号 | 对应评分维度 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| DIM_PRODUCT_SKU | 产品SKU列表 | Update_Date | 更新时间 | 人工录入 | 产品专员 | Mia | C1,C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Product_SKU | 产品大类代码 | 人工录入 | 产品专员 | Mia | C1,C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Carrier_Code | 保司代码 | DIM_CARRIER | 产品专员 | Mia | C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Chinese_Standard_Name | 标准化的产品中文名 | 人工录入 | 产品专员 | Mia | C1,C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | English_Standard_Name | 标准化的产品英文名 | 人工录入 | 产品专员 | Mia | C1,C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Product_Category | 产品险种 | 计划书/产品手册 | 产品专员 | Mia | C3,C5 | D1,D2 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Product_Type | 产品类型 | 保司佣金PDF文件 | 产品专员 | Mia | C3,C5 | D1,D2 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Business_Line | 所属业务线分类 | 人工录入 | 产品专员 | Mia | C1,C3,C5 | D1,D2 |
| DIM_PRODUCT_SKU | 产品SKU列表 | product_Unite_Grid | 所属产品单元 | 人工录入 | 产品专员 | Mia | C2,C3 | D1,D2 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Is_Offshore | 离岸标识 | 人工录入 | 产品专员 | Mia | C1,C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Is_Premium_Financing | 融资标识 | 保险公司 | 产品专员 | Mia | C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Clawback_Period_Months | 退保追佣期 | 保司佣金PDF文件 | 产品专员 | Mia | C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Cooling_Off_Days | 冷静期天数 | 产品手册 | 产品专员 | Mia | C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Currency_Link_Rule | 币种连接 | 产品手册 | 产品专员 | Mia | C3 | D1 |
| DIM_PRODUCT_SKU | 产品SKU列表 | Product_Risk_Level | 风险评级 | 人工录入 | 产品专员 | Mia | C2,C3 | D1,D2 |
| DIM_PRODUCT_ID | 产品ID列表 | Update_Date | 更新时间 | 人工录入 | 产品专员 | Mia | C1,C3 | D1 |
| DIM_PRODUCT_ID | 产品ID列表 | Product_ID_SK | 产品子表主键 | 人工录入 | 产品专员 | Mia | C1,C3 | D1 |
| DIM_PRODUCT_ID | 产品ID列表 | Product_ID | 产品ID | 人工录入 | 产品专员 | Mia | C1,C2,C3 | D1,D2 |
| DIM_PRODUCT_ID | 产品ID列表 | Product_SKU | 所属大类外键 | DIM_PRODUCT_SKU | 产品专员 | Mia | C3 | D1 |
| DIM_PRODUCT_ID | 产品ID列表 | Chinese_Product_Name | 产品中文名 | 保司佣金PDF文件 | 产品专员 | Mia | C2,C3 | D1,D2 |
| DIM_PRODUCT_ID | 产品ID列表 | English_Product_Name | 产品英文名 | 保司佣金PDF文件 | 产品专员 | Mia | C2,C3 | D1,D2 |
| DIM_PRODUCT_ID | 产品ID列表 | Rate_Option_Code | 特殊折扣 | RO/保司 | 产品专员 | Mia | C2,C3 | D1,D2 |
| DIM_PRODUCT_ID | 产品ID列表 | Premium_Term | 缴费期 | 产品手册 | 产品专员 | Mia | C2,C3 | D1,D2 |
| DIM_PRODUCT_ID | 产品ID列表 | Benefit_Term | 保障期限 | 产品手册 | 产品专员 | Mia | C2,C3 | D1,D2 |
| DIM_PRODUCT_ID | 产品ID列表 | Is_Active | 上架状态 | 保司佣金PDF文件 | 产品专员 | Mia | C3 | D1 |
| DIM_PRODUCT_ID | 产品ID列表 | Product_Risk_Level | 风险评级 | 人工录入 | 产品专员 | Mia | C2,C3 | D1,D2 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | Carrier | 保司代码 | 手工录入 | 刘敏然 | MOMO | C3 | D1 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | license_type | 牌照类型 | 手工录入 | 刘敏然 | MOMO | C3,C5 | D1,D2 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | customer_type | 客户分群 | 手工录入 | 刘敏然 | MOMO | C3 | D1 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | first_year_formula | 首年佣金公式 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | renewal_year_formula | 续期佣金公式 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | basic_rate_from | Basic取值来源 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | extra_rate_from | Extra取值来源 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| CONFIG_PRODUCT_COMMISSION_FORMULA | 产品佣金计算公式 | smpa_rate_from | SMPA取值来源 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | License_Code | 牌照代码 | RO/保司邮件 | 刘敏然 | MOMO | C3 | D1 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | Carrier_Code | 保司Code | RO/保司邮件 | 刘敏然 | MOMO | C3 | D1 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | commission_plan_code | 佣金准入表名 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | Effective_From | 有效期从 | 保司佣金文件 | 刘敏然 | MOMO | C3 | D1 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | Effective_To | 有效期至 | 保司佣金文件 | 刘敏然 | MOMO | C3 | D1 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | Is_Active | 是否有效 | 手工录入 | 刘敏然 | MOMO | C3 | D1 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | Last_Updated_By | 最后更新人 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| CONFIG_LICENSE_CARRIER_MAPPING | 牌照保司路由 | Remarks | 备注 | 手工录入 | 刘敏然 | MOMO | C2,C3 | D1,D2 |
| FACT_COMMISSION_RATE | 佣金事实表 | license_type | 牌照资质类别 | Config_License_Carrier_Mapping | 刘敏然 | MOMO | C5 | D2 |
| FACT_COMMISSION_RATE | 佣金事实表 | customer_type | 客户分群 | 佣金准入表 | 刘敏然 | MOMO | C5 | D2 |
| FACT_COMMISSION_RATE | 佣金事实表 | tier_code | 佣金档位 | 佣金准入表 | 刘敏然 | MOMO | C5 | D2 |
| FACT_COMMISSION_RATE | 佣金事实表 | issue_cutoff_date | 批核截止日期 | 佣金准入表 | 刘敏然 | MOMO | C5 | D2 |
| FACT_COMMISSION_RATE | 佣金事实表 | effective_start_date | 费率生效日期 | 人工录入 | 刘敏然 | MOMO | C1 | D1 |
| FACT_COMMISSION_RATE | 佣金事实表 | effective_end_date | 费率失效日期 | 人工录入 | 刘敏然 | MOMO | C1 | D1 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Routing_rules_ID | 路由规则ID | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | priority | 优先级 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Partner_code_Condition | 合作伙伴编码条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Partner_Category_Condition | 合作伙伴分类条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Commission_Pattern | 佣金模式 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | carrier_code_Condition | 保险公司条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Bussiness_Line_comdition | 产品业务线条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Product_Condition | 产品条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Assigned_license_code | 分配牌照编码 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | Is_Active | 是否启用 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_PARTNER_ROUTING | 合作伙伴保司牌照路由规则 | remark | 备注 | 人工录入 | MOMO | MOMO | C3,C4 | D1,D6 |
| Product_Risk_Override | 产品属性覆写路由 | Product_SKU | 产品SKU | 业务配置 | MOMO | MOMO | C3,C4 | D1,D6 |
| Product_Risk_Override | 产品属性覆写路由 | Product_ID | 产品ID | 业务配置 | MOMO | MOMO | C3,C4,C5 | D1,D2,D6 |
| Product_Risk_Override | 产品属性覆写路由 | Rate_Option_Code | 计价选项编码 | 业务配置 | MOMO | MOMO | C3,C4 | D1,D6 |
| Product_Risk_Override | 产品属性覆写路由 | Mapped_Business_Line | 原始产品线 | 业务配置 | MOMO | MOMO | C3,C4,C5 | D1,D2,D6 |
| Product_Risk_Override | 产品属性覆写路由 | Target_Business_Line | 目标产品线 | 业务配置 | MOMO | MOMO | C2,C3,C4 | D1,D2,D6 |
| Product_Risk_Override | 产品属性覆写路由 | Mapped_PUG | 原始PUG | 业务配置 | MOMO | MOMO | C3,C4 | D1,D6 |
| Product_Risk_Override | 产品属性覆写路由 | Target_PUG | 目标PUG | 业务配置 | MOMO | MOMO | C3,C4 | D1,D6 |
| Product_Risk_Override | 产品属性覆写路由 | remark | 备注 | 业务配置 | MOMO | MOMO | C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Priority | 优先级 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Partner_code | 合作伙伴编码 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Carrier_Code_Condition | 保司代码条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Partner_Category | 合作伙伴分类 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Customer_Type | 客户分类 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Bussiness_Line_Condition | 业务线条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Product_Unit_Condition | 产品单元条件 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | FYC_Tier | 首年佣金分层 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | RYC_Tier | 续年佣金分层 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | FYC_Adjustment | 首年佣金调整系数 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | RYC_Adjustment | 续年佣金调整系数 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Fixed_Fee_Rate | 固定费用费率 | 人工录入 | MOMO | MOMO | C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Effective_Date_Type | 日期类型 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | effective_date | 有效期从 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | expiry_date | 有效期至 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| Partner_Tier_Rules | 合作伙伴档位佣金规则 | Description | 规则说明 | 人工录入 | MOMO | MOMO | C3,C4 | D1,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | business_category | 业务分类 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | table_type | 制表类型 | 人工录入 | MOMO | MOMO | C1,C2,C3,C4 | D1,D2,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | excluded_carrier_code | 排除的保司 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | excluded_bussiness_line | 排除的产品线 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | excluded_product_pgu | 排除的产品PGU | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | excluded_product_sku | 排除的产品SKU | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | excluded_product_id | 排除的产品ID | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | excluded_rate_option_code | 排除的产品计价选项 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | is_active | 是否有效 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_PRODUCT_EXCLUSION_RANGE | 产品排除范围配置 | remark | 备注说明 | 人工录入 | MOMO | MOMO | C3,C4 | D1,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | business_category | 业务分类 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | table_type | 制表类型 | 人工录入 | MOMO | MOMO | C1,C2,C3,C4 | D1,D2,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | partner_code | 合作伙伴代码 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | partner_name | 合作伙伴名称 | 人工录入 | MOMO | MOMO | C1,C2,C3,C4 | D1,D2,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | partner_category | 合作伙伴分类 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | commission_pattern | 佣金模式 | 人工录入 | MOMO | MOMO | C1,C3,C4,C5 | D1,D2,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | customer_type | 客户分类 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | main_license_code | 主签牌照 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | commission_date | 佣金日期 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
| CONFIG_COMMISSION_TABLE_TYPE | 市场佣金制表参数 | commission_duration | 佣金所属期 | 人工录入 | MOMO | MOMO | C1,C3,C4 | D1,D6 |
