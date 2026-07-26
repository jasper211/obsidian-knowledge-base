# _待审_GitHub发现/

GitHub开源方法论自动发现雷达（`方法论转正Agent/github_discovery.py`，每周一09:00
自动跑一次）产出的候选材料存放处。**这是AI能写入的边界**——`raw/`依然只能人工
放入资料，AI不主动抓取；本目录是`raw/`之外新增的第4层，专门给自动发现的候选
"先落地、再等人工审核"，不绕过、不修改`raw/`那条既有规则。

## 候选文件长什么样

一候选一个md文件，命名格式：`YYYY-MM-DD_owner-repo_release|readme-update|new-repo.md`。
frontmatter含`status`(pending_review/promoted/rejected)、来源链接、方向
（流程架构方法论/AI协同方法论）、LLM给出的相关性判断理由等；正文含摘要+
原文摘录，方便直接读完就能判断。

## 怎么处理一条候选

**方式一：脚本辅助（推荐，frontmatter字段不会漏填）**

```bash
cd "05_Agent库/草稿/方法论转正Agent"
# 确认收录，自动写入raw/并补全collected_at/staleness_review_date等字段
python3 promote_candidate.py <候选文件名> --promote

# 不收录
python3 promote_candidate.py <候选文件名> --reject --reason "..."
```

**方式二：纯手动**——候选文件本身就是完整可读的素材（摘要+原文摘录+链接），
直接打开复制正文另存到`raw/`下，自己填frontmatter即可，完全绕开脚本。

两种方式处理后，候选文件都会被移到`_已处理/`子目录（不删除，留痕迹）。

## 跟人工Claudian渠道的关系

行业自学习线现在有两条并行的资料发现渠道：①Jasper在Obsidian里用Claudian对话
手动摄入；②本目录代表的GitHub自动发现。两条渠道终点相同——都落到`raw/`后，
后续Karpathy摄入流程（读raw→提炼→建wiki页）完全一样，不区分资料来源。
