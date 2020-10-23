import scrapy
from scrapy import Request

class TestSpider(scrapy.Spider):
	name = "test"
	
	def start_requests(self):
		url = "https://xt.17zwd.com/item.htm?GID=117105580&spm=0.52.0.32568.117105580.aa08d301008206d51af1d35c32c98772.0"
		yield Request(url)

	def parse(self,response):
		print("---------------------Spider test response--------------------")
		pass

# class bi17Spider(scrapy.Spider):
# 	name = "test"
	
# 	def start_requests(self):
# 		url = "https://xt.17zwd.com/item.htm?GID=117105580&spm=0.52.0.32568.117105580.aa08d301008206d51af1d35c32c98772.0"
# 		yield Request(url)

# 	def parse(self,response):
# 		print("-------------------------------response-----------------------------------")
# 		#item = bi17Item()
# 		#item["imgs"] = response.xpath('*//div[@class="details-right-allTB-image-container"]//img')
# 		print(item)
# 		pass
