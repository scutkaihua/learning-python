#!/usr/bin/env python
#coding=utf-8
import re
import urllib.request
import time
import os
import shutil
import threading
import json

#====================================================================大图===============================================================================
#:读取url内的所有大图连接
def find_1(url):
	print("查找所有大图连接 = "+url)
	h1 = urllib.request.urlopen(url).read()
	h1=str(h1)
	#多项匹配
	p1 = ['<div class="details-right-allTB-image-container".+?detail-right','<div class="details-right-allTB-image-container".+?fs-recommon']
	r0=[]
	for p in p1:
		r0 = re.compile(p).findall(h1)
		if(len(r0)>0):
			break
	r1=r0[0]
	p2="http[s]+://[img].+?.[jp][pn]g"  #过滤图片连接
	r2 = re.compile(p2).findall(r1)
	#print(r2)
	return r2  
funcs =[find_1]
def find_big_images(url):
	urls = []
	for f in funcs:
		urls = f(url)
		if(len(urls)!=0):
			return urls
	return urls                         #返回图片连接

#:下载大图文件
def download_bigimages(imgurl,folder):	
	imagename = folder+"/"+ str(time.time()) + imgurl[-4:] #大图文件名
	print(imgurl+"   ->   "+imagename)
	imagedata = urllib.request.urlopen(imgurl).read()     #大图数据
	f=open(imagename,"wb")                            #保存数据文件
	f.write(imagedata)
	f.close()
	
#:下载一个连接的大图
def download_a_url(url,folder):
	urls = find_big_images(url)
	try:
		print("删除目录:"+folder)
		shutil.rmtree(folder)                        #递归删除文件夹
	except OSError:
		pass
	os.mkdir(folder)                                 #创建目录 
	savehtml(url,folder)                             #保存跳转网页
	for u in urls:
		pass#download_bigimages(u,folder)                   #下载网页图的大图

#====================================================================连接文件===============================================================================
#:保存跳转的网页
def savehtml(url,folder):
	f=open("17.html","r")
	d = f.read()
	f.close()
	d = d.replace("myurl",url.replace("\n",""))
	#print(d)
	f=open(folder+"/html.html","w")
	f.write(d)
	f.close()

#====================================================================商品信息=================================================================================	     
#---------------------颜色
def find_color(html):
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
def find_size(html):
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
def find_huohao(html):
	#<a href="###" class="parameter-item-show">8804</a>
	p = re.compile(r'class="parameter-item-show">(.+?)</a>').findall(html)
	hh = str(time.time())
	if(len(p)>0):
		hh=p[0]
	return {'货号':hh}

#--------------------档口信息
def find_shop(html):
	p = re.compile(r'<div class="shop-address">\n+\s+([\u4e00-\u9fa5]+.+?)\s+?</div>').findall(html)
	#print(p)
	shop = str(time.time())
	if(len(p)>0):
		shop=p[0]
	return {'档口':shop}

#-------------------商品价格
def find_price(html):
	#<span class="goods-value" id="goods-pifa-price">15.00</span>
	p = re.compile(r'<span class="goods-value" id="goods-pifa-price">[￥]?(.+)</span>').findall(html)
	pr = "0"
	if(len(p)>0):
		pr=p[0]
	return {'价格':pr}

#---------------------价格
def find_price1(html):
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

#--------------------详情
def find_while_null(info,html,names,func):
	has = False
	for n in names:
		if(info.get(n,'没有')!='没有'):
			has = True
	if(has==False):
		r=func(html)
		info.update(r)

def find_info(url):
	h = urllib.request.urlopen(url).read().decode('utf-8')
	p = re.compile(r'<div class="details-right-content-item">\n+\s+(.+?)\n+\s+</div>').findall(h)
	#print(p)
	key=[]
	val=[]
	for i in p:
		key.append(re.compile(r'([\u4e00-\u9fa5/\w]+.?):').findall(i)[0].replace(" ",""))
		val.append(re.compile(r':(.+)').findall(i)[0].strip())
	#print(key,val)
	result = dict(zip(key,val))
	find_while_null(result,h,['货号'],find_huohao)
	find_while_null(result,h,["价格"],find_price)
	find_while_null(result,h,["档口"],find_shop)
	find_while_null(result,h,["尺码"],find_size)
	find_while_null(result,h,["颜色","颜色分类"],find_color)
	find_while_null(result,h,["价格"],find_price1)
	print(result)
	return result


#====================================================================多线程下载===============================================================================	  
class downLoadThread(threading.Thread):
	def __init__(self, threadID, name, url,folderparent):
		threading.Thread.__init__(self)
		self.threadID = threadID;
		self.name = name
		self.url = url
		self.folderparent=folderparent
	def run(self):
		self.info =find_info(self.url)
		self.foldername = self.folderparent+"/"+self.info["档口"]+"-" + self.info["货号"].replace("#","").replace(" ","")
		print('[线程:{} ID:{} 目录:{} 地址:{}]'.format(self.name,self.threadID,self.foldername,self.url))
		download_a_url(self.url,self.foldername)
		f=open(self.foldername+"/info.txt","w")
		jsObj = json.dumps(self.info,ensure_ascii=False, indent=4)
		f.write(jsObj)
		f.close()
		
#1.读入连接文件
f = open("./urls.txt","r")

# #创建线程
thread_counter = 0
threads = []
for line in f.readlines():
	if(len(line)>10):
		thread_counter +=1
		th = downLoadThread(thread_counter,"big-images",line.replace("\n",""),"download")
		threads.append(th)
f.close()

#启动线程
for t in threads:
	t.start()
#等待所有线程完成
for t in threads:
   t.join()
