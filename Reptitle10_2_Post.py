import requests
from urllib import parse
import json
url = "http://www.baidu.com/s?"
data = {
    "kw":"girl"
}
# data = parse.urlencode(data).encode("utf-8")
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}
rsp = requests.post(url,data=data,headers=headers)
print(rsp.text)
# print(rsp.json())
