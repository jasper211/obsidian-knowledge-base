---
type: 项目笔记
source: 04_Skill库/草稿
synced: 2026-06-15
tags: [项目]
---

# A1-S02 — 编号差异识别与对照样本输出

**Skill ID**：A1-S02
**版本**：V1.0
**归属 Agent**：A1（EA数据库维护）
**创建日期**：2026-04-28
**状态**：可用

---

## 一、这个 Skill 做什么

对比两个数据源中指定编码字段的差异，输出：
- 并排对照样本（每行标注是否可匹配）
- 可匹配率
- 仅在来源1/来源2的编码列表
- 两侧编码格式规律描述

**核心特性**：
- 支持 DataFrame-to-DataFrame 直接对比
- 支持从 SQLite 数据库执行 SQL 查询后对比
- 自动识别编码格式规律（纯数字 / 字母前缀 / 复合键 / activity_id风格）
- 输出 CSV 样本 + Markdown 差异报告

---

## 二、函数签名

### `identify_code_difference(...) -> dict`

```python
from skill_A1_S02 import identify_code_difference

result = identify_code_difference(
    df_source1    = df_lib,       # 第一个 DataFrame
    df_source2    = df_agent,     # 第二个 DataFrame
    code_col      = "l3_code",   # 要对比的字段名
    sample_n      = 30,           # 并排样本行数
    source1_label = "L3流程库",   # 来源1标签
    source2_label = "Agent评分表", # 来源2标签
)
```

### 返回值

```python
{
    "sample_df":       pd.DataFrame,  # 并排对照样本（含是否可匹配列）
    "match_rate":      float,         # 来源1视角的可匹配率
    "only_in_source1": list[str],     # 只在来源1的编码
    "only_in_source2": list[str],     # 只在来源2的编码
    "format_pattern":  str,           # 格式规律描述
    "stats":           dict,          # 详细统计
}
```

### `compare_from_db(db_path, query1, query2, code_col, ...) -> dict`

```python
from skill_A1_S02 import compare_from_db

result = compare_from_db(
    db_path = "ea_knowledge_base.db",
    query1  = "SELECT DISTINCT l3_code FROM fact_activity WHERE l5_activity IS NOT NULL",
    query2  = "SELECT DISTINCT l3_code FROM fact_activity WHERE agent_score_total IS NOT NULL",
    code_col = "l3_code",
    source1_label = "L3流程库",
    source2_label = "Agent评分",
)
```

### `save_results(result, out_dir, csv_name, report_name) -> dict`

```python
from skill_A1_S02 import save_results

paths = save_results(result, "/path/output/validation")
# → {"csv_path": "...编号对照样本.csv", "report_path": "...编号差异报告.md"}
```

---

## 三、典型调用示例

### 复现 task4.py 的 task41_code_comparison()

```python
from skill_A1_S02 import compare_from_db, save_results

DB = "/path/ea_knowledge_base.db"
OUT = "/path/output/validation"

result = compare_from_db(
    db_path      = DB,
    query1       = """
        SELECT DISTINCT l3_code, l4_code
        FROM fact_activity
        WHERE l5_activity IS NOT NULL
        ORDER BY l3_code, l4_code
        LIMIT 30
    """,
    query2       = """
        SELECT DISTINCT l3_code, l4_code
        FROM fact_activity
        WHERE agent_score_total IS NOT NULL
        ORDER BY l3_code, l4_code
        LIMIT 30
    """,
    code_col     = "l3_code",
    source1_label = "L3流程库",
    source2_label = "Agent评分表",
)

print(f"可匹配率：{result['match_rate']:.1%}")
print(f"仅在L3流程库：{result['only_in_source1'][:5]}")
save_results(result, OUT, csv_name="编号对照样本.csv")
```

### 对比两个 CSV 文件的 L3 编码

```python
import pandas as pd
from skill_A1_S02 import identify_code_difference, save_results

df1 = pd.read_csv("/path/L3编码注册表.csv", encoding="utf-8-sig")
df2 = pd.read_csv("/path/L3编码修改映射表.csv", encoding="utf-8-sig")

result = identify_code_difference(
    df1, df2,
    code_col      = "标准L3代码",
    source1_label = "注册表",
    source2_label = "映射表",
    sample_n      = 50,
)
save_results(result, "/path/output")
```

---

## 四、边界与限制

| 场景 | 行为 |
|------|------|
| code_col 不存在于 df | 抛出 `KeyError`，提示可用字段 |
| 某一 DataFrame 为空 | 可匹配率为 0，only_in_source2 = 全部 |
| sample_n 超出实际数据量 | 自动按实际数量截断 |
| 两侧 code_col 名称不同 | 需提前在 df 中 rename 对齐 |

---

## 五、命令行使用

### 对比两个 CSV 文件

```bash
python skill_A1_S02.py csv \
    --file1  /path/L3注册表.csv \
    --file2  /path/L3映射表.csv \
    --col    标准L3代码 \
    --label1 注册表 \
    --label2 映射表 \
    --n      30 \
    --out    /path/output/validation
```

### 从数据库查询对比

```bash
python skill_A1_S02.py db \
    --db     /path/ea_knowledge_base.db \
    --query1 "SELECT DISTINCT l3_code FROM fact_activity WHERE l5_activity IS NOT NULL" \
    --query2 "SELECT DISTINCT l3_code FROM fact_activity WHERE agent_score_total IS NOT NULL" \
    --col    l3_code \
    --label1 L3流程库 \
    --label2 Agent评分表 \
    --out    /path/output/validation
```

---

## 六、与其他 Skill 的关系

| Skill | 关系 |
|-------|------|
| A1-S01（文件读取） | 上游：A1-S01 读取 CSV → A1-S02 对比编码差异 |
| A1-S09（L1-L3归属验证） | 并行：A1-S02 识别编码差异 → A1-S09 纠正归属 |

---

*本文档由 Claude Code 自动生成，需架构小组审核后正式入库。*
