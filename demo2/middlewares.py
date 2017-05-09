# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import  scrapy
from demo2.items import Demo2Item

class Demo2SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class MyfilesPipeline(object):

    def get_media_requests(self, item, info):
        for url in item["file_urls"]:
            yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        """下载完成之后，重命名文件之类的处理，文件路径在results 里，具体results数据结构用pdb看一下就可以了"""
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        file_paths = [x["path"] for ok, x in results if ok]
        if not file_paths:
            raise Demo2Item("Item contains no images")


class filesPipeline(object):
    def process_request(self,request,spider):
        print request.url
        print "process_request..................."+request.url[-3:]
        if request.url[-3:]=="mp4":
            return None
        else:
            return scrapy.Response("")


    def process_response(self,request, response, spider):
        print ">>>>>>>>>>>>>>> process_response"
        t = request.url[-3:]
        if t=="mp4":
            return response
        else:
            return response

    def process_exception(self,request, exception, spider):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> process_exception"
        t = request.url[-3:]
        if t=="mp4":
            return
