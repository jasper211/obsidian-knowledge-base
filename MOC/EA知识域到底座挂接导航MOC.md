---
type: moc
tags: [MOC, EA, 治理底座挂接, 导航, OB]
project: EA流程架构项目
source_type: MOC
created: 2026-08-12
updated: 2026-08-12
---

# EA知识域到底座挂接导航 MOC

## 一句话定义

这页不再只是讲 `EA知识域` 是什么，而是把 `EA` 如何挂到公司级治理底座上，直接整理成一张可浏览、可回跳、可给 agent 调用的导航页。

它回答的是：

- 六张公司级底座卡在 EA 里分别对应哪些入口
- 想看 EA 的流程、边界、交接、判断、状态、异常治理时，应先跳哪里
- agent 处理 EA 问题时，应该先调哪张底座卡，再回到哪张 EA 专题页

---

## 为什么这页重要

前面我们已经完成了两步：

1. 把公司级治理底座 6 张卡落了下来
2. 把 `EA知识域定义` 补成了第一张“项目域挂底座”的样板

但如果没有这张导航页，关系仍然更偏“定义层”，还不够像可直接使用的工作入口。

这页的作用就是把：

- 公司级底座
- EA 专题 MOC
- EA 项目知识域

三者真正接成一层“导航即调用”的结构。

---

## EA 挂接公司级底座的总图

先把 EA 当前的挂接关系压缩成一句话：

`先用公司级底座理解治理骨架，再回到 EA 专题页找具体业务真相。`

对应关系可以先理解成两层：

### P0：结构治理挂接

- `公司级通用流程与验证标准` -> `EA流程主链与验证标准MOC`
- `公司级Owner与边界规则` -> `EA Agent机制与流程交接MOC`
- `公司级交接与共享对象原则` -> `EA Agent机制与流程交接MOC`

### P1：高阶治理挂接

- `公司级判断决策闭环` -> `EA规则空白与熔断治理MOC` + `Jasper经验到EA应用映射MOC`
- `公司级状态一致性与Crosswalk校验` -> `EA流程主链与验证标准MOC` + `Jasper经验到EA应用映射MOC`
- `公司级SOP质量与异常暴露机制` -> `EA规则空白与熔断治理MOC` + `Jasper经验到EA应用映射MOC`

---

## 第一组：流程与验证标准挂接

### 对应的公司级底座卡

- [公司级通用流程与验证标准](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/公司级通用流程与验证标准.md:1)

### 在 EA 中的主入口

- [EA流程主链与验证标准MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA流程主链与验证标准MOC.md:1)
- [EA核心项目知识总览MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA核心项目知识总览MOC.md:1)

### 这组挂接主要回答什么

- EA 的关键流程节点是什么
- 每个节点靠什么通过
- 哪些地方靠 Gate
- 哪些地方靠人工复核
- 哪些地方靠外部确认

### 适合 agent 的默认调用方式

当问题更像：

- “这步算完成了吗”
- “这里靠什么验收”
- “这个流程缺的是动作还是验证”

优先先调 `公司级通用流程与验证标准`，再回落到 `EA流程主链与验证标准MOC` 找具体节点。

---

## 第二组：Owner 与边界挂接

### 对应的公司级底座卡

- [公司级Owner与边界规则](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/公司级Owner与边界规则.md:1)

### 在 EA 中的主入口

- [EA Agent机制与流程交接MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA%20Agent机制与流程交接MOC.md:1)
- [EA知识域定义](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA知识域定义.md:1)

### 这组挂接主要回答什么

- 这件事谁收口
- 模块 owner 和边界 owner 谁在场
- 端到端责任有没有人接
- 哪里的边界还待定

### 适合 agent 的默认调用方式

当问题更像：

- “这件事到底谁负责”
- “为什么交接后没人接住”
- “这里是不是边界 owner 缺位”

优先先调 `公司级Owner与边界规则`，再回落到 `EA Agent机制与流程交接MOC` 找具体角色和结构。

---

## 第三组：交接与共享对象挂接

### 对应的公司级底座卡

- [公司级交接与共享对象原则](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/公司级交接与共享对象原则.md:1)

### 在 EA 中的主入口

- [EA Agent机制与流程交接MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA%20Agent机制与流程交接MOC.md:1)

### 这组挂接主要回答什么

- 交接点在哪里
- 交接对象是什么
- 是否共用同一主对象 / 主档案
- 哪些地方只是“通知下一方”，还不算正式交接

### 适合 agent 的默认调用方式

当问题更像：

- “这一步怎么从 A 交到 B”
- “为什么上下游各记一份”
- “共享对象是否裂变了”

优先先调 `公司级交接与共享对象原则`，再回落到 `EA Agent机制与流程交接MOC` 找具体交接点和共享对象。

---

## 第四组：判断决策闭环挂接

### 对应的公司级底座卡

- [公司级判断决策闭环](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/公司级判断决策闭环.md:1)

### 在 EA 中的主入口

- [EA规则空白与熔断治理MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA规则空白与熔断治理MOC.md:1)
- [Jasper经验到EA应用映射MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/Jasper经验到EA应用映射MOC.md:1)

### 这组挂接主要回答什么

- 哪些问题需要 Mark 裁定
- 哪些空白先补
- 熔断后修哪条
- 理由有没有被记录
- 后续是否回灌

### 适合 agent 的默认调用方式

当问题更像：

- “这件事为什么先做”
- “这条规则空白为什么是 P0”
- “这里的裁定有没有闭环”

优先先调 `公司级判断决策闭环`，再回落到 `EA规则空白与熔断治理MOC` 与 `Jasper经验到EA应用映射MOC`。

---

## 第五组：状态一致性与 Crosswalk 挂接

### 对应的公司级底座卡

- [公司级状态一致性与Crosswalk校验](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/公司级状态一致性与Crosswalk校验.md:1)

### 在 EA 中的主入口

- [EA流程主链与验证标准MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA流程主链与验证标准MOC.md:1)
- [Jasper经验到EA应用映射MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/Jasper经验到EA应用映射MOC.md:1)

### 这组挂接主要回答什么

- 两边是不是同一对象
- 草稿是不是被误当正式
- 上下游状态是否一致
- 差异属于正常分层还是风险

### 适合 agent 的默认调用方式

当问题更像：

- “这里到底算 confirmed 还是 pending”
- “模板为什么不能当生效”
- “两边写法不一样算不算冲突”

优先先调 `公司级状态一致性与Crosswalk校验`，再回落到 EA 的验证入口和 Jasper 映射入口。

---

## 第六组：SOP 质量与异常暴露挂接

### 对应的公司级底座卡

- [公司级SOP质量与异常暴露机制](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/公司级SOP质量与异常暴露机制.md:1)

### 在 EA 中的主入口

- [EA规则空白与熔断治理MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA规则空白与熔断治理MOC.md:1)
- [Jasper经验到EA应用映射MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/Jasper经验到EA应用映射MOC.md:1)

### 这组挂接主要回答什么

- 这条 SOP 真正在运作吗
- 异常能不能被及时看见
- Gap 是不是只补当前、不回写规则
- 执行方会不会隐藏问题

### 适合 agent 的默认调用方式

当问题更像：

- “为什么总是在结果阶段才发现”
- “这条异常为什么老复发”
- “Gap 补完后有没有真正回写 SOP”

优先先调 `公司级SOP质量与异常暴露机制`，再回落到 `EA规则空白与熔断治理MOC` 和 `Jasper经验到EA应用映射MOC`。

---

## 一个最简单的调用顺序

后续不管是人还是 agent，处理 EA 问题时，都可以优先按这套顺序走：

1. 先判断问题属于流程、边界、交接、判断、状态还是异常治理
2. 先调用对应的公司级底座卡
3. 再回落到对应的 EA 专题 MOC
4. 最后再下钻到 EA 原子 / 流程卡片 / 规则节点

这会比直接在 EA 原子海里搜要稳定得多。

---

## 对 OBagent 的直接价值

这页建成后，OBagent 处理 EA 时就不必只走“项目内检索”路径，而可以更像下面这样工作：

- 先用公司级底座做问题分类
- 再用 EA 专题页做业务落点
- 最后用 EA 原子做证据和细节补全

这会让 EA 成为第一张真正“可挂底座、可被底座统领、可给 agent 调用”的项目知识域样板。

---

## 与其他文档的关系

- [EA知识域定义](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA知识域定义.md:1) 负责：定义 EA 是什么以及为什么是首个成熟项目知识域
- [公司级治理底座应用与回挂规则](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/公司级治理底座应用与回挂规则.md:1) 负责：定义所有项目知识域如何挂到底座
- [EA核心项目知识总览MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA核心项目知识总览MOC.md:1) 负责：EA 总入口
- [EA规则空白与熔断治理MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA规则空白与熔断治理MOC.md:1) 负责：EA 风险治理入口
- [EA Agent机制与流程交接MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA%20Agent机制与流程交接MOC.md:1) 负责：EA 执行结构入口
- [EA流程主链与验证标准MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/EA流程主链与验证标准MOC.md:1) 负责：EA 流程与验证入口
- [Jasper经验到EA应用映射MOC](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/Jasper经验到EA应用映射MOC.md:1) 负责：治理经验如何映射到 EA
