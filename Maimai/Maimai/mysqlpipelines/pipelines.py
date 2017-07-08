#coding=utf-8

from sql import Sql
from twisted.internet.threads import deferToThread
from Maimai.items import BaseItem
from Maimai.items import WorkItem
from Maimai.items import EduItem
from Maimai.items import CommentItem
from Maimai.items import SimpleItem

class MaimaiPipeline(object):
	
	def process_item(self, item, spider):
		if isinstance(item, BaseItem):
			id = item['id']
			name = item['name']
			sex = item['sex']
			birthday = item['birthday']
			img = item['img']
			company = item['company']
			position = item['position']
			work_city = item['work_city']
			birth_city = item['birth_city']
			xingzuo = item['xingzuo']
			tag = item['tag']
			url = item['url']
			Sql.insert_baseitem(id, name, sex, birthday, img, company, position, work_city, birth_city, xingzuo, tag, url)
		
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
		
		if isinstance(item, CommentItem):
			id = item['id']
			friend_id = item['friend_id']
			friend_name = item['friend_name']
			friend_company = item['friend_company']
			friend_position = item['friend_position']
			level = item['level']
			comment = item['comment']
			try:
				Sql.insert_commentitem(id, friend_id, friend_name, friend_company, friend_position, level, comment)
			except:
				pass
		if isinstance(item, SimpleItem):
			id = item['id']
			cid = item['cid']
			name = item['name']
			loc = item['loc']
			company = item['company']
			position = item['position']
			encode_mmid = item['encode_mmid']
			url = item['url']
			Sql.insert_simpleitem(id, cid, name, loc, company, position, encode_mmid, url)

