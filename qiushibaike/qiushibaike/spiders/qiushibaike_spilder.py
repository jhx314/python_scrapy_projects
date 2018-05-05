#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy

from qiushibaike.items import QiushibaikeItem

class QiushibaikeSpilder(scrapy.Spider):
    name = 'qiushibaike'
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        for item in response.css('div.article'):
            username = item.css('div.author>a>h2::text').extract_first().strip()
            userinfo = item.css('div.author>a::attr(href)').extract_first().strip()
            content = item.css('a.contentHerf>div.content>span::text').extract_first().strip()
            src = item.css('a.contentHerf::attr(href)').extract_first().strip()

            Qiushibaike = QiushibaikeItem()
            Qiushibaike['username'] = username
            Qiushibaike['userinfo'] = userinfo if userinfo.startswith('http') else 'https://www.qiushibaike.com' + userinfo
            Qiushibaike['content'] = content
            Qiushibaike['src'] = src if src.startswith('http') else 'https://www.qiushibaike.com' + src

            yield Qiushibaike