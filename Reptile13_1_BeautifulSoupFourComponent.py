from bs4 import BeautifulSoup
from urllib import request

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content)
#bs自动转码
content = soup.prettify()
print(content)
print("==" *12)
print(soup.head)
print("=="*12)
print(soup.link.name)
print("=="*12)
print(soup.link.attrs)
print(soup.link.attrs["type"])
print("=="*12)
print(soup.title)
print(soup.title.name)#打印标签
print(soup.title.attrs)
print(soup.title.contents)#打印内容，返回一个列表
