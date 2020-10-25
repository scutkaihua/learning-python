# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class JdPipeline:
	def __init__(self):
		self.f = open("F:/jd.txt","w",encoding='utf-8')

	def process_item(self, item, spider):
		return item

	def close_spider(self,spider):
		print("--------------------pipeline save-----------------")
		spider.items['info'].sort(key=lambda x:int(x["pageindex"])*50 + int(x["index"]))
		#print(spider.items)
		self.f.write("{info:[\n")
		for i in spider.items['info']:
			self.f.write(json.dumps(dict(i),ensure_ascii=False,indent=4)+",")
		self.f.write("\n]}")
		self.f.close()


