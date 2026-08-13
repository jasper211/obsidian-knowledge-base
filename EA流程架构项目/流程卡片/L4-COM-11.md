---
type: process_card
card_level: L4
entity_ref: L4-COM-11
project: EA流程架构项目
parent_entity_ref: L3-COM
aliases: [银行到账确认与实收对账（待注册）]
linked_l3: [L3-COM]
linked_vn: [VN-PAY-02]
edges: [L3-COM, L4-COM-10, L4-COM-12, L4-COM-13, L4-COM-17, VN-PAY-02]
source: 流程蓝图_L3-COM_佣金全链路管理_V1.0.md / L3-COM.json（VNW模型快照）/ process_analytics.dim_vn
status: draft（本卡片本身未经Terresa/Mark确认）
version: v4
completeness: complete
gaps: 无
---
# L4-COM-11 银行到账确认与实收对账（待注册）

上级节点：[[L3-COM]]

起点：提取银行流水与回单（OCR并形成fact_bank_inflow候选数据）（任务11-a） [流程模型·C面板任务卡片工作坊·首个任务]
目的（规则场景）：当银行流水与保司账单到位后，触发实收对账场景：应收与实收自动匹配，差异按原因码分类；只有确认"已对平"状态的数据才能进入下一步，规则不允许带着未解释差异向下游传递。 [大模型分析撰写，基于流程模型B/C面板综合，非字段拼接]
终点：差异分类与平衡确认（补原因码并确认已对平状态）（任务11-c） [流程模型·C面板任务卡片工作坊·末个任务]

输入：提取银行流水与回单（OCR并形成fact_bank_inflow候选数据）所需材料：银行流水 + 保司账单 + COM-10应收明细清单 [输入=任务01（起点任务），蓝图原文交叉核对一致]
阶段/活动：11-a提取银行流水与回单→11-b应收与实收自动匹配→11-c差异分类与平衡确认
输出：《实收清单》 + 《差异对照表》 [流程模型·deliverable]

上游：[[L4-COM-10]]
下游：[[L4-COM-12]]
（上下游关系说明：主链线性顺序）
KPI（质量锚点）：应收与实收可勾稽，差异有原因码，回单和版本可追溯

能力：回单OCR、应实匹配、差异归因、平衡校验
岗位：佣金合规族（JF-07）

RACI（岗位，非人名）：主责(A)：财务　执行(R)：财务　咨询(C)：中台支持（应派计算）　知会(I)：—

关联价值节点：[[VN-PAY-02]] 佣金实收确认表

---
（以下不在模版字段范围内，供参考）
dim_process状态：（待注册）
模型建议方向（MODEL_DRAFT，未确认）：治理银行回单结构化与差异字典，再推进Aug自动对账（自动匹配+人工确认差异）
