import os

# === 1. 结构定义 (Refined Structure) ===
structure = {
    "sports": {
        "title": "Sports & Fitness",
        "items": [
            # 冰雪运动 (滑雪/滑冰) - 图标用 snowflake
            {"name": "winter_sports", "title": "Winter Sports", "icon": "snowflake"},
            # 游泳 - 图标用 waves (波浪)
            {"name": "swimming", "title": "Swimming", "icon": "waves"},
            # 跑步 (保留)
            {"name": "running", "title": "Running Notes", "icon": "footprints"},
            # 健身计划 (保留)
            {"name": "workout", "title": "Workout Plan", "icon": "dumbbell"}
        ]
    },
    "cooking": {
        "title": "Culinary Arts",
        "items": [
            # 甜点 - 图标用 cake
            {"name": "desserts", "title": "Desserts & Baking", "icon": "cake"},
            # 肉类: 牛肉/红肉 - 图标用 flame (火焰/煎烤)
            {"name": "meats", "title": "Steaks & Red Meat", "icon": "flame"},
            # 肉类: 鱼/海鲜 - 图标用 fish
            {"name": "seafood", "title": "Seafood & Fish", "icon": "fish"},
            # 披萨 - 图标用 sun (形状类似披萨) 或 asterisk
            {"name": "pizza", "title": "Pizza Lab", "icon": "sun"},
            # 饮品: 咖啡与酒 - 图标用 glass-water 或 coffee
            {"name": "beverages", "title": "Coffee & Wine", "icon": "glass-water"}
        ]
    }
}

def create_hugo_content():
    base_dir = "content"  # 默认在 content 目录下创建，如果想在当前目录，改为空字符串 ""
    
    for section, data in structure.items():
        # 1. 创建主板块文件夹 (例如: content/sports)
        section_path = os.path.join(base_dir, section) if base_dir else section
        os.makedirs(section_path, exist_ok=True)
        
        # 准备主页面的 Cards 内容
        cards_content = ""
        
        for item in data["items"]:
            # 生成 Card 短代码
            cards_content += f'  {{{{< card link="./{item["name"]}" title="{item["title"]}" icon="{item["icon"]}" >}}}}\n'
            
            # 2. 创建子文件夹 (例如: content/sports/swimming)
            subfolder_path = os.path.join(section_path, item["name"])
            os.makedirs(subfolder_path, exist_ok=True)
            
            # 3. 创建子文件夹内部的 _index.md
            sub_index_path = os.path.join(subfolder_path, "_index.md")
            # 只有当文件不存在时才写入，避免覆盖你已经写好的内容
            if not os.path.exists(sub_index_path):
                with open(sub_index_path, "w", encoding="utf-8") as f:
                    sub_header = f"""---
title: {item['title']}
type: docs
---

# {item['title']}

记录关于 {item['title']} 的相关内容...
"""
                    f.write(sub_header)
                print(f"  Created sub-section: {item['name']}")
            
        # 4. 写入/更新 主板块的 _index.md (例如: content/sports/_index.md)
        main_index_path = os.path.join(section_path, "_index.md")
        with open(main_index_path, "w", encoding="utf-8") as f:
            main_header = f"""---
title: {data['title']}
type: docs
sidebar:
  open: false
---

{{{{< cards >}}}}
{cards_content}{{{{< /cards >}}}}
"""
            f.write(main_header)
            
        print(f"✅ Successfully updated section: {section}")

if __name__ == "__main__":
    create_hugo_content()