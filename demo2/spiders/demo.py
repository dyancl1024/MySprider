
import scrapy
from demo2.items import Demo2Item
from scrapy.http import Request
from scrapy.selector import Selector

demain="https://channel9.msdn.com"
class ChannelSpider(scrapy.Spider):
    name = "xx123"
    allowed_domains=[".msdn.com"]
    start_urls=[
        "https://channel9.msdn.com/Events/Ignite/Microsoft-Ignite-China-2016?sort=status&direction=desc"
    ]

    def parse(self,response):
        sale = Selector(response)
        idx=0
        for a in sale.xpath("//h3"):
            item = Demo2Item()
            item["title"] = a.xpath("a/text()").extract()[0]#.encode('utf-8')
            item["link"] = a.xpath("a/@href").extract()[0]
            fileurl = demain + item["link"]
            # print fileurl
            # print item["link"]
            # print item["title"].encode("gbk","ignore")
            # yield Request(url=fileurl,meta=item,callback=self.details_parse,dont_filter=True)

            if(idx==0):
                yield Request(url=fileurl, meta={'title':item["title"]}, callback=self.details_parse, dont_filter=True)
                print fileurl
            idx+=1


    def details_parse(self,response):
        sale = Selector(response)
        item = Demo2Item();
        item["title"] = response.meta['title']
        item["link"] = sale.xpath("//*[@id='format']/option/@value").extract()[1]
        item["file_urls"] = item["link"]
        yield item
        # print item["link"],item["title"].encode("gbk","ignore")

        # for x in filepath:
        #     p = x.xpath('option/@value').extract()[1]
        #     print p