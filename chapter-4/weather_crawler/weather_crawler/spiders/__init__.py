# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from ..items import City
from scrapy.spiders import CSVFeedSpider
from cities import names


class WeatherSpider(CSVFeedSpider):
    name = 'example.com'
    start_urls = ['http://www.example.com/feed.csv']

    def parse_row(response, row):
        city = City()
        for name in names:
            if row[name] != None:
                city['name'] = name
                city['norm'] = row['type']
                city['value'] = row[name]
                city['date'] = "%s-%s-%s" % (row['date'][0, 3], row['date'][4, 5], row['date'][6, 7])
                yield city
