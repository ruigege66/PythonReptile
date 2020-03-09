from bs4 import BeautifulSoup
from urllib import request
import re

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content)
#bs自动转码
content = soup.prettify()
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
print("=="*12)

tags = soup.find_all(name=re.compile("meta"))#可以使用正则，返回了一个列表，找的是含有meta属性的所有标签
print(tags)
print("=="*12)
