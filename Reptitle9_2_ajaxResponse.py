"""
爬取豆瓣电影排行榜
"""
from urllib import request
import json
url_u = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}
url = request.Request(url_u,headers=headers)
rsp = request.urlopen(url)
data = rsp.read().decode()

print(data)
