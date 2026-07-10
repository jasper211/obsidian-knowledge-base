---
type: project_note
project: 流程架构
layer: "08_任务与跟进"
layer_tag: 任务
subdir: "AI上下文"
tags: [任务, AI]
---

## 🧭 导航
⬆️ [[08_任务与跟进]] · ⬆️ [[AI上下文]] · 🏠 [[流程架构项目MOC]]

---

# 任务 0：.env 密码清理 —— Mark 端 Claude 同步指南

> 日期: 2026-05-22
> 来源: Carrie（本地侧已完成）
> 目标执行人: Mark / Mark 端 Claude
> 优先级: P0

---

## 一、背景

EA 项目 `mga-data-platform` 模块的 `.env` 文件中，数据库密码 `Mga2026@root` 以明文形式存在，存在安全风险。Carrie 本地侧已完成清理，现需 Mark 端同步相同操作。

---

## 二、Carrie 本地已完成 ✅

| 项目包路径 | 操作 |
|---|---|
| `企业共享平台/项目空间/06_平台配置/mga-data-platform/.env` | 明文密码已 mask |
| `EA项目/06_Scripts库/06_平台配置/mga-data-platform/.env` | 明文密码已 mask |

**更新后的 `.env` 内容模板**：

```bash
# ============================================
# MGA Data Platform 数据库配置
# ============================================
# ⚠️ 安全提醒：本地 PG (47.84.6.114) 已废弃，
#    现使用远程服务器 43.98.163.46
#    本文件仅保留模板，真实凭据请勿入 git
# ============================================

MGA_DB_HOST=43.98.163.46
MGA_DB_PORT=5432
MGA_DB_NAME=mga_platform
MGA_DB_USER=root
MGA_DB_PASSWORD=__REDACTED_REQUIRES_RESET__
```

---

## 三、Mark 端需同步（Claude 协助执行）

### 步骤 1：清理 Mark 本地项目包的 `.env`

**目标文件**：
```
<Mark 的项目目录>/06_Scripts库/06_平台配置/mga-data-platform/.env
```

**操作**：
1. 备份原文件
2. 将 `MGA_DB_PASSWORD=Mga2026@root` 替换为 `MGA_DB_PASSWORD=__REDACTED_REQUIRES_RESET__`
3. 建议参照上方模板完整替换 `.env` 内容

---

### 步骤 2：检查 git 历史暴露

**操作**：
```bash
cd <Mark 的项目目录>
git log --all --oneline -S "Mga2026@root"
```

**判断**：
- 有结果（commit 中包含密码）→ 需清理 git 历史
- 无结果 / 不是 git 仓库 → 无需处理

---

## 四、同步确认

Mark 完成后请 Carrie 确认：
- [ ] Mark 端 `.env` 已清理
- [ ] git 历史检查结果（有 / 无 / 不是 git 仓库）

---

*本指南由 Carrie 于 2026-05-22 创建，供 Mark 端 Claude 协助执行。*

