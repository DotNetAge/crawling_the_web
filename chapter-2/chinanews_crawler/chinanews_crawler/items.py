# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class NewsFeedItem(Item):
    title = Field()  # 标题
    link = Field()  # 新闻详情链接
    desc = Field()  # 新闻综述
    pub_date = Field()  # 发布日期
