
#coding=utf-8

import scrapy
from scrapy import Request
from jd.items import JdItem
import json
import re
class JdSpider(scrapy.Spider):
	default_headers = {
        # 'accept': 'image/webp,image/*,*/*;q=0.8',
        # 'accept-encoding': 'gzip, deflate, sdch, br',
        # 'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        # 'cookie': 'bid=yQdC/AzTaCw',
        # 'referer': 'https://list.jd.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
	name = "Jd"
	allow_domains = ['https://list.jd.com/list.html',"https://www.baidu.com/","https://club.jd.com/"]

  #   def  __init__(self):
		# self.items = {"info":[]}
		# for i in range(1,2):
		# 	p_url = 'https://list.jd.com/list.html?cat=9987%2C653%2C655&psort=3&psort=3&page='+str(i) +'&s=20'
		# 	self.start_urls.append(p_url)


	def start_requests(self):
		self.items = {"info":[]}
		for i in range(1,10):
			p_url = 'https://list.jd.com/list.html?cat=9987%2C653%2C655&psort=3&psort=3&page='+str(i) +'&s=20'
			yield Request(url=p_url,callback=self.parse_detail,headers=self.default_headers,meta={'pageindex':i})


	def parse_detail(self,response):		
		sel = response
		pageindex = response.meta['pageindex']
		print("-------------------------------response-----------------------------------")
		price = sel.xpath('*//div[@id="J_goodsList"]//div[@class="p-price"]//i/text()').extract()
		name = sel.xpath('*//div[@id="J_goodsList"]//div[@class="p-name p-name-type-3"]//em/text()').extract()
		shopid =   sel.xpath('*//div[@id="J_goodsList"]//div[@class="p-shop"]').extract()
		picture = sel.xpath('*//div[@id="J_goodsList"]//div[@class="p-img"]//img/@data-lazy-img').extract()
		productId = sel.xpath('*//div[@id="J_goodsList"]//li[@class="gl-item"]/@data-sku').extract()
		for i in range(0,len(price)):
			item = JdItem()
			item["pageindex"]=pageindex
			item['index'] = str(i+1)
			item['ok']='False'
			item['价格']=price[i]
			item['品牌']=name[i]
			shop = re.compile(r'title="(.+?)">').findall(shopid[i])
			if(len(shop)==0):
				shop=""
			else:
				shop = shop[0]
			item['店铺']=shop
			item['图片']=picture[i]
			item['ID']=productId[i]
			item['page_url']=response.url
			item['url']="https://item.jd.com/"+item['ID']+".html"
			json_url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds="+item["ID"]
			yield Request(url=json_url,callback=self.parse_json,meta={'item':item},headers=self.default_headers)

	def parse_json(self,response):		
		item = response.meta['item']
		print("-------------------------------json-----------------------------------")
		sites = json.loads(response.text,strict=False)
		sites = sites["CommentsCount"][0]
		item["评价"] = sites["CommentCountStr"]
		item["销量"] = sites["GoodCount"]
		item['ok']='True'
		self.items['info'].append(item)
		print(item)
		yield item

	def parse(self,response):
		pass
			



