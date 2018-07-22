# coding=utf-8


from scrapy.spiders import XMLFeedSpider
from ..items import NewsFeedItem


class ChinaNewsSpider(XMLFeedSpider):
    name = "chinanews"
    start_urls = {"http://www.chinanews.com/rss/scroll-news.xml"}

    # 这是XMLFeedSpider的两个默认属性，由于值相同所以无需要在子类内改写
    # iterator = 'iternodes'
    # itertag = 'item'

    def parse_node(self, response, node):
        item = NewsFeedItem()
        item['title'] = node.xpath('title/text()').extract_first()
        item['link'] = node.xpath('link/text()').extract_first()
        item['desc'] = node.xpath('description/text()').extract_first()
        item['pub_date'] = node.xpath('pubDate/text()').extract_first()

        yield item


