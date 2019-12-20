from urllib.error import URLError

import utils.Parsing
from utils.Utils import url_request

result_source = {}
web_url = utils.Parsing.baidu_search("蓝白社txt下载", 10)
for k in web_url:
    print("网站地址:", k)
    print(web_url[k])
    try:
        dict = url_request(web_url[k])
        if '下书网' in k:
            result = utils.Parsing.xiashu_resolve(dict)
            result_source['下书网'] = result
        else:
            result = utils.Parsing.universal_resolve(dict)
            if len(result):
                print("量：",len(result))
                result_source[k + '通用解析'] = result
    except URLError as e:
        print(k, e)
    except Exception as e:
        print("解析错误", e)
pass
print()
print("解析结果：")  # {'1':[],'2':{}}
for t in result_source:
    if isinstance(result_source[t], list):
        pass
        print("\n",t, ":")
        for item in result_source[t]:
            print(item)
    else:
        pass
        print("\n",t, ":")
        for k in result_source[t]:
            print("{}:{}".format(k,result_source[t][k]))
