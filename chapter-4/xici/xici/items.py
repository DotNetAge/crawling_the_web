# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ProxyItem(Item):
    ip = Field()              # 地址
    port = Field() # 端口
    speed = Field() # 连接速度
    connection_time = Field() # 连接时间
    ttl = Field() # 可用时长
    protocol = Field() # 连接协议
    validated = Field() # 是否有效（标志位）

