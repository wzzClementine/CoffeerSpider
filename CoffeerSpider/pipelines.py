# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.conf import settings


class Maoyantop100Pipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        articles = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `passages` " \
                      "(`user_id`, `title`, `content`, `cover`, `imgUrl`, `time`) " \
                      "VALUES (%s, %s, %s, %s, %s,%s)"
                self.cursor.execute(sql,
                               (int(articles["user_id"]), articles["title"], articles["content"],
                                articles["cover"],  articles["imgUrl"], articles["time"]))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class TopicPassagePipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        topicPassage = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `topicPassage` " \
                      "(`topic_id`, `title`, `icon`, `user_id`, `date`, `cover`, `description`) " \
                      "VALUES (%s, %s, %s, %s, %s,%s, %s)"
                self.cursor.execute(sql,
                               (int(topicPassage["topic_id"]), topicPassage["title"], topicPassage["icon"],
                                int(topicPassage["user_id"]), topicPassage["date"], topicPassage["cover"],
                                topicPassage["description"]))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class CompetitionPipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        competition = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `competition` " \
                      "(`name`, `content`, `imgUrl`, `time`, `cover`) " \
                      "VALUES (%s, %s, %s, %s, %s)"
                self.cursor.execute(sql,
                               (competition["name"], competition["content"], competition["imgUrl"],
                                competition["time"], competition["cover"],))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class TopicDevelopmentPipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        development = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `development` " \
                      "(`user_id`, `topic`, `tpcpsg_id`, `type`, `content`, `time`, `imgUrl`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql,
                               (int(development["user_id"]), int(development["topic"]), int(development["tpcpsg_id"]),
                                int(development["type"]), development["content"], development["time"], development["imgUrl"]))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class CommentPipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        comment = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `comment` " \
                      "(`user_id`, `target_id`, `type`, `content`, `time`) " \
                      "VALUES (%s, %s, %s, %s, %s)"
                self.cursor.execute(sql,
                               (int(comment["user_id"]), int(comment["target_id"]),
                                int(comment["type"]), comment["content"], comment["time"]))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class FavourPipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        favour = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `favour` " \
                      "(`user_id`, `target_id`, `type`, `status`) " \
                      "VALUES (%s, %s, %s, %s)"
                self.cursor.execute(sql,
                               (int(favour["user_id"]), int(favour["target_id"]),
                                int(favour["type"]), favour["status"]))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class ParticipantPipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        participant = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `participant` " \
                      "(`user_id`, `activity_id`, `time`, `type`, `status`) " \
                      "VALUES (%s, %s, %s, %s, %s)"
                self.cursor.execute(sql,
                               (int(participant["user_id"]), int(participant["activity_id"]),
                                participant["time"], int(participant["type"]), int(participant["status"])))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class ReplyPipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        reply = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `reply` " \
                      "(`comment_reply_id`, `reply_type`, `target_id`, `content`, `time`, `type`, `from_userid`, `to_userid`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql,
                               (int(reply["comment_reply_id"]), int(reply["reply_type"]), int(reply["target_id"]),
                                reply["content"], reply["time"], int(reply["type"]),
                                int(reply["from_userid"]), int(reply["to_userid"])))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item


class CollectionPipeline(object):
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host="cdb-31719yec.bj.tencentcdb.com",
                                     user='root',
                                     port=10234,
                                     password='wzz19971112!!!',
                                     db='coffee',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        collection = dict(item)
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                # sql = "INSERT INTO `articles` " \
                #       "(`pid`, `uid`, `topic`, `type`, `title`, `cover`, `content`, `time`, `imgUrl`) " \
                #       "VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
                # self.cursor.execute(sql,
                #                (int(articles["pid"]), int(articles["uid"]), int(articles["topic"]), int(articles["type"]),
                #                 articles["title"], articles["cover"], articles["content"], articles["time"],
                #                 articles["imgUrl"]))
                sql = "INSERT INTO `collection` " \
                      "(`target_id`, `user_id`, `status`, `time`, `type`) " \
                      "VALUES (%s, %s, %s, %s, %s)"
                self.cursor.execute(sql,
                               (int(collection["target_id"]), int(collection["user_id"]), int(collection["status"]),
                                collection["time"], int(collection["type"])))

            self.connection.commit()

        finally:
            # self.connection.close()
            pass

        return item