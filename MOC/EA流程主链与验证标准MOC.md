---
type: moc
tags: [MOC, 导航, EA, 流程主链, 验证标准]
project: EA流程架构项目
source_type: MOC
created: 2026-08-12
updated: 2026-08-12
---

# EA流程主链与验证标准 MOC

## 一句话定义

这页负责把 EA 主库里的“流程主链”和“验证标准”放在一起看，重点回答：

- 流程主链是怎么推进的
- 每段流程靠什么判定通过
- 哪些关卡是硬性 Gate，哪些是人工复核，哪些是外部确认

它的作用，是让 OBagent 后续不只会找流程节点，还能把“是否完成、如何验收、何时拦截”一起带出来。

---

## 为什么这页重要

流程图只回答“先做什么后做什么”，但 EA 主库里真正决定质量和风险的，是验证标准：

- 没有验证标准，流程只是动作序列
- 没有通过条件，交付只是形式完成
- 没有 Gate 和复核，风险会直接下传

所以这页的重点不是再描述流程，而是把“流程推进逻辑”和“验证逻辑”绑定起来。

---

## 验证视角下的流程主链

建议把 EA 的流程主链理解为三层：

1. 主链流程
2. 验证关卡
3. 验收证据

---

## 第一层：主链流程入口

当前最明确、最适合作为样板主链的是：

- [L3-COM](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/流程卡片/L3-COM.md:1)
- [流程卡片目录](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/流程卡片)

以 [L3-COM](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/流程卡片/L3-COM.md:1) 为例，可以清楚看到：

- 输入 / 输出
- 上下游关系
- L4 子流程清单
- KPI
- 合规红线

这说明 EA 的流程主链表达已经初步成型，下一步真正要强化的是：

- 每个关键 L3/L4 节点对应什么验证模式
- 哪些节点的通过标准已明确
- 哪些节点仍缺终点标准或验收标准

---

## 第二层：通用 Gate 体系

这层是主链之外、跨流程可复用的验证骨架。

关键入口：

- [Gate规则](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate规则.md:1)
- [Gate通过标准](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate通过标准.md:1)
- [Gate①达标挂数要求](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate①达标挂数要求.md:1)
- [Gate②达标落地要求](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate②达标落地要求.md:1)
- [Gate③FAIL即熔断](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate③FAIL即熔断.md:1)

当前可以提炼出两套 Gate：

### A. 外发 / 合规类 Gate

来自 [Gate规则](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate规则.md:1)：

- `G1`：正式源齐全
- `G2`：指标定义齐全
- `G3`：匿名化合规
- `G4`：敏感字段审查
- `G5`：审批确认
- `G6`：外发审批完成

这套更像“内容对外发布或对外证明”时的验证体系。

### B. 三层递进 / 熔断类 Gate

来自 [Gate通过标准](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate通过标准.md:1)：

- `Gate①`：系统化挂数和实时刷新
- `Gate②`：物理产物存在且系统可读
- `Gate③`：交付和审核记录 100% 可追溯

这套更像“流程治理成熟度”的验证体系，一旦关键 Gate FAIL，就会进入熔断补建路径。

---

## 第三层：验证模式分类

从当前原子看，EA 主库里的验证标准大致分成 4 种。

### 1. 流程内置验证

关键入口：

- [内置验证机制](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/内置验证机制.md:1)
- [验证步骤内置于流程](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/验证步骤内置于流程.md:1)

特点：

- 验证不是额外动作
- 验证本身就是流程中的一个步骤

这类适合成熟、边界清楚、验证对象单一的流程。

### 2. 人工复核关卡

关键入口：

- [结算对账需财务复核](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/结算对账需财务复核.md:1)
- [结算对账财务复核关卡](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/结算对账财务复核关卡.md:1)
- [分佣结算人工复核](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/分佣结算人工复核.md:1)
- [高风险步骤人工评估](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/高风险步骤人工评估.md:1)

特点：

- 涉及真实资金、合规、授权、高风险动作
- 不能自动放行
- 必须由人工复核或特定角色确认

这类是 EA 当前非常关键的安全层。

### 3. 外部确认型验证

关键入口：

- [验证标准：客户签署的服务确认书](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/验证标准：客户签署的服务确认书.md:1)
- [通过标准](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/通过标准.md:1)
- [合同确认五条件齐备](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/合同确认五条件齐备.md:1)

特点：

- 不是内部说“完成了”就算完成
- 需要机构、客户、合作方或签字文件确认
- 验收证据是流程闭环的一部分

这类适合对外交付、服务确认、合同生效类流程。

### 4. 治理成熟度验证

关键入口：

- [VN-BAM-01达标标准](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/VN-BAM-01达标标准.md:1)
- [熔断优先处理](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/熔断优先处理.md:1)
- [补建访谈确认](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/补建访谈确认.md:1)

特点：

- 验证对象不是单个动作是否完成
- 而是整个节点是否达到“可持续运行、可追溯、可验证”的成熟状态

这类验证最适合和“规则空白 / 熔断治理”专题联动看。

---

## 当前最值得关注的验证问题

从现有原子看，EA 里最典型的验证缺口包括：

- [终点标准字段为空](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/终点标准字段为空.md:1)
- [跨域资源对接验证缺失](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/跨域资源对接验证缺失.md:1)
- [协议签署系统开通校验缺失](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/协议签署系统开通校验缺失.md:1)
- [原始凭证校验缺失](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/原始凭证校验缺失.md:1)
- [PDF数据校验缺失](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/PDF数据校验缺失.md:1)

这些问题说明当前主链里最脆弱的不是“有没有动作”，而是：

- 是否有明确的完成标准
- 是否有可执行的校验
- 是否有可追溯的验收证据

---

## 建议的浏览路径

### 路径 A：先看通用验证骨架

1. [Gate规则](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate规则.md:1)
2. [Gate通过标准](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/Gate通过标准.md:1)
3. [EA规则空白与熔断治理MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA规则空白与熔断治理MOC.md:1)

### 路径 B：先看主链中的验证

1. [L3-COM](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/流程卡片/L3-COM.md:1)
2. [流程卡片目录](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/流程卡片)
3. 回跳到本页的“验证模式分类”

### 路径 C：先看验收与证据

1. [通过标准](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/通过标准.md:1)
2. [验证标准：客户签署的服务确认书](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/验证标准：客户签署的服务确认书.md:1)
3. [合同确认五条件齐备](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/EA流程架构项目/合同确认五条件齐备.md:1)

---

## 对 OBagent 的直接价值

这页会直接增强 OBagent 三类能力：

1. **流程检索能力**：不仅能找到流程节点，还能找到该节点的通过条件
2. **风险解释能力**：能区分“流程没做完”和“流程做了但未验证”
3. **治理建议能力**：遇到验证缺口时，能更快判断该补 Gate、补人工复核，还是补外部验收证据

---

## 与其他 MOC 的关系

- 本页负责：EA 的流程主链与验证标准
- [EA核心项目知识总览MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA核心项目知识总览MOC.md:1) 负责：EA 总入口
- [EA规则空白与熔断治理MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA规则空白与熔断治理MOC.md:1) 负责：风险治理链
- [EA Agent机制与流程交接MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA%20Agent机制与流程交接MOC.md:1) 负责：执行面与交接面
- [Jasper经验到EA应用映射MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/Jasper经验到EA应用映射MOC.md:1) 负责：治理经验映射

