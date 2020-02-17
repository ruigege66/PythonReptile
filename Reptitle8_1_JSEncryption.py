"""
破解有道词典
"""
from urllib import request,parse

def youdao(key):
    url = "http://www.fanyi,com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i":"girl",
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"1523100789519",
        "sign":"b8a55a436686cd89873fa46514ccedbe",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typeResult":"False"
    }

    data = parse.urlencode(data).encode()
    headers = {
        "Connection": "keep - alive",
        "Content - Encoding":"gzip",
        "Content - Language": "zh - CN",
        "Content - Type": "text / html",
        "charset":"utf - 8",
        "Date": "Mon, 17 Feb 2020 15: 23:36 GMT",
        "Server":"nginx",
        "Transfer - Encoding": "chunked",
        "Vary": "Accept - Encoding"
    }
    req = request.Request(url=url,data=data,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == "__main__":
    # for i in range(10000):
    #     print(sum)
    youdao(45)
