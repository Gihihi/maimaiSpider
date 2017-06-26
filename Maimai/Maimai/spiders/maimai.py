# -*- coding: utf-8 -*-
import scrapy
import re
import json

KEY_WORDS = {
		'10695' : '小米', 
		'10939' : '新浪',
	}

class MaimaiSpider(scrapy.Spider):
	name = 'maimai'
	allowed_domains = ['maimai.cn']
	start_urls = ['http://maimai.cn/']

	#每次获取员工数量
	count = '200'

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
				i += 1
				print url
				if i == 10:
					break
				yield scrapy.Request(url, cookies=self.cookies, callback=self.parse)

	def parse(self, response):
		'''
			解析个人员工url
		'''
		start_url = 'https://maimai.cn/contact/detail/'
		end_url = '?from=webview%23%2Fcompany%2Fcontacts'
		
		#替换\u0022(")和\u002D(-)
		content = response.body.decode('raw_unicode_escape')
		#筛选公司员工信息
		pattern_staff_info = re.compile('"contacts":\[(.*?)\]')
		staff_info = pattern_staff_info.findall(content)[0]
		#获取员工url
		pattern_staff_url = re.compile('"encode_mmid":"(.*?)"')
		staff_urls = pattern_staff_url.findall(staff_info)

		for url in staff_urls:
			person_url = start_url + url + end_url
			yield scrapy.Request( person_url, cookies=self.cookies, callback=self.get_info)

	def get_info(self, response):
		'''
			解析员工个人信息
		'''
		content = response.body

		pattern_staff_info = re.compile('JSON.parse\("(.*?)\);')
		staff_info = pattern_staff_info.findall(content)[0].replace('\u0022', '"').replace('\u002D', '-')
		
		pattern_card = re.compile('"card":\{(.*?)\}')
		card = json.loads('{' + pattern_card.findall(staff_info)[0] + '}')
		print '========================================='
		print card['name']
		print '========================================='
