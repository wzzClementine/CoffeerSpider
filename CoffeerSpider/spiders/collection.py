# -*- coding: utf-8 -*-
import scrapy
from maoyanTOP100.items import CollectionItem
from scrapy.selector import Selector
import datetime
from scrapy.http import Request
import random


class FavourSpider(scrapy.Spider):
    name = 'collection'
    allowed_domains = ['coffeebug.org']
    start_urls = ['http://www.coffeebug.org/t/championship/']

    # parse对start_urls获取到的内容response进行处理
    def parse(self, response):
        item = CollectionItem()
        for i in range(0, 40):
            user_id = random.randint(1, 6)
            target_id = random.randint(1, 12)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # status = random.randint(0, 1)
            status = 1
            typeid = "3"
            item["user_id"] = user_id
            item["target_id"] = target_id
            item["type"] = typeid
            item["status"] = status
            item["time"] = date

            yield item

