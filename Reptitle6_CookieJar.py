from urllib import request,parse
from http import cookiejar
#创建cookiejar实例
cookie = cookiejar.CookieJar()
#生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPHandler()
#生成https管理器
https_handler = request.HTTPHandler()
#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    """
    负责初次登录
    需要输入用户名密码
    :return:
    """
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email":"1215217867@qq.com",
        "password":"481648541615485"
    }
    #把数据进行编码
    data = parse.urlencode(data)
    #创建一个请求对象
    req = request.Request(url,data=data.encode())
    #使用opener发起请求
    rep = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/965187997/profile"
    #如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html","w") as f:
        f.write(html)


if __name__ == "__main__":
    """
    执行完login之后，会得到授权之后的cookie
    我们尝试把cookie打印出来
    """
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)
    getHomePage()
