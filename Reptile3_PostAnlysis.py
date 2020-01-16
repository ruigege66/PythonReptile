"""

"""
from urllib import request,parse
#负责处理json格式的模块
import json
"""
大致流程：
（1）利用data构造内容，然后urlopen打开
（2）返回一个json格式的结果
（3）结果就应该是girl的释义
"""
baseurl = "https://fanyi.baidu.com/sug"

#存放迎来模拟form的数据一定是dict格式
data = {
    #girl是翻译输入的英文内容，应该是由用户输入，此处使用的是硬编码
    "kw":"girl"

}
#需要使用parse模块对data进行编码
data = parse.urlencode(data).encode("utf-8")
#我们需要构造一个请求头，请求头应该至少包含传入的数据的长度
#request要求传入的请求头是一个dict格式

headers = {
    #因为使用了post,至少应该包含content-length字段
    "Content-length":len(data)

}
#构造一个Request的实例,就是借用这个类，来把能够传入的头信息进行封装扩展
req = request.Request(url=baseurl,data=data,headers=headers)

#有了headers,data,url就可以尝试发出请求了
rsp = request.urlopen(req)#,headers=headers
json_data = rsp.read().decode()
print(json_data)

#把json字符串转化为字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data["data"]:
    print(item["k"],"--",item["v"])
