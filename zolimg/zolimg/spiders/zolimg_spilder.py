# -*- coding: utf-8 -*-

import scrapy
from zolimg.items import ZolimgItem

class ZolImgSpilder(scrapy.Spider):
    name = 'zolimg'
    start_urls = ['http://desk.zol.com.cn//bizhi/559_5439_1.html']

    def parse(self, response):
        for ele in response.css('dd#tagfbl>a::attr(href)'):
            url = 'http://desk.zol.com.cn/' + ele.extract()
            yield response.follow(url, self.parseimg)
        
        for ele in response.css('a'):
            url = ele.xpath('@href').extract_first()
            if url is not None and 'bizhi' in url:
                start_url = 'http://desk.zol.com.cn/' + url
                yield response.follow(start_url, self.parse)

    def parseimg(self, response):
        imgurl = response.css('img::attr(src)').extract_first()
        if imgurl is not None:
            print imgurl
            item = ZolimgItem()
            item['images_url'] = imgurl
            yield item