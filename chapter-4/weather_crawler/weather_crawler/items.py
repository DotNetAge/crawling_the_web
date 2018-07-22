# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item,Field

class City(Item):
    name = Field()  # 城市名
    norm = Field()  # 指标类型
    value = Field() # 值
    date = Field()  # 检测日期
