#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import pymongo
from pymongo import MongoClient

class MongoPipline(object):
    def __init__(self):
        self.client = MongoClient()

    def process_item(self, item, spilder):
        db = self.client['scrapy']
        collection = db['tuicool']
        # print item
        news = {
            'title': item['title'],
            'time': item['time'],
            'url': item['url'],
            'src': item['src']
        }
        post_id = collection.insert_one(news).inserted_id
        print post_id