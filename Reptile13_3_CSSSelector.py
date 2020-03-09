from bs4 import BeautifulSoup
from urllib import request
import re

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content)

print(soup.prettify())
print("=="*12)
titles = soup.select("title")
print(titles[0])
print("=="*12)
metas = soup.select("meta[content='always']")
print(metas)
