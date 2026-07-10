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

# A1-S04 — 多源数据分栏组装

**Skill ID**：A1-S04
**版本**：V1.0
**归属 Agent**：A1（EA数据库维护）
**创建日期**：2026-04-22
**状态**：可用

---

## 一、这个 Skill 做什么

给定岗位族代码（如 `'A'`），从 SQLite 数据库组装两栏数据：

- **L3流程库栏**：有 `l5_activity` 的行（来自 L3流程库 CSV）
- **Agent评分栏**：有 `agent_score_total` 的行（来自 Agent化严谨评分 CSV）

并输出 Markdown 分布报告，包含 L3 关联分析、L3 行数分布、Agent Tier 统计。

**核心特性**：
- 自动补录 `data_source` 字段（幂等，已有则跳过）
- 参数化岗位族代码，支持 A/B/C/DE/F/G 族
- 不依赖硬编码路径
- 返回结构化 dict，可直接被下游 Agent（A2）消费

---

## 二、函数签名

```python
from skill_A1_S04 import build_job_family_data_report

result = build_job_family_data_report(
    db_path         = "path/to/ea_knowledge_base.db",
    job_family_code = "A",           # 'A' | 'B' | 'C' | 'DE' | 'F' | 'G'
    output_path     = "path/to/A族数据分布报告.md",
)
```

### 返回值

```python
{
    "status":           "ok" | "error",
    "rows_lib":         int,   # 来自流程库的行数
    "rows_agent":       int,   # 来自Agent评分的行数
    "l3_only_lib":      list,  # 仅在流程库的 L3 编码
    "l3_only_agent":    list,  # 仅在Agent评分的 L3 编码
    "l3_both":          list,  # 两表均有的 L3 编码
    "data_source_dist": dict,  # 全表 data_source 分布
    "output_path":      str,
}
```

---

## 三、参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `db_path` | str | ✅ | SQLite数据库绝对路径 |
| `job_family_code` | str | ✅ | 岗位族代码，须与 bridge_l4_job.job_family_code 匹配 |
| `output_path` | str | ✅ | 报告输出路径（.md），目录不存在时自动创建 |

---

## 四、典型调用示例

### 生成 A族（保司资源投放）数据分布报告

```python
from skill_A1_S04 import build_job_family_data_report

result = build_job_family_data_report(
    db_path         = "/path/to/ea_knowledge_base.db",
    job_family_code = "A",
    output_path     = "/path/to/output/validation/A族数据分布报告.md",
)
print(result["rows_agent"], result["l3_only_agent"])
```

### 生成 B族 报告

```python
result = build_job_family_data_report(
    db_path         = DB,
    job_family_code = "B",
    output_path     = "output(Claude)/validation/B族数据分布报告.md",
)
```

---

## 五、边界与限制

| 场景 | 行为 |
|------|------|
| job_family_code 在 bridge_l4_job 中无对应行 | 生成空表格报告，rows_lib=0, rows_agent=0 |
| data_source 字段已存在 | 跳过补录，直接读取现有值 |
| fact_activity 中存在 "流程库+Agent评分" 来源 | 该行归入 df_all 但不计入 df_lib/df_agent |
| output_path 目录不存在 | 自动 makedirs |

---

## 六、复现指令

```bash
# 1. 确认依赖
pip install pandas tabulate

# 2. 将 skill_A1_S04.py 放到项目目录或加入 PYTHONPATH

# 3. 命令行调用：
python skill_A1_S04.py \
    --db /path/to/ea_knowledge_base.db \
    --family A \
    --out /path/to/output/validation/A族数据分布报告.md
```

---

## 七、与其他 Skill 的关系

| Skill | 关系 |
|-------|------|
| A1-S03（推导补录） | 并行：补录数据后可调用 A1-S04 重新验证分布 |
| A2-S01（岗位→查询参数） | 下游：A1-S04 的返回 dict 直接被 A2-S01 消费 |
| A1-S02（数据质量报告） | 并行：同样基于 fact_activity，可联合使用 |

---

*本文档由 Claude Code 自动生成，需架构小组审核后正式入库。*

