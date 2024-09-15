import requests
from bs4 import BeautifulSoup
import os

def remove_styles(html_content):
    start = html_content.find('<style>')
    while start != -1:
        end = html_content.find('</style>') + 8
        html_content = html_content[:start] + html_content[end:]
        start = html_content.find('<style>')
    return html_content

proxies = {
    "http": "http://ifwpnzcz:95i6otmb3qj9@38.154.227.167:5868",
    "https": "http://ifwpnzcz:95i6otmb3qj9@38.154.227.167:5868"
}

url = "https://vk.com/club31985831?from=search"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "Accept": "*/*"
}

req = requests.get(url, proxies=proxies, timeout=180, headers=headers)
src = req.text

cleaned_html = remove_styles(src)

with open("DMtext.html", "w") as file:
    file.write(src)
    
with open("DMtext.html") as file:
    src = file.read()    

soup = BeautifulSoup(src, "html.parser")

print()
title = soup.title
print("Посты от",title.text)
print()

i = 10

posts = soup.find_all(class_="wall_post_text")[:i]
i = 1
for item in posts:
    print("Пост", i ,"-",item.text)
    i=i+1
    print()
else:
    print("Нет объектов")
os.remove("DMtext.html")