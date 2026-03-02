import requests
from bs4 import BeautifulSoup
import json
import os
import urllib.parse

KEYWORDS = [
    "装饰施工图深化",
    "现场协助施工",
    "竣工图绘制",
    "驻场深化"
]

SITES = [
    "zhipin.com",
    "zhaopin.com",
    "51job.com",
    "liepin.com"
]

DATA_FILE = "data.json"


def build_query():
    keyword_part = " OR ".join(['"' + k + '"' for k in KEYWORDS])
    site_part = " OR ".join(["site:" + s for s in SITES])
    return "(" + keyword_part + ") (" + site_part + ")"


def search_jobs():
    query = build_query()
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(query)

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for item in soup.find_all("li", class_="b_algo"):
        a = item.find("a")
        if a:
            jobs.append({
                "title": a.text.strip(),
                "link": a.get("href")
            })

    return jobs


def load_old_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    new_jobs = search_jobs()
    old_jobs = load_old_data()

    added = [job for job in new_jobs if job not in old_jobs]

    if added:
        print("DATA_CHANGED")
        for job in added:
            print(job["title"])
            print(job["link"])
            print("-----")
        save_data(new_jobs)
    else:
        print("NO_CHANGE")


if __name__ == "__main__":
    main()
