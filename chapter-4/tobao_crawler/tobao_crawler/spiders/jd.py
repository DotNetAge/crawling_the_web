# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy_splash import SplashRequest

class JdSyncSpider(scrapy.Spider):
    name = "jd-sync"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://www.jd.com/2017"
    ]

    def parse(self, response):
        logging.info(u'---------我这个是简单的直接获取京东网首页测试---------')
        special = response.xpath('//div[@id="J_top"]/div/a/h3/text()').extract_first()
        logging.info(u"find：%s" % special)
        logging.info(u'---------------success----------------')


class JDAsyncSpider(scrapy.Spider):
    name = "jd-async"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://www.jd.com/2017"
    ]

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args=splash_args)

    def parse(self, response):
        logging.info(u'----------使用splash爬取京东网首页异步加载内容-----------')
        special = response.xpath('//div[@id="J_top"]/div/a/h3/text()').extract_first()
        logging.info(u"find：%s" % special)
        logging.info(u'---------------success----------------')
