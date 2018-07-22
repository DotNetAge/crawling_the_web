# -*- coding: utf-8 -*-
import scrapy


class ChinanewsSpider(scrapy.Spider):
    name = "chinanews"
    allowed_domains = ["chinanews.com/rss"]
    start_urls = (
        'http://www.chinanews.com/rss/',
    )

    def parse(self, response):
        pass
