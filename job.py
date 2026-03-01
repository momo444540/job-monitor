import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

WEBHOOK = os.environ.get("WEBHOOK")

KEYWORDS = [
    "上海 工装 深化",
    "上海 施工图 深化",
    "上海 BIM 外包",
]

def search(keyword):
    url = f"https://www.zhipin.com/web/geek/jobs?query={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    return f"关键词：{keyword} 页面抓取成功"

def send(msg):
    data = {
        "msgtype": "text",
        "text": {"content": msg}
    }
    requests.post(WEBHOOK, json=data)

def main():
    result = []
    for k in KEYWORDS:
        result.append(search(k))
    message = "\n".join(result)
    send(message)

if __name__ == "__main__":
    main()
