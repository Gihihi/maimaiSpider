# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time
from Maimai.items import MaimaiItem

KEY_WORDS = {
		'10695' : '小米', 
	#	'10939' : '新浪',
	}

SEX_DICT = {
		'他' : '男',
		'她' : '女',
	}

class MaimaiSpider(scrapy.Spider):
	name = 'maimai'
	allowed_domains = ['maimai.cn']
	start_urls = ['http://maimai.cn/']

	#每次获取员工数量
	count = '10'
	#获取页数
	page = 2
	#请求延迟秒数
	sleep_time = 5

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
		item = MaimaiItem()

		content = response.body

		pattern_staff_info = re.compile('JSON.parse\("(.*?)\);')
		staff_info = pattern_staff_info.findall(content)[0].replace('\u0022', '"').replace('\u002D', '-')

		pattern_card = re.compile('"card":\{(.*?)\}')
		card = json.loads('{' + pattern_card.findall(staff_info)[0] + '}')

		pattern_uinfo = re.compile('"uinfo":\{(.*?)\},"addrcnt"')
		uinfo = json.loads('{' + pattern_uinfo.findall(staff_info)[0] + '}')

		pattern_sex = re.compile('"ta":"(.*?)"')
		sex = pattern_sex.findall(staff_info)[0]
		
		#基本信息
		item['id'] = str(card['id'])
		item['name'] = card['name']
		item['img'] = card['avatar_large']
		item['description'] = card['company'] + card['position']

		#工作经历
		
		#教育经历

		yield item

