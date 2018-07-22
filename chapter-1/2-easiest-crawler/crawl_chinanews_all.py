# crawl_chinanews_all.py
# !/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup
import json

res = urlopen('http://www.chinanews.com/rss/rss_2.html')
rss_page = BeautifulSoup(res.read(), "html.parser")
rss_links = set([item['href'] for item in rss_page.find_all('a')])


def crawl_feed(url):
    response = urlopen(url)
    rss = BeautifulSoup(response.read(), "lxml")
    items = []
    print "Crawling %s" % url

    for item in rss.find_all('item'):
        try:
            feed_item = {
                'title': item.title.text,
                'link': item.contents[2],
                'desc': item.description.text,
                'pub_date': u'' if item.pubdate is None else item.pubdate.text
            }
            items.append(feed_item)
        except Exception as e:
            print 'Crawling %s error.' % url
            print e.message

    return items


feed_items = []

for link in rss_links:
    feed_items += crawl_feed(link)

with open('result.json', 'a') as file:
    file.write(json.dumps(feed_items))

print 'Total crawl %s items' % len(feed_items)
