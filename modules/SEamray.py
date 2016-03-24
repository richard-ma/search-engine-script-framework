# -*- coding: utf-8 -*-
# amray search engine

import requests
import re
import sys
import time
from urllib import quote

from searchEngine import SearchEngine

class SEamray(SearchEngine):

    def __init__(self):
        super(SEamray, self).__init__()

        self.engineName = "amray"
        # self.url = "http://cn.bing.com/search?q=%s&first=%d" # 搜索引擎地址 %s for keyword ! %d for page
        self.url = "http://www.amray.com/directory/Auctions_,038_Shopping/Clothing_,038_Accessories/clothing__accessories%d.html"
        self.url_reg = r'<font color="green">(.*?)</font><br>' # 必须在子类设置
        #self.headers = {} # HTTP请求头，可使用父类默认值
        #self.cookies = {} # HTTP cookie，可使用父类默认值

        #self.timeout = 1 # 请求超时，超过此数值则判定服务器无响应，终止本次连接，可使用父类默认值
        self.page_count = 2 # 下载链接计数，可使用父类默认值
        self.count_per_page = 1 # 每页链接数量，可使用父类默认值

if __name__ == '__main__':
    se = SEamray()
    se.search(None, 2)
