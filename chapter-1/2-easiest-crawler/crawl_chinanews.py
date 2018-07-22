# -*- encoding: utf8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import json

response = urlopen('http://www.chinanews.com/rss/scroll-news.xml')
rss = BeautifulSoup(response.read(), "html.parser")

items = []  # 结果数据

for item in rss.find_all('item'):

    feed_item = {
        'title': item.title.text,
        'link': item.link.text,
        'desc': item.description.text,
        'pub_date': item.pubdate.text
    }

    items.append(feed_item)  # 将结果保存到JSON文件内

with open('result.json', 'wt') as file:
    file.write(json.dumps(items))
