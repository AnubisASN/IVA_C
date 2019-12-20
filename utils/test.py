import time
import urllib.request
import chardet
from lxml import etree
import utils.Parsing
from utils.Utils import url_request

# 爱下电子书--https://www.aixdzs.com/
# 下书网--https://www.xiashu.cc
# 00小说网：http://www.00shu.com/

url = "http://www.baidu.com/link?url=RO5I-s_omnZegEs2dHeeADu44OlUcJqRhL9oj_wiQ6a3urV2M-gmzhXlF9KRUkqV"

page_source = url_request(url)
# utils.Parsing.universal_resolve(page_source,xpath='//a[contains(text(),"下载") and @href and not(contains(@href,"game"))]')
print("\n", "0")
print("\n", "0")
dict = {'1': 'ss'}
print(list(dict.values())[0])

if 'www.' not in "download_id":
    print('true')
else:
    print("false")

url = "https://sharjah.cc/txt/xiazai159100.html//txt/xiazai74006.html"
print(url)
print(url.replace("//", "/").replace(":", ":/"))
