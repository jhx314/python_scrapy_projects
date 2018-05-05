# -*- coding: utf-8 -*-

import scrapy
from meizitu.items import MeizituItem

class MeizituSpilder(scrapy.Spider):
    name = 'meizitu'
    start_urls = [
        'http://www.meizitu.com/'
    ]

    def parse(self, response):
        for ele in response.css('div.tags>span>a::attr(href)'):
            url = ele.extract()
            yield response.follow(url, self.parse_imgs)

    def parse_imgs(self, response):
        for ele in response.css('ul.wp-list>li.wp-item h3.tit>a::attr(href)'):
            url = ele.extract()
            yield response.follow(url, self.parse_img)

    def parse_img(self, response):
        type_title = response.css('title::text').extract_first()
        strs = type_title.split('|')
        type = strs[0].strip()
        title = strs[1].strip()

        for ele in response.css('div#picture>p>img::attr(src)'):
            item = MeizituItem()
            src = ele.extract()

            item['type'] = type
            item['title'] = title
            item['img_url'] = src
            
            yield item