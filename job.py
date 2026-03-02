import requests
import json
import os

# ====== 你的查询地址 ======
URL = "你的boss直聘完整查询URL"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

DATA_FILE = "jobs.json"


def load_old_jobs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_jobs(jobs):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)


def get_jobs():
    response = requests.get(URL, headers=HEADERS)
    data = response.text

    # 简单提取职位标题（根据你之前结构）
    # 如果你之前已经解析成功，可以替换为你原有解析代码
    titles = []

    import re
    results = re.findall(r'"jobName":"(.*?)"', data)

    for r in results:
        titles.append(r)

    return list(set(titles))


def main():
    old_jobs = load_old_jobs()
    new_jobs = get_jobs()

    added_jobs = list(set(new_jobs) - set(old_jobs))

    if added_jobs:
        print("DATA_CHANGED")
        print("新增岗位：")
        for job in added_jobs:
            print(job)

        save_jobs(new_jobs)
    else:
        print("NO_CHANGE")


if __name__ == "__main__":
    main()
