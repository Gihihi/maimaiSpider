# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time
from Maimai.items import BaseItem
from Maimai.items import WorkItem
from Maimai.items import EduItem

NONE_STR = lambda x : '' if x == None else x

WORK_END_DATE = lambda x : '至今' if x == None else x

KEY_WORDS = {
		'10695' : '小米', 
		#'10939' : '新浪',
	}

SEX_DICT = {
		'他' : '男',
		'她' : '女',
	}

DEGREE_DICT = {
		0 : '专科',
		1 : '本科',
		2 : '硕士',
		3 : '博士',
		4 : '博士后',
		255 : '其他',
	}

class MaimaiSpider(scrapy.Spider):
	name = 'maimai'
	allowed_domains = ['maimai.cn',]
	start_urls = ['http://maimai.cn/',]

	#每次获取员工数量
	count = '2'
	#获取页数
	page = 1
	#请求延迟秒数
	sleep_time = 0

	head_url = 'https://maimai.cn/company/contacts?count='
	page_url = '&page='
	cid_url = '&cid='
	json_url = '&jsononly=1'

	cookies = {
		'token' : '"nW56bx8KqRtobT9ZpyKoW7LSl23Lelwu2j/yC3Uxmp7E8chkqpLBOKIMDf+fnU578CKuzcDfAvoCmBm7+jVysA=="',
		'uid' : '"ZEkXyXgSVkAPNZvq3t1D1PAirs3A3wL6ApgZu/o1crA="',
		}

	def start_requests(self):
		'''
			查询公司员工
		'''
		for cid in KEY_WORDS.keys():
			i = 0
			while True:
				url = self.head_url + self.count + self.page_url + str(i) + self.cid_url + cid + self.json_url
				time.sleep(self.sleep_time)
				yield scrapy.Request(url, cookies=self.cookies, callback=self.parse)
				i += 1
				if i == self.page:
					break

	def parse(self, response):
		'''
			解析个人员工url
		'''
		start_url = 'https://maimai.cn/contact/detail/'
		end_url = '?from=webview%23%2Fcompany%2Fcontacts'
		content = json.loads(response.body)
		contacts = content['data']['contacts']
		for contact in contacts:
			person_url = start_url + contact['contact']['encode_mmid'] + end_url
			time.sleep(self.sleep_time)
			yield scrapy.Request(person_url, cookies=self.cookies, callback=self.get_info)

	def get_info(self, response):
		'''
			解析员工个人信息
		'''

		content = response.body

		pattern_staff_info = re.compile('JSON.parse\("(.*?)\);')
		staff_info = pattern_staff_info.findall(content)[0].replace('\u0022', '"').replace('\u002D', '-')

		pattern_card = re.compile('"card":\{(.*?)\}')
		card = json.loads('{' + pattern_card.findall(staff_info)[0] + '}')

		pattern_uinfo = re.compile('"uinfo":\{(.*?)\},"addrcnt"')
		uinfo = json.loads('{' + pattern_uinfo.findall(staff_info)[0] + '}')

		pattern_sex = re.compile('"ta":"(.*?)"')
		sex = pattern_sex.findall(staff_info)[0]
		
		#个人ID
		id = str(card['id'])

		#基本信息
		item = BaseItem()
		#id
		item['id'] = id
		#姓名
		item['name'] = card['name']
		#头像链接
		item['img'] = card['avatar_large']
		#公司+职位
		item['description'] = card['company'] + card['position']
		#工作地
		item['work_city'] = card['province'] + '-' +  card['city']
		#性别
		if sex in SEX_DICT.keys():
			item['sex'] = SEX_DICT[sex]
		else:
			item['sex'] = '不详'
		#家乡
		if 'ht_city' in uinfo.keys() and 'ht_province' in uinfo.keys():
			item['birth_city'] = NONE_STR(uinfo['ht_province']) + '-' + NONE_STR(uinfo['ht_city'])
			if item['birth_city'] == '-':
				item['birth_city'] = ''
		else:
			item['birth_city'] = ''
		#星座
		if 'xingzuo' in uinfo.keys():
			item['xingzuo'] = uinfo['xingzuo']
		else:
			item['xingzuo'] = ''
		#生日
		if 'birthday' in uinfo.keys():
			item['birthday'] = NONE_STR(uinfo['birthday'])
		else:
			item['birthday'] = ''
		#标签
		tag_list = ''
		for tag in uinfo['weibo_tags']:
			tag_list += tag + ','
		item['tag'] = tag_list[:-1]
		yield item	
		
		#工作经历
		for work_exp in uinfo['work_exp']:
			item = WorkItem()
			item['id'] = id
			item['company'] = work_exp['company']
			item['position'] = work_exp['position']
			if 'descroption' in work_exp.keys():
				item['description'] = work_exp['description']
			else:
				item['description'] = ''
			item['start_date'] = work_exp['start_date']
			item['end_date'] = WORK_END_DATE(work_exp['end_date'])
			yield item

		#教育经历
		for edu_exp in uinfo['education']:
			item = EduItem()
			item['id'] = id
			item['school'] = edu_exp['school']
			if 'degree' in edu_exp.keys():
				item['degree'] = DEGREE_DICT[edu_exp['degree']]
			else:
				item['degree'] = '' 
			item['department'] = edu_exp['department']
			item['start_date'] = edu_exp['start_date']
			item['end_date'] = edu_exp['start_date']
			yield item

