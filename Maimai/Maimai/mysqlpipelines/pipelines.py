#coding=utf-8

from sql import Sql
from twisted.internet.threads import deferToThread
from Maimai.items import BaseItem
from Maimai.items import WorkItem
from Maimai.items import EduItem

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
			tag = item['tag']
			Sql.insert_baseitem(id, name, sex, birthday, img, description, work_city, birth_city, xingzuo, tag)
		
		if isinstance(item, WorkItem):
			id = item['id']
			company = item['company']
			position = item['position']
			description = item['description']
			start_date = item['start_date']
			end_date = item['end_date']
			Sql.insert_workitem(id, company, position, description, start_date, end_date)

		if isinstance(item, EduItem):
			id = item['id']
			school = item['school']
			degree = item['degree']
			department = item['department']
			start_date = item['start_date']
			end_date = item['end_date']
			Sql.insert_eduitem(id, school, degree, department, start_date, end_date)
			id = item['id']
