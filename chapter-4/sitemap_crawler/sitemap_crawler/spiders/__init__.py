# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spiders import SitemapSpider
from scrapy import Selector
from scrapy import Field, Item


class Place(Item):
    country = Field()
    area = Field()


class MySpider(SitemapSpider):
    name = 'example_sitemap'
    sitemap_urls = ['http://example.webscraping.com/sitemap.xml']
    sitemap_rules = [('/places/default/view/', 'parse_view')]

    def parse_view(self, response):
        sel = Selector(response)
        place = Place()
        place['area'] = sel.select("[@id='places_area__row']/[@class='w2p_fw']").extract_first()
        place['country'] = sel.select("[@id='places_iso__row']/[@class='w2p_fw']").extract_first()
        yield place
