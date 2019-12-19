import utils.Parsing
from utils.Utils import url_request

web_url = utils.Parsing.baidu_search("九星毒奶")
for k in web_url:
    if ("下书网" in k):
        utils.Parsing.xiashu_resolve(url_request(web_url[k]))
