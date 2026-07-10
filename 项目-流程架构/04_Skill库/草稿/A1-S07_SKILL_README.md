---
type: 项目笔记
source: 04_Skill库/草稿
synced: 2026-06-15
tags: [项目]
---

# A1-S07 — L3编码标准化

**Skill ID**：A1-S07
**版本**：V1.0
**归属 Agent**：A1（EA数据库维护）
**参考标准**：L3编码映射标准 V1.1
**创建日期**：2026-04-23
**状态**：可用

---

## 一、这个 Skill 做什么

基于用户确认的7条映射规则，将原始 L3 编码标准化。支持：

- **单条处理**：`normalize_l3_code()` — 可被其他 Python 脚本直接 import
- **批量处理**：`normalize_l3_batch()` — 读取 CSV，写出映射表，可选同步写库
- **L4 前缀同步**：`get_l4_prefix_update()` — 返回 L3 变更对应的 L4 前缀更新
- **来源置信度**：每行附加 `confirmation_status` 字段

**7条映射规则**：

| 规则 | 适用编码 | 操作 |
|------|----------|------|
| R1 | CDA/COB/KASC/OBC/SLCM/SLM/SRA | 名称以注册表为准，编码不变 |
| R2 | COM-01/02/03、PROC-01~08、BMC-01~06 | 编码改为纯字母，名称以注册表为准 |
| R3 | ISD | 按服务商关键词拆分为8个独立编码 |
| R4 | RSD/RSD-RW/RSD-JD | 按名称含义拆分：L3-RSD（权益）/ L3-RSJD（经代） |
| R5 | L3-C、L3-CR、L3-KART | 删除 |
| R6 | 仅来自归一化表 | 删除 |
| RD | BMD/BME/MSI/MSE | 直接删除 |

---

## 二、函数签名

### 单条标准化

```python
from skill_A1_S07 import normalize_l3_code

result = normalize_l3_code(l3_code="L3-COM-01", l3_name="永明佣金政策分发")
# 返回：
# {
#     "std_code":    "L3-CMU",
#     "std_name":    "永明保司佣金政策接收校准与标准化分发",
#     "change_type": "R2",
#     "is_changed":  True,
#     "needs_human": False,
#     "action":      "rename"
# }
```

### 批量处理

```python
from skill_A1_S07 import normalize_l3_batch

result = normalize_l3_batch(
    input_path = "path/to/L3流程编码全量表.csv",
    output_dir = "path/to/output/",
    db_path    = "path/to/ea_knowledge_base.db",  # 可选，写库
    log_path   = "path/to/logs/a1s07.txt",        # 可选，写日志
)
```

### L4 前缀查询

```python
from skill_A1_S07 import get_l4_prefix_update

old_pfx, new_pfx = get_l4_prefix_update("L3-COM-01", "L3-CMU")
# → ("L4-COM-01", "L4-CMU")
```

---

## 三、参数说明

### normalize_l3_batch

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `input_path` | str | ✅ | L3流程编码全量表.csv 路径 |
| `output_dir` | str | ✅ | 输出目录，写出 L3编码修改映射表.csv |
| `db_path` | str | ❌ | SQLite数据库路径；传入则更新 fact_activity/dim_value_stream |
| `log_path` | str | ❌ | 日志输出路径 |

### 返回值

```python
{
    "status":      "ok" | "error",
    "total":       int,   # 保留记录数（不含删除）
    "changed":     int,   # 发生变更的记录数
    "deleted":     int,   # 删除的记录数
    "needs_human": int,   # 需人工确认的记录数
    "output_csv":  str,   # 输出 CSV 路径
    "db_updated":  bool,
}
```

---

## 四、confirmation_status 规则

| 来源文件包含 | confirmation_status |
|------------|---------------------|
| 注册表 | 🟢 业务确认 |
| L3流程库 / L2流程库 | 🟠 草稿态 |
| JD映射 | 🔴 规划态（Teresa GAP-01 未完成） |
| 其他 | 🟡 推导态 |

优先级：🟢 > 🟠 > 🟡 > 🔴（多来源时取最高置信度）

---

## 五、输入 CSV 格式

| 列名 | 必填 | 说明 |
|------|------|------|
| `l3_code` | ✅ | 原始 L3 编码 |
| `l3_name` | ✅ | 原始 L3 名称 |
| `一致性` | ❌ | 一致性标记（透传到输出） |
| `来源文件` | ✅ | 分号分隔的来源文件名列表（用于确认状态判断） |

---

## 六、边界与限制

| 场景 | 行为 |
|------|------|
| R3 ISD 关键词无匹配 | action="delete"，needs_human=True，日志记录 |
| R4 RSD 名称无关键词匹配 | 默认映射到 L3-RSD（权益方案框架设计） |
| db_path 中表不存在 | 抛出异常，status="error" |
| 输出目录不存在 | 自动创建 |
| 归一化表独有记录 | 直接跳过（不出现在输出 CSV 中） |

---

## 七、复现指令

```bash
# 1. 确认依赖（仅标准库，无需安装）
python --version   # >= 3.10

# 2. 将 skill_A1_S07.py 和 mapping_rules.json 放到同一目录

# 3. 命令行调用：
python skill_A1_S07.py \
    --input  /path/to/output/L3流程编码全量表.csv \
    --output /path/to/output/ \
    --db     /path/to/ea_knowledge_base.db \
    --log    /path/to/output/logs/a1s07.txt

# 4. Python import 调用：
python3 -c "
from skill_A1_S07 import normalize_l3_code
print(normalize_l3_code('L3-COM-01', '永明佣金'))
"
```

---

## 八、与其他 Skill 的关系

| Skill | 关系 |
|-------|------|
| A1-S01（数据库构建） | 上游：A1-S07 依赖已存在的 fact_activity / dim_value_stream |
| A1-S03（推导补录） | 并行：补录后可调用 A1-S07 对新补录行进行编码标准化 |
| A1-S02（数据质量报告） | 下游：标准化后可重新评估编码一致性 |

---

*本文档由 Claude Code 自动生成，需架构小组审核后正式入库。*
