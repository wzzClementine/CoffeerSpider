# -*- coding: utf-8 -*-
import scrapy
from maoyanTOP100.items import TopicPassageItem
from scrapy.selector import Selector
import datetime
from scrapy.http import Request


class TopicPassageSpider(scrapy.Spider):
    name = 'TopicPassage'
    allowed_domains = ['coffeebug.org']
    start_urls = ['http://www.coffeebug.org/t/roastery/']

    # parse对start_urls获取到的内容response进行处理
    def parse(self, response):
        selector = Selector(response)  # 像之前一样创建一个selector
        articles = selector.xpath('//div[@class="article-list fl clear"]/ul/li')
        for article in articles:
            item = TopicPassageItem()  # 初始化item,便于填充item容器
            title = article.xpath("div[2]/h3/a/text()").extract_first()
            cover = article.xpath("div[1]/a/img/@src").extract_first()
            description = article.xpath("div[2]/p[2]/text()").extract_first()
            print(description)
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            item["topic_id"] = "6"
            item['title'] = title
            item["icon"] = ["../../../../assets/images/cake.png"]
            item['user_id'] = '1'
            item['date'] = str(date)
            item["description"] = description

            # item['time'] = time
            # # item["topic"] = "06"
            if "http" in cover:
                item['cover'] = cover
            else:
                item['cover'] = "http://www.coffeebug.org" + cover

            yield item
            #
            # if nextLink:
            #     yield scrapy.Request(url=nextLink, meta={'item': item}, callback=self.second_parse)

    # def second_parse(self, response):
    #     item = response.meta['item']
    #     details = response.xpath('//div[@class="detail"]/section[2]')
    #     htmlType = details.xpath('p').extract()
    #     if len(htmlType) == 0:
    #         urls = []
    #         content = details.xpath('string()').extract_first()
    #         item["content"] = content
    #         imgUrls = details.xpath('img/@href').extract()
    #         for url in imgUrls:
    #             urls.append("http://www.coffeebug.org" + url)
    #             # urls.append(url)
    #         item["imgUrl"] = "&".join(urls)
    #     else:
    #         imgUrls = []
    #         contents = ""
    #         details = details.xpath('p')
    #         for detail in details:
    #             imgUrl = detail.xpath("img/@src").extract_first()
    #             if imgUrl is None:
    #                 content = detail.xpath("string()").extract_first()
    #                 if content is not None or '':
    #                     contents = contents + "&&&" + content
    #             else:
    #                 imgUrls.append("http://www.coffeebug.org" + imgUrl)
    #
    #         item["content"] = contents
    #         item["imgUrl"] = "&".join(imgUrls)
    #
    #     yield item


