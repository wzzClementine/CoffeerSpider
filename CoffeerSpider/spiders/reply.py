# -*- coding: utf-8 -*-
import scrapy
from maoyanTOP100.items import ReplyItem
from scrapy.selector import Selector
import datetime
from scrapy.http import Request
import random


class ReplySpider(scrapy.Spider):
    name = 'reply'
    allowed_domains = ['coffeebug.org']
    start_urls = ['http://www.coffeebug.org/t/championship/']

    # parse对start_urls获取到的内容response进行处理
    def parse(self, response):
        item = ReplyItem()
        for i in range(0, 40):
            comment_reply_id = random.randint(1, 141)
            # reply_type = random.randint(0, 1)
            reply_type = 1
            from_userid = random.randint(1, 6)
            to_userid = random.randint(1, 6)
            target_id = random.randint(1, 17)
            comment = ["说的太好了吧！", "我也觉得是这样的", "好像以前听说过", "哈哈哈，太棒了！"]
            content = random.choice(comment)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            typeid = "1"
            item["comment_reply_id"] = comment_reply_id
            item["reply_type"] = reply_type
            item["from_userid"] = from_userid
            item["to_userid"] = to_userid
            item["target_id"] = target_id
            item["content"] = content
            item["type"] = typeid
            item["time"] = date

            yield item

