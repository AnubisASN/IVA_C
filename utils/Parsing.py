import urllib.request
import time
from lxml import etree
from selenium import webdriver
from utils.Utils import url_request
import chardet


# 资源解析类


# 百度搜索解析
# return: dic_source{}
def baidu_search(word='', pagesNum=3, sleep=2):
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
    time.sleep(sleep)
    root = etree.HTML(driver.page_source)
    source_list = root.xpath('//div[@class="result c-container "]/h3')
    dic_source = {}
    # 加载资源
    # for i in range(pagesNum):
    for i, item in enumerate(source_list):
        title = item.xpath('string(.)')
        url = item.xpath('./a/@href')[0]
        print("百度数据检索：#{}{}--{}".format(i, title, url))
        dic_source[title] = url
        print("----------------------------------------------------------")
    driver.find_element_by_class_name('n').click()
    # time.sleep(sleep)
    print("百度检索数据量：", len(dic_source))
    return dic_source




# 下书网解析
# retrun: download_source[]
def xiashu_resolve(source):
    # print(source)  # 打印网页源代码
    root = etree.HTML(source)
    source_list = root.xpath('//*[contains(text(),"下载")]')
    # 解析资源
    print('开始解析资源')
    download_id = ""
    download_url = ""
    for i, item in enumerate(source_list):
        print("匹配元素：{}--{}".format(i, item.xpath("string(.)")))
        download_id = item.xpath('./@href')
        if (len(download_id)):
            print("检索：", download_id)
            download_url = "https://www.xiashu.cc{}{}".format(download_id[0], "down")
            break
    page_source = url_request(download_url)
    root = etree.HTML(page_source)
    source_list = root.xpath("//div[@id='downlist']//*[contains(@href,'" + download_id[0] + "')]")
    download_source = []
    for i, item in enumerate(source_list):
        print("下载元素：{}--{}--{}".format(i, item.xpath("string(.)"), item.xpath("./@href")))
        download_source.append("https://www.xiashu.cc{}".format(item.xpath("./@href")[0]))
    print("下载资源解析结束，量：", len(download_source))
    return download_source
