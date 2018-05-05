#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 

# 正则表达式提取video url
# <iframe width="560" height="315" src="http://streamjav.net/embed/18976" frameborder="0" allowfullscreen></iframe>
import re

url_str = '<iframe width="560" height="315" src="http://streamjav.net/embed/18976" frameborder="0" allowfullscreen></iframe>'
pattern = re.compile(r'src=\"([^\"]+)\"')
m = pattern.findall(url_str)
print m[0]