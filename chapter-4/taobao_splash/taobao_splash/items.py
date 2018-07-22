# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html



from scrapy import Item, Field

class ProductItem(Item):
    name = Field()        # 品名
    link = Field()        # 链接地址
    sn = Field()          # 货号
    image_url = Field()   # 产品图片地址
    image_path = Field()  # 图片下载至本地的位置
    price = Field()       # 价格
    deal = Field()        # 成交人数
    free_shipping  = Field() # 是否包邮
    shop = Field()        # 淘宝店名
    location = Field()    # 地区