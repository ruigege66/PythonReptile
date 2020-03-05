import re

s = r"([a-z]+)( [a-z]+)"
pattern = re.compile(s,re.I)

m = pattern.match("Hello world wide web")
#group(0)表示返回匹配成功的整个字串
s = m.group(0)
print(s)
#返回匹配成功的整个子串的跨度
a = m.span(0)
print(a)
#group(1)表示返回的第一个分组匹配成功的字串
s = m.group(1)
print(s)
#span(1)返回匹配成功的第一个子串的跨度
a = m.span(1)
print(a)
#groups()返回的是匹配的所有分组子串都输出出来，不包含整个匹配的子串
b = m.groups()
print(b)
print("===============")
string = r"\d+"
pattern = re.compile(string)
m = pattern.search("one12two34three56")#返回第一个查找到的结果
print(m.group(0))#这里的0不写也没有关系，不写就是默认为0
m = pattern.search("one12two34three56",10,40)#从字符串的第十个位置进行查找，第四十结束，这里不够四十，那就直接到字符串结束位置即可
print(m)

m = pattern.findall("one12two34three56")#以列表的形式返回所有的结果
print(m)

m = pattern.finditer("one12two34three56")
print(m)
for i in m:
    print(i)
    print(i.group())

print("=======")
string2 = u"你好，世界"
pattern = re.compile(r"[\u4e00-\u9fa5]+")
print(pattern.search("你好，世界杯").group())
