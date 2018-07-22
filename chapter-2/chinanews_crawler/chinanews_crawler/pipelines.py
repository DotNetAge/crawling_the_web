# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
from bs4 import BeautifulSoup

class BlockGamePipeline:
    def process_item(self, item, spider):
        key = "游戏"
        if key in (item['title']).encode('utf-8'):
            raise DropItem()
        return item


class DuplicatesPipeline:
    def __init__(self):
        self.fingerprints = set()

    def process_item(self, item, spider):
        if self.fingerprints in item['title']:
            self.fingerprints.add(item["title"])
            raise DropItem()

        return item


class JsonFeedPipeline:
    def __init__(self):
        self.json_file = open('feed.json', 'wt')
        self.json_file.write("[\n")
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.json_file.write(line)
        return item


    def close_spider(self, spider):
        self.json_file.write("\n]")
        self.json_file.close()

class CleanHTMLPipeline:
    def clear_html(self,txt):
        html = BeautifulSoup(txt,"html.parser")
        return html.get_text()

    def process_item(self, item, spider):
        item['title'] = self.clear_html(item["title"])
        item['desc'] = self.clear_html(item["desc"])

        return item
