import
 csv
import
 re

def classify_url(url):
    """根据 URL 特征返回分类标签"""
    # 域名关键词匹配
    domain_patterns 
= {
        "代码平台": r"github\.com|gitlab\.com",
        "技术博客": r"towardsdatascience\.com|medium\.com|掘金\.com",
        "视频平台": r"youtube\.com|bilibili\.com|腾讯视频\.com",
        "新闻网站": r"nytimes\.com|人民日报\.com|bbc\.com"
    }
    
    for label, pattern in domain_patterns.items():
        if re.search(pattern, url, re.IGNORECASE):
            return
 label
    return "未分类"

# 读取并处理 CSV
with open("urls.csv", "r", encoding="utf-8") as f:
    reader 
= csv.DictReader(f)
    rows 
= list(reader)

# 为未分类的 URL 添加自动标签
for row in rows:
    if not row["auto_label"]:  # 只处理未标记的 URL
        row
["auto_label"] = classify_url(row["url"])

# 写回 CSV
with open("urls.csv", "w", encoding="utf-8", newline="") as f:
    writer 
= csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer
.writeheader()
    writer
.writerows(rows)
