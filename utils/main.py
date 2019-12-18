import time
import urllib.request
import chardet
from selenium import webdriver
from lxml import etree

# 谷歌浏览器驱动
def baidu_search(word=''):
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()#这里是火狐的浏览器运行方法
    driver.get('http://www.baidu.com')
    # 选择网页元素
    element_keyword = driver.find_element_by_id('kw')
    # 输入字符
    element_keyword.send_keys(word)
    # 找到搜索按钮
    element_search_button = driver.find_element_by_id('su')
    element_search_button.submit()
    time.sleep(2)
    return driver.page_source

def test_search(word=''):
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()#这里是火狐的浏览器运行方法
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
    # 选择网页元素
    element_keysta = driver.find_element_by_id('fromStation')
    # 输入字符
    element_keysta.send_keys("SZQ")
    # 找到搜索按钮
    element_keyend = driver.find_element_by_id('toStation')
    element_keyend.send_keys('CZQ')
    time.sleep(2)
    return driver.page_source
# 网址输入返回页面资源
def main_request(url="http://www.baidu.com"):
    page = urllib.request.urlopen(url)  # 打开网页
    htmlCode = page.read()  # 获取网页源代码
    encoding = chardet.detect(htmlCode)['encoding']  # 返回网页的编码方式
    print("encoding",encoding)
    print(htmlCode.decode(encoding))  # 打印网页源代码

#页面资源解析
def page_source(source):
    print(source)  # 打印网页源代码
    root=etree.HTML(source)
    list=root.xpath("//div[@class]/h3")
    for i,item in enumerate(list):
        print("检索：#{}-{}".format(i,item.xpath('string(.)').replace("\n","").strip()))
    print()


page_source(baidu_search("蓝白社"))



