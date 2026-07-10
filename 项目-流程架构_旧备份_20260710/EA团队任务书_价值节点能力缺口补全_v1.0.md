---
type: 项目笔记
source: 08_任务与跟进/任务状态
synced: 2026-06-15
tags: [项目]
---

# EA 团队任务书 · 价值节点能力缺口补全 v1.0

> **签发**: Mark　**承接**: Jasper（执行负责人）　**日期**: 2026-06-13
> **依据**: BO-1.1 能力问题全集 §3（25 个 Gate=FAIL 价值节点）+ `D1_价值节点清单_V3.21.xlsx / sheet5 熔断与P0行动清单`（行动事项的唯一权威源）
> **关系**: 取代工作草案 `BO-1.1_EA能力缺口补全_任务动作包_v0.1.md`，本文件为可直接派发版。

---

## 0. 任务一句话

把 sheet5 已经写好的「熔断与 P0 行动清单」**激活 → 派发 → 闭环**到 3-gate 复评 PASS。**不重写行动**（sheet5 已有根因+行动+期望产出+owner），本任务书只补 sheet5 缺的两环：**派发授权** 与 **闭环追踪**。

## 1. Jasper 要交付的

25 个 Gate=FAIL 价值节点全部完成 3-gate 复评 PASS（或经 Mark 显式延期），节奏沿 sheet5 Section D 里程碑，整包目标 **T+3 月熔断率 → 0%**。

## 2. 裁定与授权分工 —— 回答"Mark 要不要拍全部 6 个"

> **结论：不用。Mark 此刻只需拍 1 个战略点（D3）。** 其余节点 owner 在 sheet5 已指定、或属执行级由 Jasper 提案。

| 类别 | 项 | 谁定 | 是否阻塞派发 |
|---|---|---|---|
| 🔴 战略·待 Mark 拍 | **D3 资金管理架构**（支付中心 vs 三条线各自管理） | **Mark** | 仅 gate 财务子流（VN-BAM-01 / VN-CFM-01 + PAY 结算口径）；其余 23 节点不等 |
| 🟡 sheet5 已指定 owner·直接派 | HR→袁林/Terresa · IBRD/INS→Terresa(+牌照端) · KA(KASC/KAEM)→交付经理+MoMo+IS · 代理人(FLM/FOB/FOR/FTR/FBA/FPG)→组织发展经理/总部/产品经理/分公司 | 已定 | 否 |
| 🟢 执行级·Jasper 提案人 + Mark 在 Phase A 确认 | D5 报销负责人(VN-PAY-08,P1) · D6 MGA/权益团队→具体人(MGA-01/02/03、EQ-01) · D4 VN-PAY-06 FPG-05 归属(Pebbles+Carrie) | Jasper 提案 | 否（不必预先逐拍） |
| 🟣 EA 建模·Terresa/Jasper 提案 + Mark 确认 | D7 L3-IAC 拆分（谈判 + 授权确认 两个 L3） | 提案后 Mark 确认 | 否 |
| ⚪ 已定(provisional) | D1 IA 合规 = Terresa 临时(规则/协调/验收) + 实现手 Carrie 或新工程师 | Mark 待终认实现手 | 否 |
| ⏸️ 挂起 | D2 对账周期(季度/半年) | 待田总 cadence + Carrie 自动化可行性 | 否（节点照派，仅周期项挂起） |

## 3. 行动内容来源（唯一权威，不另立第二真源）

每个节点的「行动事项 + 期望产出」**全部以 D1 sheet5 Section A/B 为准**。本任务书不重写动作，避免与 EA 现有方案产生第二真源（例：VN-PAY-04 = IA 规则代码化 + 新增 L4-COM-17/15 + 银行回执自动归档管线 + 阈值实时监控仪表盘，见 sheet5 Section A）。

## 4. 节点清单（25 个 Gate=FAIL，按优先级分组）

> 失败 Gate：①挂数 / ②落地 / ③追溯。owner 取自 sheet5。

**A. 财务/佣金链（最高优先 · P0/熔断）**

| 节点 | 失败 Gate | 优先级 | owner(sheet5) | 依赖 |
|---|---|---|---|---|
| VN-PAY-04 转介费派发确认台账 | ①②③ | P0熔断 | IA合规(D1:Terresa临时/Carrie实现) | — |
| VN-PAY-09 体系外对账表 | ①②③ | P0强制熔断 | Carrie+Chaya | 周期项=D2挂起(节点照建) |
| VN-BAM-01 银行账户全周期管理 | ①②③ | P0 | Chaya/财务 | **D3 资金架构** |
| VN-CFM-01 现金流管理报告包 | ①②③ | P0 | Chaya/财务 | **D3 资金架构** |
| VN-PAY-06 理财师综合应派清单 | ①③ | P0 | Pebbles+Carrie | D4(FPG-05归属) |
| VN-PAY-08 报销凭证包 | ①② | P1 | HR/行政 | D5(指派) |

**B. MGA / 权益（P1熔断 · 模板缺失类）**

| 节点 | 失败 Gate | owner(sheet5) | 依赖 |
|---|---|---|---|
| VN-MGA-01 联合运营需求诊断包 | ①②③ | BD/MGA团队 | D6 |
| VN-MGA-02 联合运营框架方案 | ①③ | BD/MGA团队 | D6 |
| VN-MGA-03 联合运营合约包 | ①③ | MGA/法务 | D6 |
| VN-EQ-01 同行经代服务方案 | ①③ | 权益/BD | D6 |
| VN-EQ-09 权益上市推广素材 | ①②③ | 权益/BD（见sheet5） | D6 |

**C. HR / 保险（owner 已定，直接派）**

| 节点 | 失败 Gate | 优先级 | owner(sheet5) |
|---|---|---|---|
| VN-HR-05 人力资源诊断与改善报告 | ② | P0 | 袁林 |
| VN-HR-10 员工档案 | ② | P0 | 袁林 |
| VN-HR-08 员工成长路径方案 | ③ | P1熔断 | Terresa |
| VN-IBRD-01 合作伙伴尽调记录 | ③ | 熔断 | Terresa/MoMo |
| VN-INS-01《可行性报告》 | ①②③ | P1 | Mark(CEO)/牌照端 |

**D. 代理人/理财师（VS-4 · owner 已定，直接派 · 均 P1）**

| 节点 | 失败 Gate | owner(sheet5) |
|---|---|---|
| VN-FLM-01 招募计划与执行记录 | ②③ | 分公司组织发展经理/总部 |
| VN-FOB-02 新人90天培养计划 | ③ | 组织发展经理/产品经理/总部 |
| VN-FOR-01 首单陪跑记录 | ③ | 组织发展经理/团队长/产品经理/副总 |
| VN-FTR-01 培训课程体系 | ③ | 交付经理/总部 |
| VN-FBA-01 月度/季度经营分析报告 | ③ | 组织发展经理/分公司总经理/总部 |
| VN-FPG-01 月度/季度考核指标表 | 待建设/③ | 总部/组织发展经理 |

**E. KA（VS-3 · owner 已定，直接派 · 均 P1）**

| 节点 | 失败 Gate | owner(sheet5) |
|---|---|---|
| VN-KASC-01 KA 合同/协议签署版 | ③ | 交付经理/MoMo |
| VN-KAEM-01 KA 培训完成记录 | ②③ | 交付经理/MoMo/IS |
| VN-KAEM-02 KA 资讯发放核销记录 | ③ | 交付经理/IS/MoMo |

## 5. 完成定义（闭环 = 可机验）

- **单节点闭环** = 3 个 Gate 复评由 FAIL→PASS（挂数/落地/追溯），**或** Mark 显式延期（须带理由 + 重新触发条件，禁"够用"式延期）。
- **追踪台账** = `能力问题全集_v1.0.csv` 的 CQ-id + src_status；每次复评回写 Gate 状态，全集重跑即出最新熔断率（机器可验，不靠口头）。
- **整包目标** = sheet5 Section D：T+3 月熔断率→0%，25 节点全 3-gate PASS（或显式延期）。

## 6. 路由与回执（EA 铁律）

Mark → **Jasper**（唯一对 Mark 回执 Owner）→ 各 owner；Terresa 在出包前完成 02 层质量把关；Jasper 管 Phase A–F 六阶段闭环。每 Phase 回执 Mark：进展 / 受阻 / 待 Mark 项。任务状态入 `08_任务与跟进/任务状态/`。

## 7. 不阻塞声明

- **D2 挂起**、**D3 仅 gate 2 个财务节点**，其余 **23 节点即时可派发**，不等任何 Mark 裁定。
- 范围限 25 个 FAIL 节点；39 个 PARTIAL 节点（弱 gate 补强）作第二批，sheet5 Section B 已列部分。
