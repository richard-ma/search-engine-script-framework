#!/usr/bin/env python
# encoding: utf-8

class SearchEngine(object):

    """Docstring for SearchEngine. """

    def __init__(self):
        """@todo: to be defined1. """
        super(SearchEngine, self).__init__()

    def search(self, keyword, pages):
        """ 搜索并保存搜索结果连接

        :keyword: 搜索关键字
        :pages: 下载搜索结果页数
        :returns: 搜索结果连接list

        """
        pass

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
