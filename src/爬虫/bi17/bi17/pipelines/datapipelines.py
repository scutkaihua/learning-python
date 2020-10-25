# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.utils.project import get_project_settings
from itemadapter import ItemAdapter
import json

class BITxtPipeline(object):

	#保存商品详细信息
	def process_item(self,item,spider):
		#----------------------------------详情-----------------------
		folder = item.get('标题')
		xq = item.get('详情')
		xin = item.get('信息')
		item['详情'] = dict(xin,**xq)
		IMAGES_STORE=get_project_settings().get('IMAGES_STORE')
		folder = IMAGES_STORE + "/full/"+folder
		info = json.dumps(dict(item),ensure_ascii=False,indent=4)
		f = open(folder+"/info.txt","w")
		f.write(info)
		f.close()

		#----------------------------------跳转页面-----------------------
		html = '<!DOCTYPE html> \
<html lang="en"> \
<head> \
	<meta charset="UTF-8"> \
	<title>titlename</title> \
	<script language=\'JavaScript\'> \
		document.location="myurl" \
	</script> \
</head> \
<body> \
	<a href="myurl">jump to src url=baidu</a> \
</body> \
</html>'
		url = item.get('url')
		html = html.replace("myurl",url)
		f = open(folder+"/html.html","w")
		f.write(html)
		f.close()
		print("--------------datapipelines-----------")
		print(info)
		return item