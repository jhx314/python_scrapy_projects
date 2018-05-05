#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymongo
from pymongo import MongoClient

class MongoPipline(object):
    def __init__(self):
        self.client = MongoClient()

    def process_item(self, item, spilder):
        db = self.client['scrapy']
        collection = db['qiushibaike']

        qiushibaike = {
            'username': item['username'],
            'userinfo': item['userinfo'],
            'content': item['content'],
            'src': item['src']
        }
        id = collection.insert_one(qiushibaike).inserted_id
        print id