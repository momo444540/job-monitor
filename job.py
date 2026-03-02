import requests
from bs4 import BeautifulSoup

# 测试网址
url = "https://example.com"

response = requests.get(url, verify=False)

soup = BeautifulSoup(response.text, "html.parser")

print("网页标题是：")
print(soup.title.text)
