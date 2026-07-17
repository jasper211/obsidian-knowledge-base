#!/usr/bin/env python3
"""
将流程架构项目_jasper的MD文件转换为Obsidian知识图谱结构
策略：不移动原文件，在ObsidianVault中创建索引笔记+wikilink引用原文件
"""
import os, re, json, glob
from pathlib import Path
from collections import defaultdict

SOURCE = "/Users/zhaoqitrenda.cn/Desktop/流程架构项目_jasper"
VAULT = "/Users/zhaoqitrenda.cn/ObsidianVault"

# 项目层级 → 标签颜色映射
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

# 子目录 → 主题标签
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

def extract_yaml_frontmatter(content):
    """提取现有YAML front matter"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), content[len(parts[0])+len(parts[1])+4:]
    return "", content

def extract_title(content, filename):
    """从内容或文件名提取标题"""
    # 先看YAML后的第一个H1
    for line in content.split('\n')[:10]:
        if line.startswith('# ') and not line.startswith('# #'):
            return line[2:].strip()
    # 用文件名
    name = Path(filename).stem
    # 去掉版本号后缀
    name = re.sub(r'_v\d+[\.\d]*$', '', name)
    return name

def extract_references(content):
    """从内容中提取已有的文件引用关系"""
    refs = set()
    # 匹配 markdown link [text](path) 和纯文件名引用
    patterns = [
        r'\[([^\]]+)\]\(([^)]+\.md)\)',      # [text](path.md)
        r'(?:引用|参考|来源|输入|前置)[：:]\s*(.+)',  # 引用：xxx
        r'[-*]\s*\[?\[?([A-Z]{2,}\d{3}[^,\|\]\[]+)',  # EFA003-xxx 编码引用
    ]
    for line in content.split('\n'):
        for pat in patterns:
            m = re.search(pat, line)
            if m:
                ref = m.group(m.lastindex).strip()
                if len(ref) > 3 and len(ref) < 80:
                    refs.add(ref)
    return refs

def sanitize_note_name(filepath, source_root):
    """将文件路径转为Obsidian笔记名（唯一标识）"""
    rel = os.path.relpath(filepath, source_root)
    # 用相对路径去掉.md后缀作为笔记名
    name = rel.replace('.md', '').replace('/', '／').replace('\\', '／')
    return name

def find_md_files(source):
    """扫描所有MD文件"""
    files = []
    for root, dirs, fnames in os.walk(source):
        # 跳过隐藏和特殊目录
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '.stfolder']
        for f in fnames:
            if f.endswith('.md'):
                files.append(os.path.join(root, f))
    return files

def get_layer_and_subdir(rel_path):
    """从相对路径提取层级和子目录"""
    parts = rel_path.split('/')
    layer = parts[0] if parts else ""
    subdir = parts[1] if len(parts) > 1 else ""
    return layer, subdir

def build_graph():
    """主流程：构建知识图谱"""
    print("📁 扫描项目文件...")
    md_files = find_md_files(SOURCE)
    print(f"   找到 {len(md_files)} 个MD文件")
    
    # 按层级分类
    by_layer = defaultdict(list)
    by_subdir = defaultdict(list)
    file_meta = {}  # note_name -> meta dict
    
    print("📋 解析文件元数据...")
    for fpath in md_files:
        rel = os.path.relpath(fpath, SOURCE)
        layer, subdir = get_layer_and_subdir(rel)
        note_name = sanitize_note_name(fpath, SOURCE)
        
        # 读取内容
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue
        
        yaml_fm, body = extract_yaml_frontmatter(content)
        title = extract_title(body, os.path.basename(fpath))
        refs = extract_references(body)
        
        layer_info = LAYER_MAP.get(layer, {"tag": "其他", "color": "#95a5a6", "icon": "📄"})
        subdir_tag = SUBDIR_KEYWORDS.get(subdir, subdir)
        
        meta = {
            "path": fpath,
            "rel_path": rel,
            "note_name": note_name,
            "title": title,
            "layer": layer,
            "layer_tag": layer_info["tag"],
            "layer_icon": layer_info["icon"],
            "subdir": subdir,
            "subdir_tag": subdir_tag,
            "yaml_fm": yaml_fm,
            "refs": refs,
            "filename": os.path.basename(fpath),
        }
        
        by_layer[layer].append(meta)
        if subdir:
            by_subdir[f"{layer}/{subdir}"].append(meta)
        file_meta[note_name] = meta
    
    # 构建引用名 → note_name 映射（用于匹配wikilink）
    filename_to_note = {}
    for nm, m in file_meta.items():
        filename_to_note[m["filename"]] = nm
        filename_to_note[m["filename"].replace('.md', '')] = nm
    
    # ============ 创建输出目录 ============
    proj_dir = os.path.join(VAULT, "项目-流程架构")
    for layer in by_layer:
        os.makedirs(os.path.join(proj_dir, layer), exist_ok=True)
        for sd in by_subdir:
            if sd.startswith(layer + "/"):
                os.makedirs(os.path.join(proj_dir, sd), exist_ok=True)
    os.makedirs(os.path.join(VAULT, "MOC"), exist_ok=True)
    
    # ============ 生成索引笔记 ============
    print("✍️ 生成索引笔记...")
    
    # 建立文件名匹配字典（用于将refs转为wikilink）
    all_basenames = {m["filename"].replace('.md', ''): nm for nm, m in file_meta.items()}
    all_titles = {}
    for nm, m in file_meta.items():
        all_titles[m["title"]] = nm
    
    count = 0
    for note_name, meta in file_meta.items():
        # 推断 wikilink 引用
        wikilinks = []
        for ref in meta["refs"]:
            ref_clean = ref.strip().strip('[]').split('|')[0]
            # 尝试匹配已有笔记
            if ref_clean in all_basenames:
                wikilinks.append(all_basenames[ref_clean])
            elif ref_clean in all_titles:
                wikilinks.append(all_titles[ref_clean])
            else:
                # 保留为原始文本引用
                wikilinks.append(ref_clean)
        
        # 去重
        wikilinks = list(dict.fromkeys(wikilinks))[:10]  # 最多10个引用
        
        # 生成索引笔记内容
        layer_info = LAYER_MAP.get(meta["layer"], {"tag": "其他", "color": "#95a5a6", "icon": "📄"})
        
        # 构建YAML
        tags = [layer_info["tag"]]
        if meta["subdir_tag"] and meta["subdir_tag"] != meta["subdir"]:
            tags.append(meta["subdir_tag"])
        
        yaml_block = f"""---
type: project_note
project: 流程架构
layer: "{meta['layer']}"
layer_tag: {layer_info['tag']}
subdir: "{meta['subdir']}"
tags: [{', '.join(tags)}]
source: "{meta['rel_path']}'
---"""
        
        # wikilink 段
        links_section = ""
        if wikilinks:
            links_section = "\n## 关联引用\n" + "\n".join(f"- [[{wl}]]" for wl in wikilinks) + "\n"
        
        # 层级导航
        nav_links = []
        nav_links.append(f"- ⬆️ [[{meta['layer']}]]")
        if meta['subdir']:
            nav_links.append(f"- ⬆️ [[{meta['layer']}／{meta['subdir']}]]")
        
        nav_section = "## 导航\n" + "\n".join(nav_links) + "\n"
        
        note_content = f"""{yaml_block}

# {layer_info['icon']} {meta['title']}

> 📂 源文件：`{meta['rel_path']}`

{nav_section}
{links_section}
---
*此笔记为索引卡，原文见源文件路径*
"""
        
        # 写入（跳过与目录同名的文件）
        out_path = os.path.join(proj_dir, meta["rel_path"])
        if os.path.isdir(out_path):
            out_path = out_path.replace(".md", "_note.md")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(note_content)
        count += 1
    
    print(f"   生成 {count} 个索引笔记")
    
    # ============ 生成层级 MOC ============
    print("🗺️ 生成MOC导航页...")
    
    # 总入口 MOC
    moc_content = "---\ntype: moc\nproject: 流程架构\ntags: [MOC, 流程架构]\n---\n\n"
    moc_content += "# 🏗️ 流程架构项目 — 知识图谱入口\n\n"
    
    for layer, metas in sorted(by_layer.items()):
        info = LAYER_MAP.get(layer, {"tag": "其他", "icon": "📄"})
        moc_content += f"\n## {info['icon']} [[{layer}]] ({info['tag']} · {len(metas)}篇)\n\n"
        # 列出子目录
        subdirs_in_layer = set()
        for m in metas:
            if m["subdir"]:
                subdirs_in_layer.add(m["subdir"])
        for sd in sorted(subdirs_in_layer):
            sd_key = f"{layer}/{sd}"
            sd_count = len(by_subdir.get(sd_key, []))
            moc_content += f"- [[{layer}／{sd}]] ({sd_count}篇)\n"
    
    with open(os.path.join(VAULT, "MOC", "流程架构项目MOC.md"), 'w', encoding='utf-8') as f:
        f.write(moc_content)
    
    # 每个层级 MOC
    for layer, metas in sorted(by_layer.items()):
        info = LAYER_MAP.get(layer, {"tag": "其他", "icon": "📄"})
        layer_moc = f"---\ntype: moc\nproject: 流程架构\nlayer: {layer}\ntags: [MOC, {info['tag']}]\n---\n\n"
        layer_moc += f"# {info['icon']} {layer}\n\n"
        layer_moc += f"> ⬆️ [[流程架构项目MOC]]\n\n"
        
        # 按子目录分组
        by_sd = defaultdict(list)
        for m in metas:
            by_sd[m["subdir"] or "_根目录"].append(m)
        
        for sd, sd_metas in sorted(by_sd.items()):
            if sd != "_根目录":
                layer_moc += f"\n## [[{layer}／{sd}]]\n\n"
            for m in sorted(sd_metas, key=lambda x: x["title"]):
                layer_moc += f"- [[{m['note_name']}]] — {m['title']}\n"
        
        out = os.path.join(proj_dir, layer, f"{layer}.md")
        with open(out, 'w', encoding='utf-8') as f:
            f.write(layer_moc)
    
    # 每个子目录 MOC
    for sd_key, metas in sorted(by_subdir.items()):
        sd_tag = SUBDIR_KEYWORDS.get(metas[0]["subdir"], metas[0]["subdir"])
        sd_moc = f"---\ntype: moc\nproject: 流程架构\nlayer: {metas[0]['layer']}\nsubdir: {metas[0]['subdir']}\ntags: [MOC, {sd_tag}]\n---\n\n"
        sd_moc += f"# {metas[0]['subdir']}\n\n"
        sd_moc += f"> ⬆️ [[{metas[0]['layer']}]] · ⬆️ [[流程架构项目MOC]]\n\n"
        
        for m in sorted(metas, key=lambda x: x["title"]):
            sd_moc += f"- [[{m['note_name']}]] — {m['title']}\n"
        
        out = os.path.join(proj_dir, sd_key, f"{metas[0]['subdir']}.md")
        with open(out, 'w', encoding='utf-8') as f:
            f.write(sd_moc)
    
    # ============ 生成图谱分组配置 ============
    print("🎨 生成图谱分组配置...")
    graph_groups = []
    for layer, info in LAYER_MAP.items():
        graph_groups.append({
            "query": f"layer_tag:{info['tag']}",
            "color": info["color"]
        })
    
    # 写入Obsidian图谱配置
    obsidian_dir = os.path.join(VAULT, ".obsidian")
    os.makedirs(obsidian_dir, exist_ok=True)
    
    graph_config = {"collapse-filter": True, "groups": []}
    for layer, info in LAYER_MAP.items():
        graph_config["groups"].append({
            "query": f"\"{layer}\"",
            "color": {"a": 1, "r": int(info["color"][1:3], 16)/255, "g": int(info["color"][3:5], 16)/255, "b": int(info["color"][5:7], 16)/255}
        })
    
    with open(os.path.join(obsidian_dir, "graph.json"), 'w', encoding='utf-8') as f:
        json.dump(graph_config, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 完成！统计：")
    print(f"   索引笔记: {count}")
    print(f"   层级MOC: {len(by_layer)}")
    print(f"   子目录MOC: {len(by_subdir)}")
    print(f"   总入口: MOC/流程架构项目MOC.md")
    print(f"\n📊 在Obsidian中打开图谱查看即可！")

if __name__ == "__main__":
    build_graph()
