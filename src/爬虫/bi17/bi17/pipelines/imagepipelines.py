# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import time

class DoubanImgsPipeline(object):
    def process_item(self, item, spider):
        return item


class DoubanImgDownloadPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'referer': 'https://www.douban.com/photos/photo/2370443040/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }


    # def file_path(self, request, response=None, info=None):
        
    #     path = 'full/'+self.folder+'/'+ str(time.time()) + request.url[-4:]
    #     print("+++++++++++++++++++folder:");print(path)
    #     return path

    def file_path(self, request, response=None, info=None, *, item=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        path=super(DoubanImgDownloadPipeline, self).file_path(request,response,info)
        category=request.item.get('标题')[0]
        print("+++++++++++++++++++++++++++++++++++file_path:")
        image_path = "full/"+category+"/"+request.name
        print(image_path)
        return image_path

    def get_media_requests(self, item, info):
        i = 0
        for image_url in item['大图']:
            i+=1
            self.default_headers['referer'] = image_url
            #self.folder = item["标题"][0]
            myrequest = Request(image_url, headers=self.default_headers)
            myrequest.item = item
            myrequest.name = str(i)+".jpg"
            yield myrequest
