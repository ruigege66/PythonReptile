from urllib import request,error

if __name__ == "__main__":
    url = "http://www.baidu.comfdsfdfsf"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)

    url2 = "http://www.baiu.com"
    try:
        #使用head方法伪装UA
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
        # req2 = request.Request(url2,headers=headers)
        req2 = request.Request(url2)
        req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
        rsp2 =  request.urlopen(req2)
        html2 = rsp2.read().decode()
        print(html2)
    except error.HTTPError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)
