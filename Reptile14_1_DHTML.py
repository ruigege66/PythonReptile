"""
通过webdriver操作模拟进行查找
"""
from selenium import webdriver
import time
#通过keys模拟键盘
from selenium.webdriver.common.keys import Keys
#操作哪个浏览器就对哪个浏览器建立一个实例
#自动按照环境变量查找相应的浏览器
driver = webdriver.PhantomJS(r"E:\google download\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")#这个就是浏览器的实例
#如果浏览器没有相应的环境浏览器，需要指定浏览器位置
driver.get("http://www.baidu.com")#去访问这个网站，然后获取返回的数据
#通过函数查找title标签
print("Title:{0}".format(driver.title))

