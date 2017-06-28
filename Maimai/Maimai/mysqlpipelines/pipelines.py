#coding=utf-8

from sql import Sql
from twisted.internet.threads import deferToThread
from Maimai.items import BaseItem

class MaimaiPipeline(object):
	
	def process_item(self, item, spider):
		if isinstance(item, BaseItem):
			id = item['id']
			name = item['name']
			sex = item['sex']
			birthday = item['birthday']
			img = item['img']
			description = item['description']
			work_city = item['work_city']
			birth_city = item['birth_city']
			xingzuo = item['xingzuo']
			Sql.insert_baseitem(id, name, sex, birthday, img, description, work_city, birth_city, xingzuo)
