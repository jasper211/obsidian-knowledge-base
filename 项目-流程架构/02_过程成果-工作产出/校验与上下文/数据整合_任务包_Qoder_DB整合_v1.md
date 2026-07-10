---
type: 项目笔记
source: 02_过程成果-工作产出/校验与上下文
synced: 2026-06-15
tags: [项目]
---

# 数据库整合任务包 · Qoder执行
> 发起人：Jasper · 日期：2026-04-29 · 优先级：P0
> 目标：将分散在多个文件夹中的数据沉淀整合为统一数据底座 ea_knowledge_base.db

---

## 任务背景

当前项目在多个文件夹内已沉淀以下已完成的映射数据：
- ✅ L3编码标准化（82条）
- ✅ L1-L3映射（82条）
- ✅ VS-L3映射（83条：67条归VS，16条非VS级）
- ✅ 价值流全量表V3（354行，VS1-5全覆盖）
- ✅ L3-L4映射（396行）
- ✅ L4→核心交付物+Agent映射（400行，M2_Tier全覆盖）
- ✅ KPI-L3标准映射（235行，32企业KPI×82 L3）
- ✅ 岗位KPI→企业KPI→L3穿透（302行，9族覆盖）

**当前问题**：上述数据分散在不同CSV/Excel文件或子目录，尚未统一写入 `ea_knowledge_base.db`。

---

## 任务目标

**一句话**：扫描项目目录，识别所有相关数据文件，整合写入统一SQLite数据库，确保5张核心表数据完整、外键一致。

---

## 数据库Schema（5张核心表）

### 表1：dim_l3（L3流程库，82条）
```sql
CREATE TABLE IF NOT EXISTS dim_l3 (
    l3_code        TEXT PRIMARY KEY,  -- 格式：L3-XXX（3位大写字母）
    l3_name        TEXT NOT NULL,
    l1_code        TEXT NOT NULL,     -- 归属L1飞轮节点（L1-01~05）
    l1_name        TEXT NOT NULL,
    vs_code        TEXT,              -- 归属价值流（VS1~5），横切能力层为NULL
    vs_stage       TEXT,              -- 归属VS阶段
    is_vs_level    INTEGER DEFAULT 1, -- 1=VS级，0=非VS级（横切能力层）
    source_doc     TEXT,              -- 溯源文档
    confirmation_status TEXT DEFAULT 'draft',
    created_at     TEXT DEFAULT (datetime('now'))
);
```

### 表2：dim_value_stream（价值流表，354行）
```sql
CREATE TABLE IF NOT EXISTS dim_value_stream (
    vs_code        TEXT NOT NULL,     -- VS1~VS5
    vs_name        TEXT NOT NULL,
    stage_code     TEXT NOT NULL,     -- 阶段编码，如IAO/IAC
    stage_name     TEXT NOT NULL,
    activity_code  TEXT,              -- L3编码（外键→dim_l3）
    activity_name  TEXT,
    activity_desc  TEXT,
    sort_order     INTEGER,
    PRIMARY KEY (vs_code, stage_code, activity_code)
);
```

### 表3：dim_agent_capability（L4活动+Agent映射，400行）
```sql
CREATE TABLE IF NOT EXISTS dim_agent_capability (
    l4_code        TEXT PRIMARY KEY,  -- 格式：L4-XXX-NN
    l4_name        TEXT NOT NULL,
    l3_code        TEXT NOT NULL,     -- 外键→dim_l3
    deliverable    TEXT,              -- 核心交付物名称
    agent_type     TEXT NOT NULL,     -- Auto / Assist / Human
    m2_tier        TEXT,              -- Tier1/Tier2/Tier3（业务评审结果）
    infer_tier     TEXT,              -- 推导Tier（参考用）
    source_doc     TEXT,
    confirmation_status TEXT DEFAULT 'draft'
);
```

### 表4：dim_kpi（KPI-L3映射，235行）
```sql
CREATE TABLE IF NOT EXISTS dim_kpi (
    corp_kpi_id    TEXT PRIMARY KEY,  -- 企业KPI编码，如KPI-01
    corp_kpi_name  TEXT NOT NULL,
    l3_code        TEXT NOT NULL,     -- 外键→dim_l3
    alignment_score INTEGER,          -- 对齐度 1-5
    kpi_type       TEXT,              -- 结果型/过程型
    measure_freq   TEXT,              -- 月度/季度/年度
    confirmation_status TEXT DEFAULT 'draft'
);
```

### 表5：bridge_job_kpi（岗位KPI穿透，302行）
```sql
CREATE TABLE IF NOT EXISTS bridge_job_kpi (
    job_family_code TEXT NOT NULL,    -- A~G族
    job_kpi_name   TEXT NOT NULL,
    weight_pct     REAL,              -- 权重百分比
    corp_kpi_id    TEXT,              -- 外键→dim_kpi
    l3_code        TEXT,              -- 穿透至L3
    confirmation_status TEXT DEFAULT 'draft',
    PRIMARY KEY (job_family_code, job_kpi_name)
);
```

---

## 执行步骤

### Step 1：扫描数据文件
```
扫描以下目录，识别所有 .csv / .xlsx / .json 文件：
- 项目根目录
- 所有子目录（递归扫描）

输出一份清单，格式：
文件路径 | 推断内容（l3/vs/l4/kpi/job_kpi）| 行数 | 字段列表
```

### Step 2：Schema映射确认
对扫描到的每个文件，输出字段映射表：
```
源字段名 → 目标表.字段名
（如有差异请标注，不要自动重命名）
```

### Step 3：写入数据库
按以下顺序写入（保证外键依赖顺序）：
1. dim_l3（无外键依赖，先写）
2. dim_value_stream（依赖dim_l3.l3_code）
3. dim_agent_capability（依赖dim_l3.l3_code）
4. dim_kpi（依赖dim_l3.l3_code）
5. bridge_job_kpi（依赖dim_kpi.corp_kpi_id + dim_l3.l3_code）

**写入规则**：
- 使用 `INSERT OR REPLACE INTO`（允许幂等重跑）
- confirmation_status 保持源数据中的值，若源数据无此字段则默认 `'draft'`
- l3_code 格式强制校验：必须匹配 `^L3-[A-Z]{3}$`，不合规的跳过并记录到error_log

### Step 4：验证
写入完成后执行以下查询，输出结果：

```sql
-- 各表行数
SELECT 'dim_l3' as tbl, COUNT(*) as rows FROM dim_l3
UNION ALL SELECT 'dim_value_stream', COUNT(*) FROM dim_value_stream
UNION ALL SELECT 'dim_agent_capability', COUNT(*) FROM dim_agent_capability
UNION ALL SELECT 'dim_kpi', COUNT(*) FROM dim_kpi
UNION ALL SELECT 'bridge_job_kpi', COUNT(*) FROM bridge_job_kpi;

-- 外键孤儿检查
SELECT COUNT(*) as orphan_l4 FROM dim_agent_capability
WHERE l3_code NOT IN (SELECT l3_code FROM dim_l3);

SELECT COUNT(*) as orphan_kpi FROM dim_kpi
WHERE l3_code NOT IN (SELECT l3_code FROM dim_l3);

-- confirmation_status分布
SELECT confirmation_status, COUNT(*) as cnt
FROM dim_l3 GROUP BY confirmation_status;

-- A族覆盖检查
SELECT l3_code, l3_name FROM dim_l3
WHERE l3_code IN ('L3-MSI','L3-MSE','L3-IAO','L3-IAC','L3-IRI','L3-IBE','L3-IRR');
```

### Step 5：输出报告
完成后输出整合报告，包含：
- 各表实际写入行数 vs 预期行数
- 跳过/错误记录列表（error_log）
- 外键孤儿数量
- 若孤儿数 > 0，列出具体l4_code和对应的l3_code

---

## 验收标准

| 检查项 | 预期值 | 通过条件 |
|--------|--------|---------|
| dim_l3行数 | 82 | ≥80 |
| dim_value_stream行数 | 354 | ≥320 |
| dim_agent_capability行数 | 400 | ≥380 |
| dim_kpi行数 | 235 | ≥200 |
| bridge_job_kpi行数 | 302 | ≥280 |
| 外键孤儿 | 0 | =0 |
| l3_code格式合规率 | 100% | ≥98% |

**所有检查项通过后，在数据库根目录生成 `integration_report_YYYYMMDD.txt`**

---

## 注意事项

1. **M2_Tier优先于推导Tier**：dim_agent_capability中若两列都有，保留m2_tier，infer_tier仅作参考
2. **非VS级16条L3**：is_vs_level=0，vs_code=NULL，不强行归入任何VS
3. **L1权威名称**：来自方法论纠偏文档，5个飞轮节点名称不可修改：
   - L1-01 保险业务赋能
   - L1-02 代理人事业发展
   - L1-03 机构合作拓展
   - L1-04 数据与技术中台
   - L1-05 横切能力层
4. **不要修改已有confirmation_status=mark_locked的记录**

---

## 完成后通知Jasper

输出格式：
```
✅ 数据库整合完成
- 数据库路径：[path]/ea_knowledge_base.db
- 整合时间：YYYY-MM-DD HH:MM
- 各表行数：[list]
- 外键孤儿：0条
- 错误记录：[N]条（详见error_log）
- 下一步建议：[Jasper自行填写]
```
