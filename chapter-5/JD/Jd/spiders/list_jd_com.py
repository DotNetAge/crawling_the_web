from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class ListJd(BasePortiaSpider):
    name = "list.jd.com"
    allowed_domains = [u'list.jd.com']
    start_urls = [
        u'https://list.jd.com/list.html?cat=1318%2C2628&page=1&delivery=1&sort=sort_rank_asc&trans=1&debug=cluster&JL=4_10_0#J_main']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'cat=1318'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[]]
