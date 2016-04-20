# -*- coding: utf-8 -*-
# bing search engine

import requests
import re
import sys
import time
from urllib import quote

from searchEngine import SearchEngine

class SEgalaxy(SearchEngine):

    def __init__(self):
        super(SEgalaxy, self).__init__()

        self.engineName = "galaxy"
        # self.url = "http://cn.bing.com/search?q=%s&first=%d" # 搜索引擎地址 %s for keyword ! %d for page
        self.url = "http://www.galaxy.com/search?q=%s&inc=%d"
        self.url_reg = r'<div class="url">(.*?)</div>' # 必须在子类设置
        #self.headers = {} # HTTP请求头，可使用父类默认值
        #self.cookies = {} # HTTP cookie，可使用父类默认值

        #self.timeout = 1 # 请求超时，超过此数值则判定服务器无响应，终止本次连接，可使用父类默认值
        self.page_count = 0 # 下载链接计数，可使用父类默认值
        self.count_per_page = 25 # 每页链接数量，可使用父类默认值

    def preProcess(self, keyword):
        return keyword.replace(' ', '+')

if __name__ == '__main__':
    se = SEgalaxy()
    se.search('test', 2)
