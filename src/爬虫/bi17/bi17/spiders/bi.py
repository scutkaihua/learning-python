
#coding=utf-8

import scrapy
from scrapy import Request
from bi17.items import bi17Item
class BISpider(scrapy.Spider):
	name = "17"
	allow_domains = ['https://xt.17zwd.com']
	start_urls = [
				'https://xt.17zwd.com/item.htm?GID=117105580&spm=0.52.0.32568.117105580.aa08d301008206d51af1d35c32c98772.0',
				'https://xt.17zwd.com/item.htm?GID=116567031&spm=56058fb00a70e556.52.140.0.0.251352.0'
				]	
	def parse(self,response):
		sel = response
		print("-------------------------------response-----------------------------------")
		item = bi17Item()
		item["标题"] = sel.xpath('*//div[@class="goods-item-title"]//span//text()').extract()
		item["大图"]= sel.xpath('*//div[@class="details-right-allTB-image-container"]//img/@src').extract()
		#item["档口"]=sel.xpath('*//div[@class="shop-address"]/text()').extract()
		#item["详情"] = sel.xpath('*//div[@class="details-right-content-item"]/text()').extract()
		yield(item)
