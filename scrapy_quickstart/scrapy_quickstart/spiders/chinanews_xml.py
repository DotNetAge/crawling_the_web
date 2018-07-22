# coding:utf-8

from scrapy.spiders import XMLFeedSpider
from ..items import FeedItem
from os import path


class ChinaNewsXmlFeedSpider(XMLFeedSpider):
	name = "chinanews_xml"
	start_urls = { "http://www.chinanews.com/rss/scroll-news.xml" }

	def parse_node(response, selector):
		