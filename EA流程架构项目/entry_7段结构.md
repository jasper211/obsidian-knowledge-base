---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/AI上下文/2026-05-09_sync_to_jasper_v0_1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-09
entity_type: 非正式主题
entity_ref: 经验引用结构
extracted_at: 2026-07-16T11:51:52
status: 待裁定
conflict_group: 经验引用结构
---

# entry 7段结构

experience-engine v2.1 的 entry 数据结构包含 7 段：a business_framework（业务场景/核心命题/适用条件）、b causal_logic（显性因果链）、c root_cause（底层原理）、d quantitative_thresholds（数字阈值）、e application_scenarios（B2B/B2A 列表）、f do_and_dont（能做/不能做列表）、g risks_and_mitigations（风险/缓释列表）。其中 f/g 是业务实战版段头。

## 关联概念

- [[11元数据]]
- [[A/B/C/D 4类基线]]

## 所属枢纽

- [[经验引用结构]]

## ⚠️ 待裁定：entity_ref矛盾（经验引用结构）

与同组原子存在冲突：[[经验引用粒度升级]]、[[7段结构化内容]]、[[11元数据]]、[[11个必填元数据字段]]

冲突说明：关于entry结构，'entry 7段结构'列出7段（a-g），而'7段结构化内容'列出7段但包含action_items和risk_and_limitations，与前者f/g段名不同；且'11元数据'要求11个字段，但'11个必填元数据字段'也要求11个但字段列表略有差异（如'原话引用'在后者中为必填，前者未明确）。此外，'经验引用粒度升级'要求引用a、c、f三段，与'7段结构化内容'要求所有7段不一致。

（标记时间：2026-07-21T20:56:43）
