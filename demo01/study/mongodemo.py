#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['scrapy']
collection = db['test-collection']

news = {
    'title': 'mongodb test',
    'time': '20180501 10:52:31',
    'url': 'sdfsdfsdf',
    'src': 'collor'
}
posts = db.posts
post_id = posts.insert_one(news).inserted_id

print post_id
