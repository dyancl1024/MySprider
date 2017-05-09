# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from demo2.items import Demo2Item
import json

from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class JsonWriterPipeline(object):
    def __int__(self):
        self.file = open("item,jl",'wb')

    def process_item(self,item,spider):
        line = json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item


class Demo2Pipeline(object):
    def process_item(self, item, spider):
        with open(item["title"], 'wb') as f:
            f.write(item["link"])

        print ".................. "+ item["link"]
        return item


class MyFilesPipeline(FilesPipeline):
    def get_media_requests(self,item,info):
        for url in item["file_urls"]:
            print url
            yield scrapy.Request(url)

    def item_completed(self,results,item,info):
        file_paths = [x["path"] for ok,x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no File")
        print "...........................>>>>>"
        return item;




class MyfilesPipeline2(FilesPipeline):

    def get_media_requests(self, item, info):
        for url in item["file_urls"]:
            yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        """下载完成之后，重命名文件之类的处理，文件路径在results 里，具体results数据结构用pdb看一下就可以了"""
        file_paths = [x["path"] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no images")




