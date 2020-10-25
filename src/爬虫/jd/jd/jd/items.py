# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    价格 = scrapy.Field()
    品牌 = scrapy.Field()
    销量 = scrapy.Field()
    店铺 = scrapy.Field()
    评价 = scrapy.Field()
    图片 = scrapy.Field()
    ID = scrapy.Field()
    url = scrapy.Field()
    page_url = scrapy.Field()
    ok = scrapy.Field()
    index = scrapy.Field()
    pageindex = scrapy.Field()
    pass
