import re
import urllib.request
import time
import os
import shutil
import threading

#====================================================================大图===============================================================================
#:读取url内的所有大图连接
def find_1(url):
	print("searching ="+url)
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
		shutil.rmtree(folder)                        #递归删除文件夹
	except OSError:
		pass
	os.mkdir(folder)                                 #创建目录 
	savehtml(url,folder)                             #保存跳转网页
	for u in urls:
		download_bigimages(u,folder)                   #下载网页图的大图

#====================================================================连接文件===============================================================================
#:保存跳转的网页
def savehtml(url,folder):
	f=open("17.html","r")
	d = f.read()
	f.close()
	d = d.replace("myurl",url.replace("\n",""))
	#print(d)
	f=open(folder+"/html.html","wb")
	f.write(d.encode())
	f.close()



#====================================================================商品信息=================================================================================	     
#====================================================================多线程下载===============================================================================	  
class downLoadThread(threading.Thread):
	def __init__(self, threadID, name, url,foldername):
		threading.Thread.__init__(self)
		self.threadID = threadID;
		self.name = name
		self.url = url
		self.foldername=foldername
	def run(self):
		print('[{} {} {} {}]'.format(self.name,self.threadID,self.foldername,self.url))
		download_a_url(self.url,self.foldername)
#1.读入连接文件
f = open("./urls.txt","r")

# #创建线程
threads = []
foldername=0
for line in f.readlines():
	if(len(line)>10):
		foldername +=1
		th = downLoadThread(foldername,"big-images",line,"download/"+str(foldername))
		threads.append(th)
f.close()

#启动线程
for t in threads:
	t.start()
#等待所有线程完成
for t in threads:
   t.join()

