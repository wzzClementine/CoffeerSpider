# -*- coding: utf-8 -*-
import scrapy
from maoyanTOP100.items import ParticipantItem
from scrapy.selector import Selector
import datetime
from scrapy.http import Request
import random


class ParticipantSpider(scrapy.Spider):
    name = 'participant'
    allowed_domains = ['coffeebug.org']
    start_urls = ['http://www.coffeebug.org/t/championship/']

    # parse对start_urls获取到的内容response进行处理
    def parse(self, response):
        item = ParticipantItem()
        for i in range(0, 100):
            user_id = random.randint(1, 6)
            activity_id = random.randint(1, 12)
            status = random.randint(0, 1)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            typeid = "2"
            item["user_id"] = user_id
            item["activity_id"] = activity_id
            item["type"] = typeid
            item["status"] = status
            item["time"] = date

            yield item

