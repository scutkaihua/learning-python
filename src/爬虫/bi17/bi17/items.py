# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class bi17Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    大图 = scrapy.Field()
    档口 = scrapy.Field()
    详情 = scrapy.Field()
    标题 = scrapy.Field()
    信息 = scrapy.Field()
    url = scrapy.Field()
    pass
