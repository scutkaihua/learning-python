
#coding=utf-8

import scrapy
from scrapy import Request
from bi17.items import bi17Item
from bi17.lib.libbi import ShopInfo

class BISpider(scrapy.Spider):
	name = "17"
	allow_domains = ['https://xt.17zwd.com']
	start_urls = []	
	def __init__(self):
		f = open("F:/python/learning-python/src/爬虫/bi17/urls.txt","r")
		lines = f.readlines()
		for l in lines:
				self.start_urls.append(l)
		f.close()

	def parse(self,response):
		sel = response
		print("-------------------------------response-----------------------------------")
		item = bi17Item()
		item['url'] = response.url
		item["标题"] = sel.xpath('*//div[@class="goods-item-title"]//span//text()').extract()[0].replace("\n","").strip()
		item["大图"]= sel.xpath('*//div[@class="details-right-allTB-image-container"]//img/@src').extract()
		item["档口"]=sel.xpath('*//div[@class="shop-address"]/text()').extract()[0].replace("\n","").strip()
		xqtext = sel.xpath('*//div[@class="details-right-content-item"]/text()').extract();xq = ShopInfo.tokeyvalues(xqtext)#转成字典
		item["详情"] = xq
		item["信息"] = ShopInfo(response).findall()
		print(item)
		yield(item)
