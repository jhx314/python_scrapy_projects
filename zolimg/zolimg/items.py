# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZolimgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    images_title =scrapy.Field()
    images_url = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
