#!/usr/bin/env python3
"""
v2: 将流程架构项目的MD文件转为Obsidian知识图谱
关键改进：每个笔记嵌入完整原文内容，不只是索引卡
"""
import os, re, json, sys
from pathlib import Path
from collections import defaultdict

SOURCE = "/Users/zhaoqitrenda.cn/Desktop/流程架构项目_jasper"
VAULT = "/Users/zhaoqitrenda.cn/ObsidianVault"

LAYER_MAP = {
    "00_治理与元模型": {"tag": "治理", "color": "#e74c3c", "icon": "🏛️"},
    "01_原始材料-外部导入": {"tag": "原料", "color": "#f39c12", "icon": "📦"},
    "02_过程成果-工作产出": {"tag": "过程", "color": "#3498db", "icon": "⚙️"},
    "03_发布成果-交付物": {"tag": "交付", "color": "#2ecc71", "icon": "🎯"},
    "04_Skill库": {"tag": "Skill", "color": "#9b59b6", "icon": "🧩"},
    "05_Agent库": {"tag": "Agent", "color": "#1abc9c", "icon": "🤖"},
    "06_Scripts库": {"tag": "脚本", "color": "#e67e22", "icon": "💻"},
    "07_Memory": {"tag": "记忆", "color": "#34495e", "icon": "🧠"},
    "08_任务与跟进": {"tag": "任务", "color": "#e91e63", "icon": "📋"},
    "09_AI协作v2.0工作区": {"tag": "AI协作", "color": "#00bcd4", "icon": "🤝"},
}

SUBDIR_KEYWORDS = {
    "规则分析": "规则", "L3流程库": "L3流程", "映射分析": "映射",
    "校验与上下文": "校验", "岗位族设计": "岗位", "KPI穿透": "KPI",
    "价值流建模": "价值流", "价值链L1建模": "价值链", "组织重组": "组织",
    "数据库": "数据", "L4-核心交付物": "L4", "治理规范": "治理规范",
    "权威数据": "权威数据", "任务状态": "跟进", "项目规划": "规划",
    "AI上下文": "AI", "变更记录": "变更", "治理日志": "日志",
    "命名编码规范": "编码", "项目章程": "章程", "风险登记册": "风险",
    "M-01_方法论与标准": "方法论", "M-02_架构全景": "架构全景",
    "M-03_调研与原料": "调研", "M-04_项目工作区": "工作区",
    "M-05_分析与决策报告": "决策", "M-77_跨部门输入": "跨部门",
    "M-88_mark日常输出": "日常", "M-99_归档": "归档",
    "00_项目看板": "看板", "01_军事指挥对话": "指挥",
    "02_指挥执行指令": "指令", "03_执行产出": "执行",
    "04_决策日志": "决策", "05_规范文件": "规范",
    "06_数据库脚本": "DB脚本", "07_模板库": "模板",
}

def extract_yaml_and_body(content):
    """分离 YAML front matter 和正文"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].lstrip('\n')
    return "", content

def extract_title(body, filename):
    for line in body.split('\n')[:10]:
        m = re.match(r'^#\s+(.+)', line)
        if m:
            return m.group(1).strip()
    name = Path(filename).stem
    name = re.sub(r'_v\d+[\.\d]*$', '', name)
    return name

def find_wikilink_targets(body, all_basenames_set, all_titles_map):
    """从正文内容中识别可链接的笔记名，转为[[wikilink]]"""
    links_found = set()
    
    # 1. 已有的 markdown links: [text](xxx.md)
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+\.md)\)', body):
        target = Path(m.group(2)).stem
        if target in all_basenames_set:
            links_found.add(target)
    
    # 2. 编码引用如 EFA003-A, TASK-M4W10 等
    for m in re.finditer(r'\b([A-Z]{2,6}[-_]\d{2,4}[-_]?[A-Z0-9]{0,4})\b', body):
        code = m.group(1)
        if code in all_basenames_set:
            links_found.add(code)
    
    # 3. 从前置输入/引用行提取
    for line in body.split('\n'):
        for kw in ['前置输入', '参考', '来源', '溯源']:
            if kw in line:
                # 提取可能文件名
                for m2 in re.finditer(r'[\w\u4e00-\u9fff]+[\w\-_]*', line):
                    candidate = m2.group()
                    if candidate in all_basenames_set and len(candidate) > 5:
                        links_found.add(candidate)
    
    return links_found

def add_wikilinks_to_body(body, link_targets):
    """在正文中将匹配文本转为[[wikilink]]"""
    modified = body
    for target in link_targets:
        # 只替换第一次出现的纯文本（不替换已有的[[xxx]]或代码块内的）
        pattern = r'(?<!\[\[)(' + re.escape(target) + r')(?!\]\])'
        # 限制：只替换标题和正文前20行中的出现
        lines = modified.split('\n')
        for i, line in enumerate(lines[:30]):
            if line.startswith('```') or line.startswith('|'):
                continue
            if target in line and f'[[{target}' not in line:
                lines[i] = re.sub(pattern, f'[[{target}]]', line, count=1)
                break
        modified = '\n'.join(lines)
    return modified

def build_graph():
    print("📁 扫描项目文件...")
    md_files = []
    for root, dirs, fnames in os.walk(SOURCE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '.stfolder']
        for f in fnames:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))
    print(f"   找到 {len(md_files)} 个MD文件")

    # 第一遍：收集所有文件名和元数据
    print("📋 第一遍扫描：收集元数据...")
    file_meta = {}
    by_layer = defaultdict(list)
    by_subdir = defaultdict(list)
    all_basenames_set = set()
    
    for fpath in md_files:
        rel = os.path.relpath(fpath, SOURCE)
        parts = rel.split('/')
        layer = parts[0]
        subdir = parts[1] if len(parts) > 1 else ""
        basename = Path(fpath).stem
        all_basenames_set.add(basename)
        
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except:
            continue
        
        yaml_fm, body = extract_yaml_and_body(content)
        title = extract_title(body, os.path.basename(fpath))
        
        meta = {
            "path": fpath, "rel_path": rel, "basename": basename,
            "title": title, "layer": layer, "subdir": subdir,
            "yaml_fm": yaml_fm, "body": body,
            "layer_info": LAYER_MAP.get(layer, {"tag": "其他", "icon": "📄"}),
            "subdir_tag": SUBDIR_KEYWORDS.get(subdir, subdir),
        }
        file_meta[rel] = meta
        by_layer[layer].append(meta)
        if subdir:
            by_subdir[f"{layer}/{subdir}"].append(meta)

    # 第二遍：生成带完整内容的笔记
    print("✍️ 第二遍：生成完整内容笔记（嵌入原文）...")
    
    proj_dir = os.path.join(VAULT, "项目-流程架构")
    # 清理旧文件
    os.system(f'rm -rf "{proj_dir}"')
    os.makedirs(proj_dir, exist_ok=True)
    
    count = 0
    for rel, meta in file_meta.items():
        layer_info = meta["layer_info"]
        
        # 找到该笔记可链接的目标
        link_targets = find_wikilink_targets(
            meta["body"], all_basenames_set, {}
        )
        # 最多保留8个
        link_targets = list(link_targets)[:8]
        
        # 在正文中添加wikilink
        enhanced_body = add_wikilinks_to_body(meta["body"], link_targets)
        
        # 构建YAML
        tags = [layer_info["tag"]]
        if meta["subdir_tag"] and meta["subdir_tag"] != meta["subdir"]:
            tags.append(meta["subdir_tag"])
        
        # 构建导航区
        nav = []
        nav.append(f"⬆️ [[{meta['layer']}]]")
        if meta['subdir']:
            nav.append(f"⬆️ [[{meta['subdir']}]]")
        nav.append(f"🏠 [[流程架构项目MOC]]")
        
        # 关联笔记列表
        related_section = ""
        if link_targets:
            related_section = "\n## 🔗 关联笔记\n" + "\n".join(
                f"- [[{t}]]" for t in link_targets
            ) + "\n"
        
        # 组装完整笔记
        # 如果原文已有YAML，合并；否则新建
        if meta["yaml_fm"]:
            new_yaml = f"""---
{meta['yaml_fm']}
graph_layer: "{meta['layer']}"
graph_layer_tag: {layer_info['tag']}
graph_subdir: "{meta['subdir']}"
graph_tags: [{', '.join(tags)}]
---"""
        else:
            new_yaml = f"""---
type: project_note
project: 流程架构
layer: "{meta['layer']}"
layer_tag: {layer_info['tag']}
subdir: "{meta['subdir']}"
tags: [{', '.join(tags)}]
---"""
        
        nav_section = "## 🧭 导航\n" + " · ".join(nav) + "\n"
        
        full_note = f"""{new_yaml}

{nav_section}
{related_section}
---

{enhanced_body}
"""
        
        # 写入（保持相同目录结构）
        out_path = os.path.join(proj_dir, rel)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        
        # 避免文件名与目录同名
        if os.path.isdir(out_path):
            out_path = out_path.replace('.md', '_note.md')
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_note)
        count += 1

    print(f"   生成 {count} 个完整内容笔记")

    # ============ 生成 MOC 导航页 ============
    print("🗺️ 生成MOC导航页...")
    moc_dir = os.path.join(VAULT, "MOC")
    os.makedirs(moc_dir, exist_ok=True)
    
    # 总入口
    moc = "---\ntype: moc\nproject: 流程架构\ntags: [MOC]\n---\n\n"
    moc += "# 🏗️ 流程架构项目 — 知识图谱\n\n"
    
    for layer, metas in sorted(by_layer.items()):
        info = LAYER_MAP.get(layer, {"tag": "其他", "icon": "📄"})
        moc += f"\n## {info['icon']} [[{layer}]] · {info['tag']} · {len(metas)}篇\n\n"
        subdirs = set(m["subdir"] for m in metas if m["subdir"])
        for sd in sorted(subdirs):
            sd_count = len(by_subdir.get(f"{layer}/{sd}", []))
            moc += f"- [[{sd}]] ({sd_count}篇)\n"
    
    with open(os.path.join(moc_dir, "流程架构项目MOC.md"), 'w', encoding='utf-8') as f:
        f.write(moc)
    
    # 层级 MOC
    for layer, metas in sorted(by_layer.items()):
        info = LAYER_MAP.get(layer, {"tag": "其他", "icon": "📄"})
        lmoc = f"---\ntype: moc\nlayer: {layer}\ntags: [MOC, {info['tag']}]\n---\n\n"
        lmoc += f"# {info['icon']} {layer}\n\n"
        lmoc += "🏠 [[流程架构项目MOC]]\n\n"
        
        by_sd = defaultdict(list)
        for m in metas:
            by_sd[m["subdir"] or "_根"].append(m)
        
        for sd, sd_metas in sorted(by_sd.items()):
            if sd != "_根":
                lmoc += f"\n## [[{sd}]]\n\n"
            for m in sorted(sd_metas, key=lambda x: x["title"]):
                lmoc += f"- [[{m['basename']}]]\n"
        
        out = os.path.join(proj_dir, layer, f"{layer}.md")
        with open(out, 'w', encoding='utf-8') as f:
            f.write(lmoc)
    
    # 子目录 MOC
    for sd_key, metas in sorted(by_subdir.items()):
        sd = metas[0]["subdir"]
        layer = metas[0]["layer"]
        info = LAYER_MAP.get(layer, {"tag": "其他", "icon": "📄"})
        sdmoc = f"---\ntype: moc\nlayer: {layer}\nsubdir: {sd}\ntags: [MOC]\n---\n\n"
        sdmoc += f"# {sd}\n\n"
        sdmoc += f"⬆️ [[{layer}]] · 🏠 [[流程架构项目MOC]]\n\n"
        
        for m in sorted(metas, key=lambda x: x["title"]):
            sdmoc += f"- [[{m['basename']}]]\n"
        
        out = os.path.join(proj_dir, sd_key, f"{sd}.md")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(sdmoc)

    # 图谱着色配置
    print("🎨 配置图谱分组...")
    graph_config = {"collapse-filter": True, "groups": []}
    for layer, info in LAYER_MAP.items():
        r = int(info["color"][1:3], 16)/255
        g = int(info["color"][3:5], 16)/255
        b = int(info["color"][5:7], 16)/255
        graph_config["groups"].append({
            "query": f"\"{layer}\"",
            "color": {"a": 1, "r": r, "g": g, "b": b}
        })
    
    with open(os.path.join(VAULT, ".obsidian", "graph.json"), 'w', encoding='utf-8') as f:
        json.dump(graph_config, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 完成！")
    print(f"   完整内容笔记: {count}")
    print(f"   层级MOC: {len(by_layer)}")
    print(f"   子目录MOC: {len(by_subdir)}")
    print(f"   总入口: MOC/流程架构项目MOC.md")
    print(f"\n📊 现在点击图谱节点会显示完整内容了！")

if __name__ == "__main__":
    build_graph()
