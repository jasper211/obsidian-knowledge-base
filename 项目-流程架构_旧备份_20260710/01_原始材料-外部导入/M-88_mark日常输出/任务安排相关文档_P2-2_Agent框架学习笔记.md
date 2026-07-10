---
type: 项目笔记
source: 01_原始材料-外部导入/M-88_mark日常输出
synced: 2026-06-15
tags: [项目]
---

# P2-2 Agent框架学习笔记

> 赵琦 | 2026-04-17 | 实际试跑验证

---

## 一、Agent框架全貌

### 架构设计
```
agents/
├── base.py               # BaseAgent + PipelineAgent + AgentResult
├── validators.py          # 6个通用校验函数
├── commission_agents.py   # 佣金链 4 Agent + CommissionPipeline
├── performance_agents.py  # 业绩链 2 Agent + PerformancePipeline
├── product_agents.py      # 产品域 3 Agent
└── registry.py            # 注册表，统一查看+运行
```

### 每个Agent的执行流程
```
Agent.run()
  ├── [L1] execute()      → 执行业务逻辑，产出AgentResult
  ├── [L3] validate()     → 校验结果（行数/空值/范围/交叉引用）
  ├── [L4] 失败自动告警   → 企业微信Webhook推送
  └── [L5] 产出日志       → 输出summary (OK/FAIL + rows + duration + warnings)
```

### 当前9个Agent一览

| # | Agent名称 | 归属族 | L4覆盖 | 功能 |
|---|----------|--------|--------|------|
| 1 | FACT1_commission_rate | B | L3-IPI L4-01/02 | 33个保司佣金源表 → 佣金事实表 |
| 2 | Agg1_source_commission_wide | B | L3-COM L4-03 | 佣金事实表 → 源头佣金宽表 |
| 3 | Agg2_market_commission_tier_rate | G | L3-COM L4-03, L3-IBE SAL-03 | 宽表 → 全档位佣金表（规则引擎核心）|
| 4 | Agg3_market_commission | B | L3-COM L4-03 | 全档位表 → 市场佣金表（拆表分发）|
| 5 | FACT2_policy | D | — | 保单数据清洗 → 保单事实表 |
| 6 | Agg4_sales_base | D | — | 保单事实表 → 业绩底表 |
| 7 | IPI_L4-01_product_metadata_validator | B | L3-IPI L4-01 | 产品元数据7项检查 |
| 8 | IPI_L4-06_product_version_comparator | B | L3-IPI L4-06 | 产品版本比对 |
| 9 | SLCM_L4-01_product_health_monitor | C | L3-SLCM L4-01 | 产品运营健康度 |

### 2条Pipeline

| Pipeline | 步骤 | 说明 |
|----------|------|------|
| commission_full_pipeline | FACT1→Agg1→Agg2→Agg3 | 佣金制表全链路，串行执行，任一步失败则停止+告警 |
| performance_full_pipeline | FACT2→Agg4 | 业绩全链路 |

---

## 二、实际试跑结果

### 试跑1：产品校验Agent (PASS)
```bash
python -m agents.product_agents --agent validate
```
- 结果：**PASS**，375行（DIM_PRODUCT_ID 283行 + DIM_PRODUCT_SKU 92行）
- 7项检查全部通过：必填字段/交叉引用/唯一性/枚举值
- 4个advisory warning：Business_Line/Is_Premium_Financing/Clawback_Period_Months/Currency_Link_Rule空值
- 耗时：<1秒

### 试跑2：FACT1佣金事实表Agent (PASS)
```bash
python -m agents.commission_agents --step 1
```
- 结果：**PASS**，12,505行
- 输入：33个保司佣金源文件（AIA/AXA/BLUE/BOC等16家保司）
- 输出：`etl/fact/output/Fact_Commission_Rate_*.xlsx`
- 校验通过：行数>1000、关键字段无空值、费率范围-0.1~2.0
- 耗时：26.2秒
- 企业微信告警已自动发送

### 试跑3：Agg1源头佣金宽表Agent (FAIL — 预期)
```bash
python -m agents.commission_agents --step 2
```
- 结果：**FAIL** — `etl/agg/source_data/` 目录不存在
- 原因：Agg1依赖FACT1的输出，需要将FACT1的output链接到Agg1的source_data
- 这在Teresa的Windows机器上已配好，Mac上需要手动链接
- 企业微信告警已自动发送（crash级别）

---

## 三、Mac环境命令速查

数据平台路径：
```
~/Documents/Secondbrain/A项目/EA_B_data_platform/mga-data-platform/
```

```bash
# 进入项目目录
cd ~/Documents/Secondbrain/A项目/EA_B_data_platform/mga-data-platform

# 查看所有Agent状态
python3 -m agents.registry

# 产品校验（最安全的练手命令）
python3 -m agents.product_agents --agent validate
python3 -m agents.product_agents --agent version
python3 -m agents.product_agents --agent health

# 佣金链（单步）
python3 -m agents.commission_agents --step 1    # FACT1: 源表→事实表
python3 -m agents.commission_agents --step 2    # Agg1: 事实表→宽表
python3 -m agents.commission_agents --step 3    # Agg2: 宽表→全档位表
python3 -m agents.commission_agents --step 4    # Agg3: 全档位→市场佣金表

# 佣金链（全链路）
python3 -m agents.commission_agents

# 业绩链
python3 -m agents.performance_agents
```

---

## 四、Agent设计要点（写新Agent时参考）

### 继承BaseAgent的要求
```python
class MyAgent(BaseAgent):
    name = "my_agent_name"        # 唯一名称
    owner = "B"                    # 7族代码(A/B/C/D/E/F/G)
    l4_codes = ["L3-XXX_L4-YY"]  # 对应L4编号
    description = "一句话说明"

    def execute(self) -> AgentResult:
        # 业务逻辑，返回AgentResult
        ...

    def validate(self, result) -> AgentResult:
        # 用validators.py的6个函数校验
        # check_row_count_min / check_no_nulls / check_value_range 等
        ...
```

### 6个通用校验函数（validators.py）
1. `check_row_count_min(df, min_count, table_name)` — 最小行数
2. `check_no_nulls(df, columns, table_name)` — 关键字段无空值
3. `check_value_range(df, column, min_val, max_val, table_name)` — 数值范围
4. `check_unique(df, columns, table_name)` — 唯一性
5. `check_referential_integrity(df, ref_df, key, table_name)` — 外键引用完整性
6. `check_enumeration(df, column, valid_values, table_name)` — 枚举值

### 告警机制
- ValidationError → warning级别告警（数据/业务规则不通过）
- Exception → critical级别告警（程序崩溃）
- 成功完成 → info级别告警
- 告警通道：企业微信群机器人Webhook

---

## 五、关键认知

1. **Agent ≠ AI大模型** — 这里的Agent是自动化数据管线（Python脚本），不是ChatGPT/Claude
2. **管线设计是Kimball维度建模** — FACT(事实表) + DIM(维度表) + AGG(聚合表)，保险行业标准
3. **渐进式聚合** — FACT→Agg1→Agg2→Agg3，每层只做一件事，可独立重跑
4. **配置驱动** — 不硬编码业务规则，从Excel配置表动态读取
5. **M4.1目标34个Agent** — 当前9个(26%)，按80条Auto L4逐步覆盖
6. **你的SOP工作属于L3-EFB** — 未来也会有Agent化的SOP生成管线
