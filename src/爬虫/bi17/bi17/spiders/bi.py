
#coding=utf-8

import scrapy
from scrapy import Request
from bi17.items import bi17Item
class BISpider(scrapy.Spider):
	name = "BI-17-Spider"
	
	def start_requests(self):
		url = "https://xt.17zwd.com/item.htm?GID=117105580&spm=0.52.0.32568.117105580.aa08d301008206d51af1d35c32c98772.0"
		yield Request(url)

	def parse(self,response):
		sel = response
		print("-------------------------------response-----------------------------------")
		item = bi17Item()
		#item["大图"] = sel.xpath('*//div[@class="details-right-allTB-image-container"]//img/@src')
		item["档口"] = sel.xpath('*//div[@class="shop-address"]/text()') 
		item["详情"] = sel.xpath('*//div[@class="details-right-content-item"]/text()')
		print(item)
		pass