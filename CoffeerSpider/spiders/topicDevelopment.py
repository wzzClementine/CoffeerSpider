# -*- coding: utf-8 -*-
import scrapy
from maoyanTOP100.items import TopicDevelopmentItem
from scrapy.selector import Selector
import datetime
import random
from scrapy.http import Request


class TopicDevelopmentSpider(scrapy.Spider):
    name = 'TopicDevelopment'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/weibo?q=%23%E5%92%96%E5%95%A1%23&Refer=hot_weibo&page=2']

    # parse对start_urls获取到的内容response进行处理
    def parse(self, response):
        selector = Selector(response)  # 像之前一样创建一个selector
        articles = selector.xpath('//div[@class="content"]')
        for article in articles:
            item = TopicDevelopmentItem()  # 初始化item,便于填充item容器
            content = article.xpath("p[1]")
            for con in content:
                # print("content", con.xpath("string()"))
                item["content"] = con.xpath("string()").extract_first()
            imgUrl = article.xpath("div[2]/div[1]/ul/li/img/@src").extract_first()
            if imgUrl is not None:
                item["imgUrl"] = "http:" + imgUrl
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item["topic"] = "0"
            item['user_id'] = random.randint(1, 6)
            item['time'] = str(date)
            item['type'] = "1"
            item["tpcpsg_id"] = "0"

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


