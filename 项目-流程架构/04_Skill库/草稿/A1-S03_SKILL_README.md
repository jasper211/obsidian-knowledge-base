---
type: 项目笔记
source: 04_Skill库/草稿
synced: 2026-06-15
tags: [项目]
---

# A1-S03 — 推导补录与溯源标注

**Skill ID**：A1-S03  
**版本**：V1.0  
**归属 Agent**：A1（EA数据库维护）  
**创建日期**：2026-04-22  
**状态**：可用

---

## 一、这个 Skill 做什么

将从非结构化来源（JD文档、访谈、会议纪要）**推导**出的结构化数据，幂等写入 SQLite 目标表，并自动标注数据来源，输出可追溯的补录日志。

**核心特性**：
- 幂等保护：同一批数据不会被重复插入
- 字段对齐：自动对齐目标表字段，多余字段丢弃，缺失字段填 None
- 溯源标注：每行写入 `source_file` 字段，说明数据来源
- 标准日志：每次执行输出结构化日志文件

---

## 二、函数签名

```python
from skill_A1_S03 import supplement_table, sync_table_to_csv

result = supplement_table(
    db_path      = "path/to/ea_knowledge_base.db",
    target_table = "dim_value_stream",        # 目标表名（必须已存在）
    stage_name   = "授权与合同",               # 本次补录的阶段名（用于日志标题+去重）
    rows_data    = [...],                      # list[dict]，每个dict=一行数据
    source_tag   = "来源：JD_A_V0.2推导",      # 写入source_file字段
    dedup_keys   = ["vs_id", "value_stage"],  # 去重检查键（可选，默认自动推断）
    log_path     = "output(Claude)/logs/xxx.txt",  # 日志路径（可选）
)
```

### 返回值

```python
{
    "status":        "inserted" | "skipped" | "error",
    "rows_inserted": int,   # 实际插入行数
    "rows_existing": int,   # 幂等检查发现的已有行数
    "log_lines":     list[str],
    "log_path":      str    # 仅当传入log_path时
}
```

---

## 三、参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `db_path` | str | ✅ | SQLite数据库绝对路径 |
| `target_table` | str | ✅ | 目标表名，表必须已存在 |
| `stage_name` | str | ✅ | 本批数据的分组名，用于去重WHERE条件构建和日志标题 |
| `rows_data` | list[dict] | ✅ | 补录数据行，每行一个dict，key为字段名 |
| `source_tag` | str | ✅ | 溯源说明，写入source_file字段 |
| `dedup_keys` | list[str] | ❌ | 去重检查字段；None时自动推断（优先vs_id+value_stage） |
| `log_path` | str | ❌ | 日志文件输出路径；None时不写文件 |

---

## 四、典型调用示例

### 补录 VS-2"机构需求诊断"阶段

```python
from skill_A1_S03 import supplement_table, sync_table_to_csv

rows = [
    {
        "vs_id": "VS-2", "vs_name": "机构合作伙伴旅程",
        "value_stage": "机构需求诊断",
        "value_activity": "机构业务现状调研与痛点收集",
        "l3_mapping": "L3-BMD", "l1_mapping": "L1-02",
        "entry_condition": "机构完成初步接触",
        "exit_condition": "联合诊断报告确认",
    },
    {
        "vs_id": "VS-2", "vs_name": "机构合作伙伴旅程",
        "value_stage": "机构需求诊断",
        "value_activity": "需求合规性初筛与高风险处置",
        "l3_mapping": "L3-BMD", "l1_mapping": "L1-02",
        "entry_condition": "机构完成初步接触",
        "exit_condition": "联合诊断报告确认",
    },
]

result = supplement_table(
    db_path      = DB,
    target_table = "dim_value_stream",
    stage_name   = "机构需求诊断",
    rows_data    = rows,
    source_tag   = "来源：JD_C_机构业务族_V0推导，待确认",
    log_path     = "output(Claude)/logs/vs2_补录日志.txt",
)

# 同步更新CSV
sync_table_to_csv(DB, "dim_value_stream", "output(Claude)/dim_value_stream_cleaned.csv")
```

### 补录其他表（如 fact_activity 新增行）

```python
result = supplement_table(
    db_path      = DB,
    target_table = "fact_activity",
    stage_name   = "L3-IAO补充L5活动",
    rows_data    = [...],
    source_tag   = "来源：L3-IAO协同框架txt提取",
    dedup_keys   = ["l3_code", "l4_code", "l5_sequence"],
)
```

---

## 五、边界与限制

| 场景 | 行为 |
|------|------|
| 目标表不存在 | 抛出异常，status="error"，写入日志 |
| rows_data为空列表 | 插入0行，status="inserted"，不报错 |
| 字段不在目标表中 | 自动丢弃，日志中记录警告 |
| dedup_keys对应值全为None | 去重条件退化为1=1，**每次都会插入** —— 避免此情况 |
| 同一批次重复调用 | 幂等保护生效，status="skipped" |
| source_file字段不存在于表中 | source_tag被丢弃（字段对齐阶段处理） |

---

## 六、复现指令（其他人直接调用）

```bash
# 1. 确认依赖
pip install pandas

# 2. 将 skill_A1_S03.py 放到项目目录或加入 PYTHONPATH

# 3. 调用示例（见第四节）
#    或直接运行 demo（需传入路径参数）：
python skill_A1_S03.py \
    --db /path/to/ea_knowledge_base.db \
    --out /path/to/output
#    → 会尝试补录VS-1授权与合同（幂等，已有数据会跳过）
#    → 输出日志到 <out>/logs/skill_A1S03_demo.txt
```

---

## 七、与其他 Skill 的关系

| Skill | 关系 |
|-------|------|
| A1-S01（数据库构建） | 上游：A1-S03 依赖 A1-S01 建好的表结构 |
| A1-S04（多源分栏组装） | 下游：A1-S03 补录的数据会被 A1-S04 读取用于报告生成 |
| A1-S02（数据质量报告） | 并行：补录后可调用 A1-S02 重新评估完整度 |

---

*本文档由 Claude Code 自动生成，需架构小组审核后正式入库。*
