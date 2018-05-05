# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 用来处理Item数据的

class Demo01Pipeline(object):
    def process_item(self, item, spider):
        return item
