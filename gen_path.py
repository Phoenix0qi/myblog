import os

# === 1. 结构定义 (Refined Structure) ===
structure = {
    "sports": {
        "title": "Sports & Fitness",
        # 主板块可以使用 trophy (奖杯) 或 heart (健康) - 这里代码里不直接设置主板块图标，
        # 而是设置主板块_index.md里的子卡片图标。
        "items": [
            # 冰雪运动 -> cloud (天气/雪)
            {"name": "winter_sports", "title": "Winter Sports", "icon": "cloud"},
            # 游泳 -> lifebuoy (救生圈/水上)
            {"name": "swimming", "title": "Swimming", "icon": "academic-cap"},
            # 跑步 -> bolt (闪电/速度)
            {"name": "running", "title": "Running Notes", "icon": "lightning-bolt"},
            # 健身计划 -> calendar (日程/计划)
            {"name": "workout", "title": "Workout Plan", "icon": "calendar"}
        ]
    },
    "cooking": {
        "title": "Culinary Arts",
        "items": [
            # 甜点 -> cake (蛋糕)
            {"name": "desserts", "title": "Desserts & Baking", "icon": "cake"},
            # 肉类/牛排 -> fire (煎烤/火候)
            {"name": "meats", "title": "Steaks & Red Meat", "icon": "fire"},
            # 海鲜 -> scale (称重/厨房秤 - 列表中没有鱼，这是最相关的厨房工具)
            {"name": "seafood", "title": "Seafood & Fish", "icon": "scale"},
            # 披萨 -> sun (圆形/高温)
            {"name": "pizza", "title": "Pizza Lab", "icon": "sun"},
            # 饮品 -> beaker (烧杯 - 代表调酒/咖啡实验)
            {"name": "beverages", "title": "Coffee & Wine", "icon": "beaker"}
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




# gen content 


if __name__ == "__main__":
    create_hugo_content()