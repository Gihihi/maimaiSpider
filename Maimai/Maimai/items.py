# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SimpleItem(scrapy.Item):
	
	loc = scrapy.Field()
	company = scrapy.Field()
	name = scrapy.Field()
	position = scrapy.Field()
	id = scrapy.Field()
	cid = scrapy.Field()
	encode_mmid = scrapy.Field()
	url = scrapy.Field() 


class BaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	
	#基本信息
	id = scrapy.Field()
	url = scrapy.Field()
	name = scrapy.Field()
	img = scrapy.Field()
	company = scrapy.Field()
	position = scrapy.Field()
	work_city = scrapy.Field()
	sex = scrapy.Field()
	xingzuo = scrapy.Field()
	birthday = scrapy.Field()
	birth_city = scrapy.Field()
	tag = scrapy.Field()	
	
class WorkItem(scrapy.Item):
	
	#工作经历
	id = scrapy.Field()
	company = scrapy.Field()
	position = scrapy.Field()
	description = scrapy.Field()
	start_date = scrapy.Field()
	end_date = scrapy.Field()
	
class EduItem(scrapy.Item):
	
	#教育经历
	id = scrapy.Field()
	school = scrapy.Field()
	degree = scrapy.Field()
	department = scrapy.Field()
	start_date = scrapy.Field()
	end_date = scrapy.Field()

class CommentItem(scrapy.Item):
	
	#好友评价
	id = scrapy.Field()
	friend_id = scrapy.Field()
	friend_name = scrapy.Field()
	level = scrapy.Field()
	comment = scrapy.Field()
	friend_company = scrapy.Field()
	friend_position = scrapy.Field()
