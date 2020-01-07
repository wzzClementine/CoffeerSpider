# -*- coding: utf-8 -*-
import scrapy
from maoyanTOP100.items import CommentItem
from scrapy.selector import Selector
import datetime
from scrapy.http import Request
import random


class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['coffeebug.org']
    start_urls = ['http://www.coffeebug.org/t/championship/']

    # parse对start_urls获取到的内容response进行处理
    def parse(self, response):
        item = CommentItem()
        for i in range(0, 25):
            user_id = random.randint(1, 6)
            target_id = random.randint(109, 124)
            comment = ["说的太好了吧！", "我也觉得是这样的", "好像以前听说过", "哈哈哈，太棒了！"]
            # comment = ["我好想参加啊，可惜没时间！", "我之前参加过这个比赛，还不错", "在比赛里认识了好多大牛", "想要奖品！"]
            content = random.choice(comment)
            typeid = "2"
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item["user_id"] = user_id
            item["target_id"] = target_id
            item["content"] = content
            item["type"] = typeid
            item["time"] = date

            yield item

