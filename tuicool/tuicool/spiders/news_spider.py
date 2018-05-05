# -*- coding: utf-8 -*-

import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from tuicool.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ['https://www.tuicool.com/']

    def parse(self, response):
        for item in response.css('div.aricle_item_info'):
        #item = response.css('div.aricle_item_info')[0]
            title = item.css('a::attr(title)').extract_first().strip()
            src = item.css('div.tip>span::text').extract()[0].strip()
            time = item.css('div.tip>span::text').extract()[2].strip()
            url = item.css('a::attr(href)').extract_first().strip()

            news = NewsItem()
            news['title'] = str(title)
            news['src'] = src.encode('utf-8')
            news['time'] = time.encode('utf-8')
            news['url'] = url if url.startswith('http') else response.url + url #python 不支持三元运算

            yield news