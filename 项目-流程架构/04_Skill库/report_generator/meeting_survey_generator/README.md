---
type: 项目笔记
source: 04_Skill库/report_generator/meeting_survey_generator
synced: 2026-06-15
tags: [项目]
---

# 会议转录 → 调研Excel 自动生成器

## 工作流程

```
录制调研会议 → 语音转文字(JSON) → 本程序自动提取 → 调研Excel → 人工核实 → 生成D1-D4
```

## 文件说明

| 文件 | 说明 |
|---|---|
| `generate_survey_from_meeting.py` | 主程序 |
| `meeting_transcript_schema.json` | 会议转录JSON格式示例 |
| `.env.example` | API Key配置模板 |

## 安装依赖

```bash
pip install openpyxl requests psycopg2-binary
```

## 配置Kimi API Key

1. 复制配置模板：
```bash
cp .env.example .env
```

2. 编辑 `.env`，填入你的Kimi API Key（从 https://platform.moonshot.cn/ 获取）

## 用法

### 1. 准备会议转录JSON

参考 `meeting_transcript_schema.json` 的格式，将语音转文字结果整理为JSON：

```json
{
  "meeting_id": "MT-20260520-001",
  "meeting_date": "2026-05-20",
  "topic": "L3-COM 佣金全链路管理调研",
  "participants": [{"name": "JoJo", "role": "中台结算"}],
  "target_l3s": ["L3-COM"],
  "segments": [
    {"speaker": "JoJo", "time": "00:00:45", "text": "每月15号保司发佣金PDF..."}
  ]
}
```

### 2. 运行程序

**针对单个L3：**
```bash
python generate_survey_from_meeting.py \
    --transcript "会议转录.json" \
    --l3-code "L3-COM" \
    --output "调研_L3-COM_20260520.xlsx"
```

**针对多个L3：**
```bash
python generate_survey_from_meeting.py \
    --transcript "会议转录.json" \
    --l3-codes "L3-COM,L3-STLM,L3-SSVA" \
    --output "调研_佣金结算_20260520.xlsx"
```

**针对某个业务域：**
```bash
python generate_survey_from_meeting.py \
    --transcript "会议转录.json" \
    --domain "权益" \
    --output "调研_权益域_20260520.xlsx"
```

**仅规则提取（跳过LLM，不需要API Key）：**
```bash
python generate_survey_from_meeting.py \
    --transcript "会议转录.json" \
    --l3-code "L3-COM" \
    --output "调研_L3-COM_20260520.xlsx" \
    --no-llm
```

### 3. 人工核实

打开生成的Excel，重点核实以下字段：
- 实际触发场景
- 真实执行步骤
- 与数据库差异
- 痛点/堵点

标注 `[LLM]` 的字段表示由Kimi自动提取，建议重点复核。

### 4. 生成D1-D4

核实后的调研Excel可作为 `payment_report_generator` 的输入，生成D1-D4交付物。

## 提取机制

### 规则提取（第一层）
基于关键词匹配，从转录文本中直接提取：
- 触发场景："每月...收到..."
- 执行步骤："先...然后...最后..."
- 执行岗位：说话人身份 + "我负责..."
- 工具/系统："Excel/PDF/手工/银行"
- 痛点："最麻烦/费时/误差"

### LLM提取（第二层）
当规则提取结果不完整时，调用Kimi API补全：
- 将完整转录文本送入LLM
- 要求按固定JSON格式输出
- 置信度标注（high/medium/low）

### 合并策略
- 规则提取有值 → 优先采用（置信度high）
- 规则提取为空 → 采用LLM结果（标注[LLM]）
- 两者都为空 → 留空待人工填写

## 输出Excel结构

| Sheet | 内容 |
|---|---|
| 0_调研说明 | 字段说明与来源标注 |
| 调研执行记录 | 会议元信息（日期、参与人、覆盖L3） |
| L3调研采集表 | **核心**：每个L3的调研字段（系统预填区 + 自动提取区） |
| 差异项汇总 | 空白模板，待人工从采集表提取差异项 |
