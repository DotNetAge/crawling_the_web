# coding=utf-8

from scrapy import Spider, Request
from ..items import ProductItem
from ..product_data import product_sns  # 导入货号
import urllib


class TaobaoItemSpider(Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    base_url = 'https://s.taobao.com/search?q=%s'

    def start_requests(self):
        for sn in product_sns:
            keyword = u'匡威%s' % sn
            url = self.base_url % urllib.quote(keyword.encode('utf-8'))
            yield Request(url, self.parse, meta={'sn': sn})

    def parse(self, response):

        products = response.css('#mainsrp-itemlist .items .item')

        for product in products:
            item = ProductItem()
            item['price'] = product.css('.price>strong::text').extract_first()
            item['name'] = ''.join(product.css('div.title>a::text').extract()).strip()
            item['shop'] = ''.join(product.css(".shopname>span::text").extract()).strip()
            item['image_url'] = product.css('.pic img::attr(data-src)').extract_first().strip()
            item['deal'] = product.css('.deal-cnt::text').extract_first()
            item['location'] = product.css('.location::text').extract_first()
            item['sn'] = response.meta['sn']
            item['link'] = product.css('div.title>a::attr(href)').extract_first()
            item['free_shipping'] = product.css(".icon-service-free").extract_first() != None

            yield item
