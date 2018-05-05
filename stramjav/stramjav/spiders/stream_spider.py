#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
import re
import scrapy

class StreamSpider(scrapy.Spider):
    name = "stream"
    start_urls = ["http://streamjav.net/"]

    def parse(self, response):
        # 解析图片地址
        for item in response.css("div.tn-bxitem"):
            video_src = item.css('a::attr(href)').extract_first()
            if video_src is not None:
                yield response.follow(video_src, callback=self.parse_video)

    # 解析视频地址
    def parse_video(self, response):
        iframe_str = response.css('div#embed>input::attr(value)').extract_first()
        pattern = re.compile(r'src=\"([^\"]+)\"')
        m = pattern.findall(iframe_str)
        if m[0] is not None:
            yield response.follow(m[0], callback=self.parse_video_url)

    # 解析得到mp4 url
    def parse_video_url(self, response):
        body = response.text
        pattern = re.compile(r'file:\s*\"([^\"]+)\"')
        m = pattern.findall(body)
        if m[0] is not None:
            with open('urls.text', 'a+') as f:
                f.writelines(m[0])
                self.log(m[0])
