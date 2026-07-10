---
type: 项目笔记
source: 02_过程成果-工作产出/_归档
synced: 2026-06-15
tags: [项目]
---

# T1 修复任务包 v2 · Qoder执行
> 发起：Jasper · 日期：2026-04-30  
> 版本说明：v2相较v1移除了KPI相关所有任务，数据底座范围收窄为4张核心表  
> **修复完成后重新提交T1报告，由Claude验收后T2方可启动**

---

## 数据底座范围（最终定义）

**纳入：**
```
dim_l3              → L3流程库（82条，核心锚点）
dim_value_stream    → 价值流全量表（VS→阶段→L3）
dim_l4_activity     → L4活动表
dim_agent_capability→ L4→交付物+Agent映射
```

**移出（不建、不写、不校验）：**
```
dim_kpi             → 移出，不纳入底座
bridge_job_kpi      → 移出
bridge_job_l3       → T3阶段再建
dim_job_family      → T3阶段再建
```

---

## 需执行的3个修复项

### FIX-01：dim_value_stream 替换来源文件

**问题**：当前来源文件 `过程文档/output_旧数据/价值流_价值阶段_价值活动_全量表_V3.csv` 属于过程产物，L3编码不完整，不是最终82条标准L3对应的版本。

**修复步骤**：

Step 1 — 在项目目录中寻找正确文件

搜索条件（按优先级）：
- 位于 `核心文档/` 目录下
- 文件名含"价值流"+"全量"或"V3"或"最终"
- 打开确认：activity_code列的L3编码与dim_l3中82条l3_code完全一致

找不到时**停止，向Jasper报告**候选文件清单，由Jasper指定。

Step 2 — 校验候选文件

```python
import pandas as pd, sqlite3

df_vs = pd.read_csv("候选文件路径")
conn  = sqlite3.connect("ea_knowledge_base_t1.db")
valid_l3 = pd.read_sql("SELECT l3_code FROM dim_l3", conn)['l3_code'].tolist()

vs_l3   = df_vs[df_vs['activity_code'].notna()]['activity_code'].unique().tolist()
missing = [c for c in vs_l3 if c not in valid_l3]
print(f"不在标准L3列表中的编码（目标为空）：{missing}")
```

`missing` 为空才可继续，否则继续找文件。

Step 3 — 清空并重写

```sql
DELETE FROM dim_value_stream;
```

用正确文件重新写入，`source_doc` 填写 `核心文档/[实际文件名]`。

Step 4 — 验证

```sql
SELECT COUNT(*) FROM dim_value_stream;
-- 目标：≥320

SELECT COUNT(*) FROM dim_value_stream
WHERE activity_code IS NOT NULL
  AND activity_code NOT IN (SELECT l3_code FROM dim_l3);
-- 目标：= 0（无外键孤儿）

SELECT DISTINCT source_doc FROM dim_value_stream;
-- 目标：不含"旧数据"或"output_旧数据"字样
```

---

### FIX-02：删除 dim_kpi 表

**原因**：KPI数据不再纳入数据底座，对应的输出界面模块也已移除。

```sql
DROP TABLE IF EXISTS dim_kpi;
DROP TABLE IF EXISTS bridge_job_kpi;
```

执行后确认：

```sql
SELECT name FROM sqlite_master WHERE type='table';
-- 预期只剩4张表：dim_l3 / dim_value_stream / dim_l4_activity / dim_agent_capability
```

---

### FIX-03：agent_type 字段改为4值

**原因**：当前将 m2_tier 的4值（Auto/Aug/Hybrid/Human）合并为3值（Auto/Assist/Human），丢失了 Aug 与 Hybrid 的区分度，影响 T3 岗位推导。

**4值定义**（写入数据库文档备注）：

| 值 | 含义 |
|----|------|
| `Auto` | Agent全自动执行，无需人工介入 |
| `Aug` | Agent主导，人工做最终审批/确认（Augmented） |
| `Hybrid` | 人工主导，Agent提供辅助支持 |
| `Human` | 纯人工执行，不引入Agent |

**修复步骤**：

```sql
-- 备份
CREATE TABLE dim_agent_capability_backup
    AS SELECT * FROM dim_agent_capability;

-- 从 m2_tier 还原 agent_type（m2_tier 是业务评审原始值，优先级最高）
UPDATE dim_agent_capability
SET agent_type = m2_tier
WHERE m2_tier IN ('Auto','Aug','Hybrid','Human');

-- 验证分布（应与 T1 报告中 m2_tier 分布一致）
SELECT agent_type, COUNT(*) FROM dim_agent_capability
GROUP BY agent_type;
-- 预期：Auto(77)  Aug(~108)  Hybrid(~176)  Human(39)

-- 枚举合规检查
SELECT agent_type FROM dim_agent_capability
WHERE agent_type NOT IN ('Auto','Aug','Hybrid','Human');
-- 目标：0条
```

---

## 修复后重新提交的报告格式

文件名：`T1_integration_report_20260430_v2.txt`

在原报告基础上，替换以下内容：

```
========================================
【数据底座范围（v2）】
========================================
纳入：dim_l3 / dim_value_stream / dim_l4_activity / dim_agent_capability
移出：dim_kpi（已DROP）/ bridge_job_kpi（未建）

========================================
【各表行数 vs 预期（v2）】
========================================
dim_l3:              实际___ / 预期82   [PASS/FAIL]
dim_value_stream:    实际___ / 预期≥320 [PASS/FAIL]
dim_l4_activity:     实际___ / 预期396  [PASS/FAIL]
dim_agent_capability:实际___ / 预期400  [PASS/FAIL]
dim_kpi:             已DROP（不纳入底座）

========================================
【FIX-01 dim_value_stream修复记录】
========================================
旧来源文件：过程文档/output_旧数据/价值流_价值阶段_价值活动_全量表_V3.csv
新来源文件：[实际路径]
修复后行数：___
外键孤儿：  ___（目标0）

========================================
【FIX-02 dim_kpi移除记录】
========================================
DROP TABLE dim_kpi：已执行
DROP TABLE bridge_job_kpi：已执行
当前数据库表清单：[列出4张表]

========================================
【FIX-03 agent_type修复记录】
========================================
修复前：Auto(77) Assist(284) Human(39)
修复后：Auto(___) Aug(___) Hybrid(___) Human(___)
修复方式：从m2_tier字段还原
枚举合规：___条不合规（目标0）

========================================
【重新验收结果】
========================================
[重新执行所有校验SQL，输出完整结果]
```

---

## T1-v2 验收标准（Claude重新校验用）

| 检查项 | 预期 | 通过条件 |
|--------|------|---------|
| 数据库表数量 | 4张 | =4（无dim_kpi） |
| dim_l3行数 | 82 | ≥80 |
| dim_value_stream行数 | ≥320 | ≥320，来源非旧数据目录 |
| dim_l4_activity行数 | 396 | ≥370 |
| dim_agent_capability行数 | 400 | ≥380 |
| 所有外键孤儿 | 0 | =0 |
| source_doc覆盖率 | 100% | ≥95% |
| source_doc不含"旧数据"字样 | 是 | 必须 |
| l3_code格式合规 | 100% | ≥98% |
| agent_type为4值枚举 | 100% | =100% |
| 岗位JD相关数据混入 | 0条 | =0 |

**全部通过 → T1 PASS v2，T2可启动**
