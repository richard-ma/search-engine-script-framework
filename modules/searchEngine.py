#!/usr/bin/env python
# encoding: utf-8

import requests
import re

class SearchEngine(object):

    """Docstring for SearchEngine. """

    def __init__(self):
        """@todo: to be defined1. """
        super(SearchEngine, self).__init__()

        self.engineName = "" #必须在子类中设置
        # self.url = "http://cn.bing.com/search?q=%s&first=%d" # 搜索引擎地址 %s for keyword ! %d for page
        self.url = "" # 必须在子类中设置
        # self.url_reg = r'<li class="b_algo"><h2><a href="(.*?)" target="_blank"' # 必须在子类设置
        self.url_reg = r'' # 必须在子类设置
        self.headers = {} # HTTP请求头，可使用父类默认值
        self.cookies = {} # HTTP cookie，可使用父类默认值

        self.timeout = 1 # 请求超时，超过此数值则判定服务器无响应，终止本次连接，可使用父类默认值
        self.page_count = 1 # 下载链接计数，可使用父类默认值
        self.count_per_page = 10 # 每页链接数量，可使用父类默认值

    def search(self, keyword, total_page):
        """ 搜索并保存搜索结果连接

        :keyword: 搜索关键字
        :total_page: 下载搜索结果页数
        :returns: 搜索结果连接list

        """
        all_url = []
        newpage_url = []
        while 1:
            if self.page_count / self.count_per_page + 1 < int(total_page):
                url = self.url % (keyword, self.page_count)
                self.page_count += self.count_per_page # 加上每页链接数，即为下一页的其实链接编号
                try:
                    # DEBUG: 输出请求信息
                    response = requests.get(
                            url,
                            headers=self.headers,
                            cookies=self.cookies,
                            timeout=self.timeout)
                    content = response.content
                    newpage_url = self.findAllUrl(content)
                    all_url.extend(newpage_url)
                    all_url = [i for i in set(all_url)] # 去除重复地址
                except:
                    # DEBUG: 输出获取页面失败
                    continue
            else:
                #DEBUG: 输出page_count
                break;

        self.writeToFile(all_url, self.genFilename(keyword))

    def beforeSearch(self):
        """ 搜索之前要处理的事项
        :returns: @todo

        """
        pass

    def afterSearch(self):
        """ 搜索之后要处理的事项
        :returns: @todo

        """
        pass

    def genFilename(self, keyword):
        """@todo: 根据关键字生成结果文件名

        :keyword: 搜索关键字
        :returns: 文件名

        """
        # 文件名keyword_bing.urls
        return "%s_%s.urls" % (keyword, self.engineName)

    def writeToFile(self, all_url, filename):
        """@todo: 将结果保存到文件

        :all_url: 所有链接
        :filename: 文件名
        :returns: @todo

        """
        f = open(filename, 'a')
        f.writelines(['%s\n' % x for x in all_url])
        f.close()

    def findAllUrl(self, content):
        """ 筛选页面中的url链接

        :content: 页面html代码
        :returns: 页面中的链接数组

        """
        onepage_url = []
        onepage_url = re.findall(self.url_reg, content)
        return onepage_url

