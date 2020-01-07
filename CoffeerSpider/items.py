# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Maoyantop100Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    cover = scrapy.Field()
    imgUrl = scrapy.Field()
    time = scrapy.Field()


class TopicPassageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic_id = scrapy.Field()
    title = scrapy.Field()
    icon = scrapy.Field()
    user_id = scrapy.Field()
    date = scrapy.Field()
    cover = scrapy.Field()
    description = scrapy.Field()


class CompetitionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    cover = scrapy.Field()
    imgUrl = scrapy.Field()


class TopicDevelopmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    topic = scrapy.Field()
    tpcpsg_id = scrapy.Field()
    type = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    imgUrl = scrapy.Field()


class CommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    target_id = scrapy.Field()
    type = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()


class FavourItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    target_id = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()


class ParticipantItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    activity_id = scrapy.Field()
    time = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()


class ReplyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comment_reply_id = scrapy.Field()
    reply_type = scrapy.Field()
    target_id = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    type = scrapy.Field()
    from_userid = scrapy.Field()
    to_userid = scrapy.Field()


class CollectionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    target_id = scrapy.Field()
    status = scrapy.Field()
    time = scrapy.Field()
    type = scrapy.Field()
