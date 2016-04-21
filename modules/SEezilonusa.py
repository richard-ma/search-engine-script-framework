# -*- coding: utf-8 -*-
# ezilon search engine

import requests
import re
import sys
import time
from urllib import quote

from searchEngine import SearchEngine

class SEezilonusa(SearchEngine):

    def __init__(self):
        super(SEezilonusa, self).__init__()

        self.engineName = "ezilon-usa"
        # self.url = "http://cn.ezilon.com/search?q=%s&first=%d" # 搜索引擎地址 %s for keyword ! %d for page
        self.url = "http://find.ezilon.com/search.php?q=%s&start=%d&t=&v=usa&f="
        self.url_reg = r'.</span>\s<a href="(.*?)">' # 必须在子类设置
        #self.headers = {} # HTTP请求头，可使用父类默认值
        #self.cookies = {} # HTTP cookie，可使用父类默认值

        self.timeout = 2 # 请求超时，超过此数值则判定服务器无响应，终止本次连接，可使用父类默认值
        self.page_count = 0 # 下载链接计数，可使用父类默认值
        self.count_per_page = 15 # 每页链接数量，可使用父类默认值

    def preProcess(self, keyword):
        return keyword.replace(' ', '+')

if __name__ == '__main__':
    se = SEezilonusa()
    se.search('test', 2)
