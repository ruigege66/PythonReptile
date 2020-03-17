from selenium import webdriver
from selenium.webdriver.common.keys import Keys#导入的键盘
import time
#可能需要手动添加路径
chromedriverAddress = r"C:\Users\lenovo1\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriverAddress)
#写这一行的时候报错了，可见这里配置：https://blog.csdn.net/weixin_43746433/article/details/95237254

url = "http://www.baidu.com"
driver.get(url)
text1 = driver.find_element_by_id("wrapper").text#得到这个元素的值
print(text1)
print(driver.title)
#得到页面的快照
driver.save_screenshot("index,png")

driver.find_element_by_id("kw").send_keys(u"大熊猫")#向这个id输入“大熊猫”（实际上这里的kw的id就是查找的字段）
driver.find_element_by_id("su").click()#点击操作（实际上就是上一步键入信息，下一步我们进行检索）
time.sleep(5)
driver.save_screenshot("daxiongmao.png")
#获取当前界面的cookie
print(driver.get_cookies())
#模拟输入两个按键ctrl+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#模拟ctrl + x,剪切操作
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
driver.find_element_by_id("kw").send_keys(u"航空母舰")
driver.save_screenshot("hangmu.png")
driver.find_element_by_id("su").send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot("hangmu2.png")
#清空输入框,clear
driver.find_element_by_id("kw").clear()

#关闭浏览器
driver.quit()
