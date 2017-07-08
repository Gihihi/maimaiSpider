# -*- coding: utf-8 -*-
import MySQLdb
import scrapy
import json
import random
from Maimai.items import BaseItem
from Maimai.items import WorkItem
from Maimai.items import EduItem
from Maimai.items import CommentItem
from Maimai.items import SimpleItem

MYSQL_HOSTS = 'localhost'
MYSQL_USER = 'maimai'
MYSQL_PASSWORD = 'maimai'
MYSQL_PORT = 3306
MYSQL_DB = 'maimai'

cnx = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWORD, host=MYSQL_HOSTS, db=MYSQL_DB, port=MYSQL_PORT, charset='utf8')
cur = cnx.cursor()

#待爬池获取个人信息
cur.execute('select encode_mmid from simpleitem_search where id not in (select id from baseitem)')

#指定本次爬去数量
#rows = cur.fetchall()
rows = cur.fetchmany(1)

cur.close



NONE_STR = lambda x : '' if x == None else x

WORK_END_DATE = lambda x : '至今' if x == None else x

KEY_WORDS = {
		'2221' : '陌陌',
		'11070' : '豆瓣',
		'1' : '脉脉',
		'8877' : '人人网',
		'10020' : '去哪儿',
		'27394' : '友盟',
		'10041' : '优酷',
		'8220' : '爱奇艺',
		'10989' : '搜狐',
		'10993' : '今日头条',
		'8538' : '微软',
		'9859' : '滴滴',
		'12207' : '雅虎',
		'10860' : '亚马逊',
		'24030' : 'boss直聘',
		'11973' : '领英',
		'16017' : '谷歌',
	}

SEX_DICT = {
		u'他' : '男',
		u'她' : '女',
	}

DEGREE_DICT = {
		0 : '专科',
		1 : '本科',
		2 : '硕士',
		3 : '博士',
		4 : '博士后',
		5 : '其他',
		255 : '其他',
	}

class MaimaiSpider(scrapy.Spider):
	name = 'maimai'
	allowed_domains = ['maimai.cn',]
	start_urls = ['http://maimai.cn/',]

	head_url = 'https://maimai.cn/company/contacts?count='
	page_url = '&page='
	cid_url = '&cid='
	json_url = '&jsononly=1'
	
	other_cookies = {
		'token' : 'rR+0sYDAG7n4eTd50dDOoG8UZ5EGUWQao1D88xnXRC87egJdXL/riMlMlHuQj+gM8CKuzcDfAvoCmBm7+jVysA=="',
		'uid' : '"arurl0Eq1zCBSULJBihAPPAirs3A3wL6ApgZu/o1crA="',
		}

	my_cookies = [
		{
		'token' : '"JCaXZWgfZOSH7HerBGI8mZCYBUl6BUEXQ+yKKBzwb1ovLy2Lo30GuJ2zjUZ65Mfi8CKuzcDfAvoCmBm7+jVysA=="',
		'uid' : '"ZEkXyXgSVkAPNZvq3t1D1PAirs3A3wL6ApgZu/o1crA="',
		},
		{
		'token' : '"WRWyESvGsjgEusRJBcHCTouRjn27eTa62SabOkD7i6SCEEhIJYD6RqyMqIvygYJJ8CKuzcDfAvoCmBm7+jVysA=="',
		'uid' : '"ZEkXyXgSVkAPNZvq3t1D1PAirs3A3wL6ApgZu/o1crA="',
		},
		{
		'token' : '"CtH+IyzvVbolRx12RwMKYfQbfFHgXoGO1jLk1EAQXM3LztWZqFyaPoTcGFFy7HoU8CKuzcDfAvoCmBm7+jVysA=="',
		'uid' : '"ZEkXyXgSVkAPNZvq3t1D1PAirs3A3wL6ApgZu/o1crA="',
		}
		]

	my_mobile_cookies = {
		#"access_token" : "1.1b5a9b6485fea1532d7f9712c41aad16",
		#"channel" : "AppStore",
		#"version" : "4.16.36",
		"u" : "38076353",
		"koa:sess" : "eyJ1IjoiMzgwNzYzNTMiLCJzZWNyZXQiOiJfNjZLUnBhVVRCLVpteVJlNVhXWWIycmoiLCJfZXhwaXJlIjoxNDk5NTg2Mzk4NzQ0LCJfbWF4QWdlIjo4NjQwMDAwMH0=",
		"koa:sess.sig" : "G6LsEpQR7SArV1rSEo2JLpgm3t0",
			}

	def start_requests(self):
		'''
			从待爬池中获取个人url
		'''
		#for cid in KEY_WORDS.keys():
		#	i = 0
		#	while True:
		#		url = self.head_url + self.count + self.page_url + str(i) + self.cid_url + cid + self.json_url
		#		yield scrapy.Request(url, cookies=self.cookies, callback=self.parse, meta={'cid' : cid})
		#		i += 1
		#		if i == self.page:
		#			break
		#for query in KEY_WORDS.values():
		#	url =  'https://maimai.cn/search/contacts?count=20000&query=' + query +  self.json_url
		#	yield scrapy.Request(url, cookies=self.cookies, callback=self.parse, meta={'query' : query})
		referer_end_url = '?from=webview#/company/contacts'
		
		start_url = 'https://maimai.cn/contact/detail/'
		end_url = '/?from=webview%23%2Fcompany%2Fcontacts&jsononly=1'

		comment_start_url = 'https://maimai.cn/contact/comment_list/'
		comment_end_url = '/?jsononly=1'
		
		for row in rows:
			comment_url = comment_start_url + row[0] + comment_end_url
			referer = start_url + row[0] + referer_end_url
			yield scrapy.Request(comment_url, callback=self.get_comment, headers={'Referer':referer})

		for row in rows:
			person_url = start_url + row[0] + end_url
			referer = start_url + row[0] + referer_end_url
			#使用不同cookie，模拟手机或网页请求
			yield scrapy.Request(person_url, cookies=self.my_mobile_cookies, callback=self.get_info, headers={'Referer':referer})


	def parse3(self, response):

		content = json.loads(response.body)
		contacts = content['data']['contacts']
		for contact in contacts:
			item = SimpleItem()
			item['loc'] = contact['contact']['loc']
			item['company'] = contact['contact']['company']
			item['name'] = contact['contact']['name']
			item['position'] = contact['contact']['position']
			item['id'] = contact['contact']['id']
			item['cid'] = response.meta['query']
			item['encode_mmid'] = contact['contact']['encode_mmid']
			item['url'] = 'https://maimai.cn/contact/detail/' +  contact['contact']['encode_mmid'] + '?from=webview%23%2Fcompany%2Fcontacts'
			yield item
		
	def parse2(self, response):
		
		content = json.loads(response.body)
		contacts = content['data']['contacts']
		for contact in contacts:
			item = SimpleItem()
			item['loc'] = contact['contact']['loc']
			item['company'] = contact['contact']['company']
			item['name'] = contact['contact']['name']
			item['position'] = contact['contact']['position']
			item['id'] = contact['contact']['id']
			item['cid'] = response.meta['cid']
			item['encode_mmid'] = contact['contact']['encode_mmid']
			item['url'] = 'https://maimai.cn/contact/detail/' +  contact['contact']['encode_mmid'] + '?from=webview%23%2Fcompany%2Fcontacts'
			yield item

	def parse(self, response):
		'''
			解析个人员工url
		'''
		
		start_url = 'https://maimai.cn/contact/detail/'
		end_url = '?from=webview%23%2Fcompany%2Fcontacts&jsononly=1'

		comment_start_url = 'https://maimai.cn/contact/comment_list/'
		comment_end_url = '?jsononly=1'

		content = json.loads(response.body)
		contacts = content['data']['contacts']
		#for contact in contacts:
		#	person_url = start_url + contact['contact']['encode_mmid'] + end_url
		#	yield scrapy.Request(person_url, cookies=self.cookies, callback=self.get_info)

		#	comment_url = comment_start_url + contact['contact']['encode_mmid'] + comment_end_url

		#	yield scrapy.Request(comment_url, callback=self.get_comment)


	def get_info(self, response):
		'''
			解析员工个人信息
		'''
		
		content = json.loads(response.body)

		try:
			card = content['data']['card']
			uinfo = content['data']['uinfo']
			sex = content['data']['ta']

			#个人ID
			id = str(card['id'])

			#基本信息
			item = BaseItem()
			#id
			item['id'] = id
			#url
			item['url'] = response.url
			#姓名
			item['name'] = card['name']
			#头像链接
			item['img'] = card['avatar_large']
			#公司
			item['company'] = card['company']
			#职位
			item['position'] = card['position']
			#工作地
			item['work_city'] = card['province'] + '-' +  card['city']
			#性别
			item['sex'] = SEX_DICT.get(sex, '不详')
			#家乡
			item['birth_city'] = NONE_STR(uinfo.get('ht_province', '')) + '-' + NONE_STR(uinfo.get('ht_city', ''))
			if item['birth_city'] == '-':
				item['birth_city'] = ''
			#星座
			item['xingzuo'] = uinfo.get('xingzuo', '')
			#生日
			item['birthday'] = NONE_STR(uinfo.get('birthday', ''))
			#标签
			item['tag'] = ','.join(uinfo['weibo_tags'])
			yield item	
	
			#工作经历
			for work_exp in uinfo['work_exp']:
				item = WorkItem()
				item['id'] = id
				item['company'] = work_exp['company']
				item['position'] = work_exp['position']
				item['description'] = work_exp.get('description', '')
				item['start_date'] = work_exp['start_date']
				item['end_date'] = WORK_END_DATE(work_exp['end_date'])
				yield item

			#教育经历
			for edu_exp in uinfo['education']:
				item = EduItem()
				item['id'] = id
				item['school'] = edu_exp['school']
				item['degree'] = DEGREE_DICT[edu_exp.get('degree', '255')]
				item['department'] = edu_exp['department']
				item['start_date'] = edu_exp['start_date']
				item['end_date'] = edu_exp.get('end_date', '')
				yield item
		except Exception, e:
			print '===================================================='
			print e
			print '===================================================='
			print response.body
			print '===================================================='

	def get_comment(self, response):
		try:
			content = json.loads(response.body)
			comment_list = content['data']['evaluation_list']

			for comment in comment_list:
				item = CommentItem()
				item['id'] = comment['user']['id']
				item['friend_id'] = comment['src_user']['id']
				item['friend_name'] = comment['src_user']['name']
				item['friend_company'] = comment['src_user']['company']
				item['friend_position'] = comment['src_user']['position']
				item['level'] = comment['re']
				item['comment'] = comment['text']
				yield item
		except Exception, e:
			print '===================================================='
			print e
			print '===================================================='
			print response.body
			print '===================================================='
