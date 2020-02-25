import requests

#两种请求
url = "http://www.baidu.com/s?"
rsp = requests.get(url)
# print(rsp.text)

#使用get请求
rsp = requests.request("GET",url)
# print(rsp.text)
#拿到的结果都是一样的

"""
使用参数headers和params来研究返回结果
"""
kw = {
    "wd":"python中文文档"
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}
rsp=requests.get(url,params=kw,headers=headers)
print(rsp.text)
print("=========================")
print(rsp.content)
print("=========================")
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)
