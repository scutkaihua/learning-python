import re
import time
import scrapy
from scrapy import Request

#商品信息
class ShopInfo(object):
	"""docstring for shopdata"""
	def __init__(self, response):
		self.html = response.text

	#---------------------颜色
	def find_color(self):
		html = self.html
		#properties_name":"1627207:28324:黄色;20509:28315:m"},
		#properties_name":"1627207:28324:\u9ec4\u8272;20509:28316:L"},
		#"properties_name":"1627207:3232480:粉红色;20509:28383:均码"},
		p = re.compile(r'properties_name":"[-\d]+:[-\d]+:([\\\w]+);[-\d]+:[-\d]+:[\\\w]+"}').findall(html)
		s = ""
		ss=[]
		if(len(p)>0):
			for i in p:
				ss.append(i.encode('utf8').decode('unicode_escape'))
			ss = sorted(list(set(ss)))
			s=" ".join(ss)
		if(s==""):
			s="未知"
		return {'颜色':s.strip()}

	#---------------------尺码
	def find_size(self):
		html = self.html
		#properties_name":"1627207:28324:黄色;20509:28315:m"},
		#properties_name":"1627207:28324:\u9ec4\u8272;20509:28316:L"},
		#"properties_name":"1627207:3232480:粉红色;20509:28383:均码"},
		#"properties_name":"1627207:-35741829:草莓兔;122216343:-1343979:14码【身高125-135CM】"}
		p = re.compile(r'properties_name":"[-\d]+:[-\d]+:[\\\w]+;[-\d]+:[-\d]+:([^}]+)"}').findall(html)
		s = ""
		ss=[]
		if(len(p)>0):
			for i in p:
				ss.append(i.encode('utf8').decode('unicode_escape'))
			ss = set(ss)
			s=" ".join(ss)
		if(s==""):
			s="未知"
		return {'尺码':s.strip()}

	#---------------------货号
	def find_huohao(self):
		html = self.html
		#<a href="###" class="parameter-item-show">8804</a>
		p = re.compile(r'class="parameter-item-show">(.+?)</a>').findall(html)
		hh = str(time.time())
		if(len(p)>0):
			hh=p[0]
		return {'货号':hh}

	#--------------------档口信息
	def find_shop(self):
		html = self.html
		p = re.compile(r'<div class="shop-address">\n+\s+([\u4e00-\u9fa5]+.+?)\s+?</div>').findall(html)
		#print(p)
		shop = str(time.time())
		if(len(p)>0):
			shop=p[0]
		return {'档口':shop}

	#-------------------商品价格
	def find_price(self):
		html = self.html
		#<span class="goods-value" id="goods-pifa-price">15.00</span>
		p = re.compile(r'<span class="goods-value" id="goods-pifa-price">[￥]?(.+)</span>').findall(html)
		pr = "0"
		if(len(p)>0):
			pr=p[0]
		return {'价格':pr}

	#---------------------价格
	def find_price1(self):
		html = self.html
		#,{"num":100000000,"price":12,"price2":12,"sku_id":7,"barcode":"
		p = re.compile(r'{"num":\d+,"price":(\d+),"price2":\d+,"sku_id":\d,"barcode":"').findall(html)
		s = ""
		ss=[]
		if(len(p)>0):
			for i in p:
				ss.append(i.encode('utf8').decode('unicode_escape'))
			ss = sorted(list(set(ss)))[0]
			s=" ".join(ss)
		if(s==""):
			s="未知"
		return {'价格1':s.strip().replace(" ","")}

	def findall(self):
		infolist = [self.find_color(),self.find_size(),self.find_price(),self.find_price1(),self.find_huohao(),self.find_shop()]
		rdict = {}
		for i in infolist:
			rdict = dict(rdict,**i)
		return rdict

	#详情=>字典
	@classmethod
	def tokeyvalues(cls,xq):
		key=[]
		val=[]
		for i in xq:
			i.replace('\n','');i.strip()
			key.append(re.compile(r'([\u4e00-\u9fa5/\w]+.?):').findall(i)[0].replace(" ",""))
			val.append(re.compile(r':(.+)').findall(i)[0].strip())
		result = dict(zip(key,val))
		return result
			


