import requests
import json
import os
import urllib.parse

KEYWORDS = [
    "装饰施工图深化",
    "现场协助施工",
    "竣工图绘制",
    "驻场深化"
]

DATA_FILE = "data.json"


def build_query():
    return " OR ".join(KEYWORDS)


def fetch_jobs():
    query = build_query()
    url = f"https://www.zhipin.com/web/geek/job?query={urllib.parse.quote(query)}&city=100010000"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        return [{"title": f"示例岗位：{query}", "link": url}]
    except:
        return []


def load_old_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    new_data = fetch_jobs()
    old_data = load_old_data()

    if new_data != old_data:
        save_data(new_data)
        print("DATA_CHANGED")
        for job in new_data:
            print(job["title"])
            print(job["link"])
            print("-----")
    else:
        print("NO_CHANGE")


if __name__ == "__main__":
    main()
