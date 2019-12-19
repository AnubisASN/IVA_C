import urllib
import chardet
import time
import urllib.request

import chardet
from selenium import webdriver


#网络地址返回页面源码
def url_request(url="http://www.baidu.com"):
    page = urllib.request.urlopen(url)  # 打开网页
    htmlCode = page.read()  # 获取网页源代码
    encoding = chardet.detect(htmlCode)['encoding']  # 返回网页的编码方式
    print("encoding:", encoding)
    if encoding==None:
        return htmlCode
    else:
        return htmlCode.decode(encoding)

#网络地址浏览器驱动返回页面源码
def browser_request(url, sleep=3):
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()#这里是火狐的浏览器运行方法
    driver.get(url)
    time.sleep(sleep)
    return driver.page_source