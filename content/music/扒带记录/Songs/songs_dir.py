


# 目录下的 的 歌名梳理，自动新建 hugo 格式额 md 文件



#%%
## 1. 读取目录下的 .md 结尾的文件名

# 文件名格式为 f"{title} - {author}.md"
# 读取csv: songs_dir + song_list.csv
# 若没有则新建
# csv 表头包括 title; author; tags； 
# tags 为 表头中的 params.tags列表中的元素
# 若有 则读取 title; author; tags； 

# 比较 songs_dir下 与 csv读取 的区别，二者取并集写入csv，并梳理 songs_dir下 没有 需要新增的文件；并按照下面格式新建md文件；



#%%
## 2. 生成 csv 文件下歌名的 .md 文件；并自动填入hugo 文件头；
"""
    1: .md文件名为: new_songs.csv 中 title + .md
    2: 每个md的hugo文件头例子如下为:

---
title: 落日 - 东京事变
type: docs
sidebar:
  open: false
params:
  math: true # 行内公式
  tags: ["椎名林檎", "Jpop", "流行"]    
---
    其中title, params.tags 为csv 中对应key 的value;

    3: 文件内 添加 通用标题结构 内容为：
    
### 整体走向 Chord Progression

### 知识点

"""


import os
import pandas as pd
from pathlib import Path

# 配置路径
songs_dir = Path(r"content\music\扒带记录\Songs")
csv_path = songs_dir / "song_list.csv"

# --- 1. 读取/初始化 CSV 数据 ---
# 定义表头
columns = ['title', 'author', 'tags']

if csv_path.exists():
    df_csv = pd.read_csv(csv_path)
    # 确保 tags 列被正确解析为列表（如果之前存的是字符串）
    df_csv['tags'] = df_csv['tags'].apply(lambda x: eval(x) if isinstance(x, str) else x)
else:
    df_csv = pd.DataFrame(columns=columns)

# --- 2. 扫描目录下的 .md 文件 ---
md_files = [f.stem for f in songs_dir.glob("*.md")]

# 解析文件名: "落日 - 东京事变" -> title: "落日", author: "东京事变"
scanned_data = []
for name in md_files:
    if " - " in name:
        title, author = name.split(" - ", 1)
        scanned_data.append({'title': title.strip(), 'author': author.strip(), 'tags': []})

df_scanned = pd.DataFrame(scanned_data)

# --- 3. 合并数据 (取并集) ---
# 以 title 和 author 为唯一键进行合并
df_combined = pd.concat([df_csv, df_scanned]).drop_duplicates(subset=['title', 'author'], keep='first').reset_index(drop=True)

# 填充空 tags 为空列表
df_combined['tags'] = df_combined['tags'].apply(lambda x: x if isinstance(x, list) else [])

# 保存更新后的 CSV
df_combined.to_csv(csv_path, index=False)

# --- 4. 找出需要新增的 md 文件 ---
# 逻辑：在 df_combined 中但目前物理磁盘上不存在的文件
existing_md_names = [f.stem for f in songs_dir.glob("*.md")]

# 生成待创建的任务列表
to_create = df_combined[~(df_combined['title'] + " - " + df_combined['author']).isin(existing_md_names)]

# --- 5. 批量生成 .md 文件 ---
hugo_template = """---
title: {title} - {author}
type: docs
sidebar:
  open: false
params:
  math: true
  tags: {tags}
---

### 整体走向 Chord Progression

### 知识点
"""

for _, row in to_create.iterrows():
    file_name = f"{row['title']} - {row['author']}.md"
    file_path = songs_dir / file_name
    
    # 格式化 tags 为 Hugo 要求的 JSON 数组格式
    content = hugo_template.format(
        title=row['title'],
        author=row['author'],
        tags=row['tags']
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"已创建文件: {file_name}")

print("\n处理完成！")