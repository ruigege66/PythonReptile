from urllib import request,parse
import chardet
"""
解析reponse
"""
if __name__ == "__main__":
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")
    #要想使用data,需要使用字典结构
    qs = {
        "wd":wd
    }
    #转换url编码
    qs = parse.urlencode(qs)#对关键字进行编码
    fullurl = url + qs#百度搜索传入的地址是基础地址加上关键字的编码形式
    print(fullurl)
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()#解码
    #使用get取值保证不会出错
    print(html)

    rsp = request.urlopen(url)
    print("URL:{0}".format(rsp.geturl()))#网页地址
    print("================")
    print("Info:{0}".format(rsp.info()))#网页头信息
    print("================")
    print("Code:{0}".format(rsp.getcode()))#请求后返回的状态码
