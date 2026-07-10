---
type: project_note
project: 流程架构
layer: "04_Skill库"
layer_tag: Skill
subdir: "草稿"
tags: [Skill]
---

## 🧭 导航
⬆️ [[04_Skill库]] · ⬆️ [[草稿]] · 🏠 [[流程架构项目MOC]]

---

# A1-S01 — 多格式文件读取与 Schema 统一

**Skill ID**：A1-S01
**版本**：V1.0
**归属 Agent**：A1（EA数据库维护）
**创建日期**：2026-04-28
**状态**：可用

---

## 一、这个 Skill 做什么

自动识别 `.csv` / `.md` / `.txt` 文件类型，处理编码差异，将读取结果统一为
标准 DataFrame，并支持将字段对齐到目标 schema。

**核心特性**：
- 编码自动检测：按 `utf-8-sig → utf-8 → gbk → gb2312 → latin-1` 顺序尝试
- CSV BOM 自动去除，列名去空格处理
- CSV 首行全 Unnamed 自动降级（兼容 VS-5 类型的表格）
- MD 文件自动提取所有标准表格，合并为单一 DataFrame
- TXT 文件按行读取，返回单列 DataFrame
- Schema 统一：支持多候选列名映射到标准字段名

---

## 二、函数签名

### `read_source_file(file_path, csv_kwargs=None) -> dict`

```python
from skill_A1_S01 import read_source_file

result = read_source_file("/path/to/file.csv")
# result = {
#     "df":        pd.DataFrame,
#     "file_type": "csv" | "md" | "txt",
#     "encoding":  "utf-8-sig" | "gbk" | ...,
#     "row_count": int,
#     "columns":   list[str],
#     "warnings":  list[str],
# }
```

### `unify_schema(df, target_schema) -> pd.DataFrame`

```python
from skill_A1_S01 import unify_schema, SCHEMA_FACT_ACTIVITY

df_unified = unify_schema(df_raw, SCHEMA_FACT_ACTIVITY)
```

### `read_and_unify(file_path, target_schema) -> dict`

```python
from skill_A1_S01 import read_and_unify, SCHEMA_VALUE_STREAM

result = read_and_unify("/path/VS-3.csv", SCHEMA_VALUE_STREAM)
df = result["df_unified"]   # schema 对齐后的 DataFrame
```

---

## 三、内置 Schema 模板

| 常量名 | 用途 |
|--------|------|
| `SCHEMA_FACT_ACTIVITY` | L3流程库 CSV → fact_activity 字段对齐 |
| `SCHEMA_VALUE_STREAM` | 价值流 CSV → dim_value_stream 字段对齐 |
| `SCHEMA_JD` | JD Markdown → dim_job_family 字段对齐 |

---

## 四、典型调用示例

### 读取 VS CSV 并对齐 schema

```python
from skill_A1_S01 import read_and_unify, SCHEMA_VALUE_STREAM

result = read_and_unify(
    "/path/VS-2_机构合作伙伴旅程.csv",
    SCHEMA_VALUE_STREAM
)
print(result["file_type"])       # "csv"
print(result["encoding"])        # "utf-8-sig"
print(result["df_unified"].head())
```

### 读取 JD Markdown 并提取表格

```python
from skill_A1_S01 import read_source_file

result = read_source_file("/path/JD_A_保司交付_V0.2.md")
print(result["row_count"])   # 提取到的表格行数
print(result["df"])          # 合并后的表格 DataFrame
```

### 自定义 schema

```python
from skill_A1_S01 import read_and_unify

my_schema = {
    "l3_code": ["L3-编号", "L3编号", "l3_code"],
    "l3_name": ["L3-名称", "l3_name"],
    "l4_code": ["L4-编号", "l4_code"],
}

result = read_and_unify("/path/流程库.csv", my_schema)
```

---

## 五、边界与限制

| 场景 | 行为 |
|------|------|
| 文件不存在 | 抛出 `FileNotFoundError` |
| 不支持的格式（如 .xlsx） | 抛出 `ValueError` |
| CSV 所有编码均失败 | 抛出 `ValueError` |
| MD 文件无标准表格 | 返回空 DataFrame，warnings 中记录 |
| Schema 中字段在 df 中找不到 | 该字段填充 `None`，不报错 |

---

## 六、命令行使用

```bash
# 只读取，预览前3行
python skill_A1_S01.py --input /path/file.csv

# 读取 + schema 统一 + 输出
python skill_A1_S01.py \
    --input  /path/VS-2.csv \
    --schema /path/schema.json \
    --out    /path/output.csv
```

`schema.json` 格式：
```json
{
    "l3_code": ["L3-编号", "L3编号"],
    "l3_name": ["L3-名称"]
}
```

---

## 七、与其他 Skill 的关系

| Skill | 关系 |
|-------|------|
| A1-S02（编号差异识别） | 并行：A1-S01 读取文件后，A1-S02 对比编码差异 |
| A1-S03（推导补录） | 上游：A1-S01 读取数据 → A1-S03 写入数据库 |
| A1-S08（VS-L3映射） | 上游：A1-S01 可用于读取 VS 全量分析汇总表 |

---

*本文档由 Claude Code 自动生成，需架构小组审核后正式入库。*

