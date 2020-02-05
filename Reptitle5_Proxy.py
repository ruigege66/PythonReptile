"""
使用代理访问百度首页

"""
from urllib import request,error

if __name__ =="__main__":
    url = "https://www.baidu.com"
    #设置代理地址
    proxy = {"http":"39.106.114.143:80"}
    #创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_handler)
    #安装Opener
    request.install_opener(opener)

    #现在如果访问url。那么就会使用代理服务器
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
