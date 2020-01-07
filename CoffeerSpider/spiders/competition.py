# -*- coding: utf-8 -*-
import scrapy
from maoyanTOP100.items import CompetitionItem
from scrapy.selector import Selector
import datetime
from scrapy.http import Request


class CompetitionSpider(scrapy.Spider):
    name = 'competition'
    allowed_domains = ['coffeebug.org']
    start_urls = ['http://www.coffeebug.org/t/championship/']

    # parse对start_urls获取到的内容response进行处理
    def parse(self, response):
        selector = Selector(response)  # 像之前一样创建一个selector
        articles = selector.xpath('//div[@class="article-list fl clear"]/ul/li')
        for article in articles:
            item = CompetitionItem()  # 初始化item,便于填充item容器
            nextLink = article.xpath("div[1]/a/@href").extract_first()
            title = article.xpath("div[2]/h3/a/text()").extract_first()
            cover = article.xpath("div[1]/a/img/@src").extract_first()
            date = datetime.datetime.now().strftime("%Y-%m-%d")

            item['name'] = title
            item['time'] = str(date)

            if "http" in cover:
                item['cover'] = cover
            else:
                item['cover'] = "http://www.coffeebug.org" + cover

            if nextLink:
                yield scrapy.Request(url=nextLink, meta={'item': item}, callback=self.second_parse)

    def second_parse(self, response):
        item = response.meta['item']
        details = response.xpath('//div[@class="detail"]/section[2]')
        htmlType = details.xpath('p').extract()
        if len(htmlType) == 0:
            content = details.xpath('string()').extract_first()
            item["content"] = content
            imgUrl = details.xpath('img/@href').extract_first()
            item["imgUrl"] = "http://www.coffeebug.org" + imgUrl
        else:
            contents = ""
            details = details.xpath('p')
            for detail in details:
                imgUrl = detail.xpath("img/@src").extract_first()
                if imgUrl is None:
                    content = detail.xpath("string()").extract_first()
                    if content is not None or " ":
                        contents += "<p>" + content + "</p>"
                else:
                    item["imgUrl"] = "http://www.coffeebug.org" + imgUrl

            item["content"] = contents

        yield item


