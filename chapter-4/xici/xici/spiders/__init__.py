# coding=utf-8
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy import  Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ProxyItem


class XiciSpider(CrawlSpider):
    """
    西刺代理爬虫
    """
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/wt/1']  # 从第一页开始
    rules = (
        Rule(LinkExtractor(allow=('/wt/*'),),
             follow=True,
             callback='parse_items'),
    )

    def parse_items(self, response):
        selector = Selector(response)
        row_selectors = selector.xpath("//tr")
        # items = []

        for row_selector in row_selectors[1:]:
            item = ProxyItem()
            connection_time_str = row_selector.xpath('td[8]/div/@title').extract_first()
            item['ip'] = row_selector.xpath("td[2]/text()").extract_first()
            item['protocol'] = row_selector.xpath("td[6]/text()").extract_first().lower()
            item['port'] = int(row_selector.xpath("td[3]/text()").extract_first())
            item['connection_time'] = _duration_to_millisecond(connection_time_str)
            item['speed'] = _duration_to_millisecond(row_selector.xpath('td[7]/div/@title').extract_first())
            item['ttl'] = _duration_to_millisecond(row_selector.xpath("td[9]/text()").extract_first())
            item['validated'] = row_selector.xpath("td[10]/text()").extract_first()
            yield item


def _duration_to_millisecond(val):
    if val:
        if u'秒' in val:
            return int(float(val.replace(u'秒', '')) * 1000)
        if u'分钟' in val:
            return int(val.replace(u'分钟', '')) * 1000 * 60
        if u'小时' in val:
            return int(val.replace(u'小时', '')) * 1000 * 60 * 60
        if u'天' in val:
            return int(val.replace(u'天', '')) * 1000 * 60 * 60 * 24
    return 0
