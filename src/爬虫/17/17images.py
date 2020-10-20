import re
import urllib.request
import time


#:保存网页
def savehtml(html,name):
	f=open(name,"wb")
	f.write(html)
	f.close()
	
#:读取url内的所有大图连接
def find_big_images(url):
	h1 = urllib.request.urlopen(url).read()
	#savehtml(h1,"1.html")
	h1=str(h1)
	p1='<div class="details-right-allTB-image-container".+?&nbsp;</p>.+?&nbsp;</p>'
	r1 = re.compile(p1).findall(h1)
	#print(r1)
	r1=r1[0]
	#<img alt="" src="https://img.alicdn.com/imgextra/i3/2386730806/O1CN01La96mZ1HpBqQOE6Lp_!!2386730806.jpg" style="max-width:100.0%;">
	p2="<img .*?>"
	r2 = re.compile(p2).findall(r1)
	return r2

#:下载大图文件
def download_bigimages(imgurl,folder):
	imagename = folder+"/"+ str(time.time()) + ".jpg"
	image = urllib.request.urlopen(imgurl).read()
	savehtml(image,imagename)
        
#1.读入连接文件
#2.读取商品信息
#3.筛选大图连接
#4.读取大图文件
url = "https://cs.17zwd.com/item.htm?GID=116173096&spm=56058fb00a70e556.48.140.0.0.238182.0"
find_big_images(url)  
download_bigimages("https://img.alicdn.com/imgextra/i3/2386730806/O1CN01La96mZ1HpBqQOE6Lp_!!2386730806.jpg","C:/Users/admin/Desktop")
#5.保存文件
