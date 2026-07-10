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

# 任务包：TASK-HR001
## HR域 · 三层递进提取法第一层产出
## 30张表全量四标签分析 + 规则空白地图
> 版本：V1.0 | 授权人：Jasper | 执行终端：Kimi | 日期：2026-05-19
> 前置方法论：数据规则提取方法论_三层递进提取法_v2.1.md
> 执行情景：**情景1（纯路径A）** · 无调研记录 · 无需P4调研交叉填充 · 规则空白地图不设调研状态列

---

## 一、任务定位

**业务域**：人力资源域（HR）
**分析范围**：30张表 · 386个字段
**上游参照**：HR星型模型_数据字典_v2_3.xlsx（Sheet1表概览 + Sheet2字段字典 + Sheet3快速编码 + Sheet4 KPI）
**全景图参照**：HR数据模型_全景图_v1_0.png（数据链关系参照，C标签使用）

---

## 二、30张表完整清单与元数据

### 数据链分层（执行C标签时的参照顺序）

```
【配置/字典层】（参数开关）
  dim_lookup_code（快码字典）
  config_score_coefficient（评分→奖金系数）
  config_position_alias（岗位归一映射）
  dim_position_grade（职级维度）
  dim_salary_band（薪酬带宽，★新建）
  bridge_position_grade（岗位×职级桥接，★新建）

【维度层】（16+1张）
  dim_employee（员工）         dim_date（日期）
  dim_organization（组织）     dim_business_unit（业务机构）
  dim_legal_entity（法人）     dim_position（岗位，★v2.3瘦身）
  dim_contract（合同）         dim_reporting（汇报关系）
  dim_segmentation（业务细分） dim_ka（KA）
  dim_bonus_pool（绩效包）     dim_job_family（岗位族，★重构）
  dim_salary_component（薪资项，★升级）
  dim_insurance_type（保险类型，★升级）

【事实层】（9张）
  fact_emp_monthly（员工月度快照，16字段）
  fact_employee_events（员工异动事件，12字段）
  consistency_check（一致性校验，9字段）← 质量监控表
  fact_attendance_monthly（月度考勤，53字段）← Phase 1
  fact_salary_monthly（月度薪资主表，25字段）← Phase 2
  fact_salary_tax_detail（个税明细，16字段）← Phase 2
  fact_social_insurance_monthly（月度社保公积金，26字段）← Phase 2
  fact_performance_eval（绩效评估，15字段）← Phase 3
  fact_bonus_calculation（绩效奖金核算，20字段）← Phase 3

【聚合层】（1张）
  AGG_labor_cost_monthly（人工成本月度聚合，25字段）← Phase 4·财务源头
```

### 全量表元数据（执行四标签时的依据）

| 表名(英文) | 表名(中文) | 表类型 | 字段数 | 状态 | Data Owner | 数据分工 | 审核状态 |
|---|---|---|---|---|---|---|---|
| fact_emp_monthly | 员工月度快照事实表 | 事实表 | 16 | v2.3 | HRD | IT数据团队 | 已实施 |
| fact_employee_events | 员工异动事件事实表 | 事实表 | 12 | v2.3 | HRD | IT数据团队 | 已实施 |
| consistency_check | 事件-快照一致性校验表 | 质量监控表 | 9 | v2.3 | HRD | IT数据团队 | 已实施 |
| fact_attendance_monthly | 月度考勤事实表 | 事实表 | 53 | Phase1(v2.4) | HRD | IT数据团队 | 待实施 |
| fact_salary_monthly | 月度薪资主事实表 | 事实表 | 25 | Phase2(v2.5) | HRD | IT数据团队 | 待实施 |
| fact_salary_tax_detail | 个税计算细节事实表 | 事实表 | 16 | Phase2(v2.5) | HRD | IT数据团队 | 待实施 |
| fact_social_insurance_monthly | 月度社保公积金事实表 | 事实表 | 26 | Phase2(v2.5) | HRD | IT数据团队 | 待实施 |
| fact_performance_eval | 员工绩效评估事实表 | 事实表 | 15 | Phase3(v2.6) | HRD | IT数据团队 | 待实施 |
| fact_bonus_calculation | 绩效奖金核算事实表 | 事实表 | 20 | Phase3(v2.6) | HRD | IT数据团队 | 待实施 |
| dim_employee | 员工维度 | 维度表 | 23 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_date | 日期维度 | 维度表 | 6 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_organization | 组织维度 | 维度表 | 7 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_business_unit | 业务机构维度 | 维度表 | 4 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_legal_entity | 法人主体维度 | 维度表 | 5 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_position | 岗位维度(★瘦身) | 维度表 | 16 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_contract | 员工合同维度 | 维度表 | 11 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_reporting | 汇报关系维度 | 维度表 | 9 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_segmentation | 业务细分维度 | 维度表 | 6 | v2.3 | BizD | HR业务方 | 已实施 |
| dim_ka | KEY ACCOUNT维度 | 维度表 | 18 | v2.3 | BizD | HR业务方 | 已实施 |
| dim_bonus_pool | 部门绩效包维度 | 维度表 | 8 | Phase3(v2.6) | HRD | HR业务方 | 待实施 |
| dim_job_family | 岗位族维度(★重构) | 维度表 | 8 | v2.3 | HRD | HR业务方 | 已实施 |
| dim_salary_component | 薪资项维度(★升级) | 维度表 | 6 | Phase2(v2.5) | HRD | HR业务方 | 待实施 |
| dim_insurance_type | 保险类型维度(★升级) | 维度表 | 5 | Phase2(v2.5) | HRD | HR业务方 | 待实施 |
| dim_salary_band | 薪酬带宽维度(★新建) | 维度表 | 6 | 待实施 | HRD | HR业务方 | 待实施 |
| bridge_position_grade | 岗位职级桥接表(★新建) | 桥接表 | 7 | 待实施 | HRD | IT数据团队 | 待实施 |
| dim_lookup_code | 全公司快码字典 | 字典表 | 5(×170条) | v2.3 | HRD | 数据治理 | 已实施 |
| dim_position_grade | 职级维度(★改名升级) | 维度表 | 7 | v2.3 | HRD | HR业务方 | 已实施 |
| config_score_coefficient | 评分→奖金系数转换表 | 配置表 | 3 | Phase3(v2.6) | HRD | HR业务方 | 待实施 |
| config_position_alias | 岗位归一映射 | 配置表 | 9 | v2.3 | HRD | HR业务方 | 已实施 |
| AGG_labor_cost_monthly | 人工成本月度聚合表 | 聚合表 | 25 | Phase4(v2.7) | HRD | IT数据团队 | 待实施 |

---

## 三、全量字段清单（四标签B执行依据）

### fact_emp_monthly（16字段）
| 字段(英文) | 字段(中文) | 数据来源 | 更新频率 | 非空 | 约束/关系 | Data Owner |
|---|---|---|---|---|---|---|
| snapshot_key | 快照主键 | ETL生成 | 月度 | 是 | PK | HRD |
| date_key | 日期键 | HR-001/002 | 月度 | 是 | FK→dim_date | HRD |
| employee_key | 员工键 | HR-001 | 月度 | 是 | FK→dim_employee | HRD |
| legal_entity_key | 法人键 | HR-001 | 月度 | 是 | FK→dim_legal_entity | HRD |
| business_unit_key | 业务机构键 | HR-002 | 月度 | 是 | FK→dim_business_unit | HRD |
| organization_key | 组织键 | HR-002 | 月度 | 是 | FK→dim_organization | HRD |
| position_key | 岗位键 | HR-001 | 月度 | 是 | FK→dim_position | HRD |
| grade_code | 实际任职职级 | HR-001 | 月度 | 否 | FK→dim_position_grade | HRD |
| segment_code | 业务细分 | HR-002 | 月度 | 否 | FK→dim_segmentation | HRD |
| is_active | 是否在职 | HR-001 | 月度 | 是 | 布尔 | HRD |
| is_new_hire_this_month | 当月新入职 | ETL计算 | 月度 | 是 | 布尔 | HRD |
| is_terminated_this_month | 当月离职 | ETL计算 | 月度 | 是 | 布尔 | HRD |
| tenure_days | 在职天数 | ETL计算 | 月度 | 否 | ≥0 | HRD |
| employment_type | 雇佣类型 | HR-001 | 月度 | 是 | 枚举(正式/顾问/实习等) | HRD |
| contract_region | 合同地域 | HR-001 | 月度 | 是 | 枚举(HK/SZ/BJ等) | HRD |
| etl_load_date | ETL入仓时间 | ETL自动 | 月度 | 是 | TIMESTAMP | HRD |

### fact_employee_events（12字段）
| 字段(英文) | 字段(中文) | 数据来源 | 更新频率 | 约束/关系 |
|---|---|---|---|---|
| event_key | 事件主键 | ETL生成 | 事件触发 | PK |
| employee_key | 员工键 | HR-001 | 事件触发 | FK→dim_employee |
| event_date | 事件日期 | HR-001/002 | 事件触发 | DATE NOT NULL |
| event_type | 事件类型 | HR-001/002 | 事件触发 | 枚举(入职/离职/调岗/晋升等) |
| from_value | 变更前值 | HR-001/002 | 事件触发 | VARCHAR |
| to_value | 变更后值 | HR-001/002 | 事件触发 | VARCHAR |
| reason | 异动原因 | HR-001/002 | 事件触发 | VARCHAR |
| approver | 审批人 | HR-001/002 | 事件触发 | VARCHAR |
| related_entity_type | 关联实体类型 | ETL计算 | 事件触发 | 枚举 |
| snapshot_check_status | 快照核对状态 | ETL计算 | 事件触发 | 枚举(通过/差异/未校验) |
| remarks | 备注 | HR-001/002 | 事件触发 | VARCHAR |
| etl_load_date | ETL入仓时间 | ETL自动 | 事件触发 | TIMESTAMP |

### consistency_check（9字段）
| 字段(英文) | 字段(中文) | 数据来源 | 更新频率 |
|---|---|---|---|
| check_key | 校验主键 | ETL生成 | 每次校验 |
| employee_key | 员工键 | ETL自动 | 每次校验 |
| check_date | 校验日期 | ETL自动 | 每次校验 |
| check_type | 校验类型 | ETL自动 | 每次校验 |
| snapshot_value | 快照值 | fact_emp_monthly | 每次校验 |
| event_value | 事件值 | fact_employee_events | 每次校验 |
| check_result | 校验结果 | ETL自动 | 每次校验 |
| description | 描述 | ETL自动 | 每次校验 |
| etl_load_date | ETL入仓时间 | ETL自动 | 每次校验 |

### fact_attendance_monthly（53字段）
attendance_key / employee_id / date_key / period_start / period_end / rule_name / required_days / actual_days / rest_days / normal_days / exception_days / standard_hours / actual_hours / exception_total / late_times / late_minutes / early_times / early_minutes / absence_times / absence_minutes / missing_punch_times / location_err_times / device_err_times / supplemented_punch / approval_punch / field_work_days / outing_hours / travel_days / annual_leave_days / personal_leave_days / sick_leave_days / overtime_leave_hrs / marriage_leave_days / maternity_leave_days / paternity_leave_days / other_leave_days / ot_total_hours / weekday_ot_hours / weekday_ot_toil / weekday_ot_pay / weekend_ot_hours / weekend_ot_toil / weekend_ot_pay / holiday_ot_hours / holiday_ot_toil / holiday_ot_pay / hk_annual_balance / sz_annual_balance_cur / sz_annual_balance_prev / data_quality_flag / source_file / etl_load_date / etl_batch_id
（全部来源：HR-003，频率：月度；最后3字段ETL生成）

### fact_salary_monthly（25字段）
salary_key(ETL生成) / employee_id(HR-004) / date_key(HR-004) / legal_entity_key(HR-004) / contract_id(ETL关联) / contract_region(dim_employee) / currency(HR-004) / basic_salary(HR-004) / attendance_deduction(HR-004) / allowance(HR-004) / performance_bonus(HR-004) / floating_bonus(HR-004) / overtime_pay(HR-004) / other_income(HR-004) / gross_salary(HR-004) / social_insurance_company(HR-004) / social_insurance_personal(HR-004) / housing_fund_company(HR-004) / housing_fund_personal(HR-004) / total_deduction(HR-004) / personal_income_tax(HR-004) / net_salary(HR-004) / data_quality_flag(ETL计算) / source_file(ETL记录) / etl_load_date(ETL自动)

### fact_salary_tax_detail（16字段）
tax_detail_key / employee_id / date_key / salary_key / special_deduction_children / special_deduction_edu / special_deduction_mortgage / special_deduction_rent / special_deduction_elderly / special_deduction_total(ETL计算) / cumulative_taxable_income / withholding_rate / quick_deduction / cumulative_tax_payable / cumulative_tax_paid / monthly_tax_amount
（来源：HR-004；频率：月度）

### fact_social_insurance_monthly（26字段）
social_key / employee_id / date_key / city / social_base / pension_company / pension_local_supplement / pension_personal / unemployment_company / unemployment_personal / medical_company / medical_personal / maternity_company / injury_company / social_company_total / social_personal_total / housing_fund_base / housing_fund_company / housing_fund_personal / insurance_type_code(枚举→FK) / backpay_months / backpay_personal / backpay_company / backpay_local / remarks / etl_load_date
（来源：HR-007；频率：月度）

### fact_performance_eval（15字段）
eval_key / employee_id / cycle_id / cycle_type(枚举) / attitude_score_1 / attitude_score_2 / ability_score_1 / ability_score_2 / achievement_score_1 / achievement_score_2 / achievement_score_3 / total_weighted_score(ETL计算) / bonus_coefficient(ETL计算，FK→config_score_coefficient) / appraiser_name / eval_date
（来源：HR-005；频率：季度）

### fact_bonus_calculation（20字段）
bonus_key / employee_id / date_key / bonus_pool_id(ETL关联) / monthly_salary_standard / currency / hire_adjustment / probation_adjustment / base_30pct / dept_coefficient / q_bonus_pool_local / q_bonus_pool_hkd / emp_coefficient_1 / emp_coefficient_2 / adjustment_hkd / bonus_amount_local / bonus_amount_hkd / data_quality_flag(ETL计算) / source_file(ETL记录) / etl_load_date
（来源：HR-006；频率：季度）

### dim_employee（23字段）
employee_id / name / alias_name / gender(枚举) / phone / email / birthdate / id_card_masked / first_hire_date / regularization_date / recorded_term_date / work_status(枚举) / contract_region(枚举) / employment_type(枚举) / highest_education / nationality / marital_status / emergency_contact / emergency_phone / home_address_city / hukou_type / etl_load_date / etl_update_date
（来源：HR-001；频率：低频更新；Owner：HRD）

### dim_date（6字段）
date_key / year / month / quarter / year_month_label / is_snapshot_point
（来源：一次性生成）

### dim_organization（7字段）
organization_key(ETL生成) / organization_code(HR-002) / org_module(枚举,HR-002) / dept_l1(HR-002) / dept_l2(HR-002) / effective_from(HR-002) / effective_to(HR-002)

### dim_business_unit（4字段）
business_unit_key / business_unit_name(线下定义) / business_unit_type(枚举,线下定义) / description(线下定义)

### dim_legal_entity（5字段）
legal_entity_key / canonical_name(法务台账) / full_name(法务台账) / entity_type(枚举,法务台账) / region(法务台账)

### dim_position（16字段，★v2.3瘦身：删除grade_code和salary_band字段）
position_key / position_id(岗位治理) / position_name(岗位治理) / position_name_standard(岗位治理) / career_track(枚举,岗位治理) / job_family(枚举,岗位治理) / sub_family(枚举,岗位治理) / proficiency_level(枚举,岗位治理) / position_category(岗位治理) / is_key_position(岗位治理) / is_revenue_generating(岗位治理) / current_headcount(ETL计算) / description(岗位治理) / effective_from(岗位治理) / effective_to(岗位治理) / etl_load_date

### dim_contract（11字段）
contract_key / employee_id(HR-001,FK) / contract_id(HR-001) / contract_entity_name(HR-001,枚举) / contract_type(HR-001) / contract_start_date / contract_end_date / renewal_count(ETL计算) / effective_from / effective_to / is_current

### dim_reporting（9字段）
reporting_key / employee_id(HR-001,FK) / manager_employee_id(HR-001,FK) / manager_name / reporting_type(HR-001) / reporting_level(ETL计算) / effective_from / effective_to / is_current

### dim_segmentation（6字段）
segment_code / segment_name / segment_name_en / parent_segment / description / is_active
（来源：中台已有；Owner：BizD）

### dim_ka（18字段）
ka_key / ka_id / ka_name / ka_tier / ka_grade / segment_code(FK) / market_segment(枚举) / business_support_emp_id(FK) / midoffice_support_emp_id(FK) / contact_person / contact_phone / contact_email / cooperation_start_date / annual_revenue / status / remarks / effective_from / effective_to
（来源：KA系统；Owner：BizD）

### dim_bonus_pool（8字段）
bonus_pool_id / cycle_id / organization_key(FK) / dept_name / dept_coefficient / pool_amount_hkd / allocated_amount_hkd(ETL计算) / remaining_hkd(ETL计算)
（来源：HR-006；频率：季度）

### dim_job_family（8字段，★v2.3重构）
family_code / family_name / parent_family_code(枚举,FK) / family_level / family_category / default_career_track(枚举) / is_revenue_generating / description
（来源：岗位治理）

### dim_salary_component（6字段，★v2.3升级）
component_code / component_name_cn / component_name_en / category / is_taxable / in_social_base
（来源：**人工定义**；C1全命中；频率：低频更新）

### dim_insurance_type（5字段，★v2.3升级）
insurance_code / insurance_name_cn / payer / sz_rate / remarks
（来源：**人工定义**；C1全命中）

### dim_salary_band（6字段，★v2.3新建）
band_id / grade_code(FK) / family_code(FK) / salary_band_min_hkd(外部顾问) / salary_band_max_hkd(外部顾问) / effective_date(**人工定义**,C1)

### bridge_position_grade（7字段，★v2.3新建）
position_key(FK) / grade_code(FK) / effective_from / effective_to / is_default / is_active / remarks
（来源：岗位治理；桥接表，N:1关系）

### dim_lookup_code（5字段，170条枚举值）
field / field_name_cn / code / display_name / remarks
（来源：中台快码；字典表；C5全域信号源）

### dim_position_grade（7字段，★v2.3改名升级）
grade_code / career_track_code(FK) / grade_level_num / grade_name / grade_label / （v2.3新增2字段待确认）
（来源：岗位治理）

### config_score_coefficient（3字段，★v2.3改名）
score_min(**人工定义**,C1) / score_max(**人工定义**,C1) / coefficient(**人工定义**,C1)
（配置表；频率：低频更新；触发条件：评分档位规则变更时）

### config_position_alias（9字段，★v2.3改名）
alias_id / source_position_name(岗位治理) / standard_position_name(岗位治理) / alias_type(岗位治理) / current_headcount(岗位治理) / belongs_to_family(岗位治理) / belongs_to_grade(岗位治理) / confidence(岗位治理) / note(岗位治理)

### AGG_labor_cost_monthly（25字段）
agg_key / date_key / legal_entity_key / business_unit_key / organization_key / segment_code / headcount_active(来源:fact_emp_monthly) / headcount_new_hire / headcount_terminated / basic_salary_total(来源:fact_salary_monthly) / allowance_total / performance_total / overtime_total / gross_salary_total / social_insurance_company_total(来源:fact_social_insurance) / housing_fund_company_total / mpf_company_total / social_total_company(ETL计算) / labor_cost_total(ETL计算) / labor_cost_per_capita(ETL计算) / includes_outsource(**用户决策**,C1) / includes_consultant(**用户决策**,C1) / etl_load_date / source_versions(ETL记录) / aggregation_method(ETL记录)

---

## 四、C1-C5规则信号预标注（执行B标签时的锚点）

### C1 · 数据来源=人工定义/人工录入

| 表名 | C1命中字段 |
|---|---|
| dim_salary_component | component_code / component_name_cn / component_name_en / category / is_taxable / in_social_base（全部6字段） |
| dim_insurance_type | insurance_code / insurance_name_cn / payer / sz_rate / remarks（全部5字段） |
| config_score_coefficient | score_min / score_max / coefficient（全部3字段） |
| dim_salary_band | effective_date |
| AGG_labor_cost_monthly | includes_outsource / includes_consultant |

### C2 · 计算口径包含手工/人工判断

| 表名 | C2候选字段（需Kimi逐一确认计算口径是否含人工判断） |
|---|---|
| fact_bonus_calculation | hire_adjustment / probation_adjustment / adjustment_hkd / emp_coefficient_1 / emp_coefficient_2 |
| dim_bonus_pool | dept_coefficient |
| AGG_labor_cost_monthly | labor_cost_total（需确认是否含手工调整项） |
| config_position_alias | confidence（置信度评分规则） |

### C3 · 更新频率=按需/规则更变时

| 表名 | C3候选字段 |
|---|---|
| config_score_coefficient | 全部3字段（评分档位规则变更时更新） |
| dim_salary_component | 全部6字段（薪资项定义变更时） |
| dim_insurance_type | 全部5字段（保险类型变更时） |
| bridge_position_grade | 全部7字段（岗位职级规则调整时） |
| dim_salary_band | 全部6字段（薪酬调研结果更新时） |

### C4 · Data Owner = 归属部门（挂名风险）

- 全量386字段中：HRD=362字段，BizD=24字段
- 归属部门字段：HR业务方(≈维度表) / IT数据团队(≈事实表) / 数据治理(字典表)
- **C4判断重点**：Owner=HRD但实际由IT数据团队维护的事实表字段（如ETL计算字段挂HRD Owner）

### C5 · 枚举值/FK约束字段

来源：Sheet3快速编码（192条），高密度枚举字段：
- position_family（14条）/ position_grade（13条）/ event_type（8条）/ entity_type（6条）/ check_result（6条）/ employment_type（5条）/ date_quality（5条）/ career_track（5条）/ business_unit_type（4条）/ org_module（4条）/ proficiency_level（4条）

---

## 五、四标签执行规则

### 标签A · 表类型规则洞察

按HR域涉及的表类型分类，天然风险方向：

| 表类型 | 天然风险方向 | HR域典型信号字段 |
|---|---|---|
| 事实表（9张） | ETL计算口径/源文件依赖/DQ标记触发条件 | data_quality_flag / source_file / etl_batch_id |
| 维度表（16张） | SCD处理/effective_from-to重叠/is_current判断 | effective_from / effective_to / is_current |
| 质量监控表（1张） | check_result枚举定义/触发频率/差异处理 | check_result / check_type |
| 配置表（2张） | 变更审批/触发条件/人工维护SPOF | 全部字段（C1全命中） |
| 字典表（1张） | 枚举值增删流程/版本控制/各域消费一致性 | code / display_name |
| 桥接表（1张） | N:1关系处理/默认值定义/失活机制 | is_default / is_active |
| 聚合表（1张） | 聚合口径文档/底表版本追踪/用户决策字段 | aggregation_method / includes_outsource / includes_consultant |

**特殊注意（HR域独有）**：
- `fact_attendance_monthly`（53字段）：跨城市考勤规则（HK vs 深圳）差异、香港/深圳年假双余额字段（hk_annual_balance / sz_annual_balance_cur / sz_annual_balance_prev）的计算口径
- `fact_salary_monthly`：contract_region来源是dim_employee而非HR-004，需标注跨表依赖风险
- `AGG_labor_cost_monthly`：includes_outsource / includes_consultant为"用户决策"字段，每次聚合可能不同，是聚合口径最大不确定源
- `dim_employee`：含PII字段（id_card_masked / phone / email / emergency_contact / emergency_phone / home_address_city），A标签需标注PII风险

### 标签B · 分工断点与字段唯一责任

三步执行：
1. 表级责任模式判断（参照：数据分工列 vs Data Owner列是否一致）
2. C1-C5逐字段扫描（参照第四节预标注）
3. 特别关注：
   - 事实表：Data Owner=HRD但由IT数据团队维护→C4集中风险
   - 配置表（2张）：全字段C1命中，变更审批链是否存在
   - 待实施表（12张）：Owner已定义但维护流程未建立

**HR域已知责任分工**：
- HRD（HR Director）：维度表/大部分事实表的业务Owner
- BizD（Business Director）：dim_segmentation / dim_ka的Owner
- IT数据团队：事实表的数据分工方（ETL执行）
- 数据治理：dim_lookup_code的数据分工方
- HR业务方：维度表的数据分工方

### 标签C · 程序验证路径与断点

参照全景图数据链，HR域分4段：

```
段1（员工基础链）：
  HR-001/002 → dim_employee / dim_organization / dim_position → fact_emp_monthly
  → consistency_check（与fact_employee_events交叉校验）

段2（薪资链）：
  HR-004 → fact_salary_monthly → fact_salary_tax_detail
  HR-007 → fact_social_insurance_monthly
  dim_salary_component / dim_insurance_type（参数输入）

段3（考勤链）：
  HR-003 → fact_attendance_monthly

段4（绩效奖金链）：
  HR-005 → fact_performance_eval → config_score_coefficient → bonus_coefficient
  HR-006 → dim_bonus_pool → fact_bonus_calculation
  dim_position_grade + bridge_position_grade + dim_salary_band（新建层）

段5（聚合层）：
  fact_emp_monthly + fact_salary_monthly + fact_social_insurance_monthly
  → AGG_labor_cost_monthly（财务源头）
```

每张表识别：所在链段 + 上游来源 + 下游去向 + 验证盲区类型

### 标签D · 商业职能与授权

HR域授权参照：

| 功能域 | 代表表 | 建议授权级别 |
|---|---|---|
| 员工基础信息 | dim_employee / fact_emp_monthly | 🟡高（含PII） |
| 薪资核算 | fact_salary_monthly / fact_salary_tax_detail | 🔴最高（财务结算） |
| 社保公积金 | fact_social_insurance_monthly | 🔴最高（合规+财务） |
| 绩效评估 | fact_performance_eval | 🟡高（晋升/薪资决策） |
| 绩效奖金 | fact_bonus_calculation / dim_bonus_pool | 🔴最高（财务结算） |
| 考勤 | fact_attendance_monthly | 🟡高（薪资依据） |
| 人工成本聚合 | AGG_labor_cost_monthly | 🔴最高（财务源头） |
| 岗位/职级配置 | bridge_position_grade / config_score_coefficient | 🟡高（薪酬依据） |
| 字典/编码 | dim_lookup_code | 🟢中（全域消费） |

---

## 六、规则空白地图输出格式

**取消P4调研交叉填充列**（Jasper确认：此为数据提供方关注信息，分析任务忽略）

输出格式：

| 优先级 | 表名 | 规则空白描述 | 空白类型 | 对应五问 | 对应D维度 | 访谈岗位 | 访谈问题草稿 |
|---|---|---|---|---|---|---|---|

**空白类型枚举**：语义盲区 / 触发缺失 / 计算黑盒 / 交接断点 / 授权断层 / SPOF集中 / 治理真空 / PII风险

**优先级判断（P0/P1/P2）**：
- P0 = B=🔴（三权合一/SPOF）+ D=🔴（财务结算/合规）+ ❌规则缺口，同时满足三项
- P1 = 满足以上三项中的两项
- P2 = 满足以上三项中的一项

---

## 七、输出物规格

### 输出物A：30张单表标签卡

每张表格式：
```
【表中文名】/ 表英文名
表类型 | 字段数 | 状态 | 数据链段

A · 表类型规则洞察
  类型风险：[HR域专属描述]
  本表信号字段：[字段名]（[具体风险]）

B · 分工断点与字段唯一责任
  分工结构：Owner=[X] / 数据分工=[X]
  责任模式：[类型]（🔴/🟡/🟢）
  C1命中：[字段名列表]
  C2命中：[字段名列表]
  C3命中：[字段名列表]
  C4命中：[字段名列表]（Owner与实际维护方不一致）
  C5命中：[字段名列表]

C · 程序验证路径与断点
  在链位置：[段1/2/3/4/5]
  上游：[来源]
  下游：[去向]
  验证盲区：[类型] - [具体描述]

D · 商业职能与授权
  职能：[描述] → 授权级别：[最高/高/中/低]
  PII风险：[有/无]（有则列明字段）
  合规风险：[高/中/低] + 1句说明

规则空白贡献（本表 → 地图）：
⚠️ [描述] → 五问:Q? → D维度:D? → 优先级:P?
```

### 输出物B：字段级规则信号清单（C1-C5命中汇总表格）

| 表名 | 字段名 | 字段中文 | 命中规则信号 | Data Owner | 对应D维度 | 备注 |

### 输出物C：规则空白地图

| 优先级 | 表名 | 规则空白描述 | 空白类型 | 对应五问 | 对应D维度 | 访谈岗位 | 访谈问题草稿 |

---

## 八、注意事项

1. **待实施表处理**：12张待实施表（Phase 1-4）执行四标签，字段信息不完整处标⛔，不得跳过。B标签重点标注"维护流程待建立"风险。

2. **PII字段特别处理**：dim_employee中的phone / email / id_card_masked / emergency_contact / emergency_phone / home_address_city，A标签须标注PII风险，D标签授权级别不低于🟡高。

3. **BizD Owner表**（dim_segmentation / dim_ka）：B标签责任模式重点检查HR数据域与BizD的交接边界是否清晰。

4. **fact_attendance_monthly（53字段）**：字段最多的表，B标签C5扫描需覆盖全部53字段，不得抽查。

5. **v2.3结构修要点**（需在对应表的A标签中标注）：
   - dim_position删除了grade_code和salary_band字段 → 依赖方需更新
   - bridge_position_grade为新建桥接表，1:N关系处理规则需重点分析
   - dim_salary_band为新建，外部顾问来源字段的更新机制需标注

6. **唯一性检查**：规则空白地图提交前执行两两比对，回传声明「已执行两两比对唯一性检查，0组重复」。

---

## 九、回传要求

**文件名**：`HR001_第一层产出_四标签+规则空白地图_V1.md`

**必须包含章节**：
1. 执行声明（情景1 / 路径A / 完成日期 / 表数 / 字段数）
2. 30张单表标签卡（按数据链段顺序排列：配置/字典层→维度层→事实层→聚合层）
3. 字段级规则信号清单（C1-C5跨表汇总）
4. 规则空白地图（P0/P1/P2，无调研状态列）
5. 自检声明：「已执行两两比对唯一性检查，共X条规则空白，0组重复」

---

## 十、附件清单

| # | 文件名 | 用途 |
|---|---|---|
| 1 | 数据规则提取方法论_三层递进提取法_v2.1.md | 方法论主文件（必读） |
| 2 | HR星型模型_数据字典_v2_3.xlsx | 主输入（Sheet1概览+Sheet2字段+Sheet3编码+Sheet4 KPI） |
| 3 | HR数据模型_全景图_v1_0.png | 数据链关系参照（C标签） |

---

*任务包生成：Claude（规划层）| 授权：Jasper | 执行：Kimi*
*生成时间：2026-05-19*

