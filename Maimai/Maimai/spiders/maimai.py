# -*- coding: utf-8 -*-
import scrapy

KEY_WORDS = {
		'10692' : '小米', 
		#'10939' : '新浪',
	}

class MaimaiSpider(scrapy.Spider):
	name = 'maimai'
	allowed_domains = ['maimai.cn']
	start_urls = ['http://maimai.cn/']

	cid_url = 'https://maimai.cn/company/contacts?cid='
	company_url = '&company='
	end_url = '&forcomp=1&highlight=false&title=所有员工'

	cookies = {
		'token' : '"nW56bx8KqRtobT9ZpyKoW7LSl23Lelwu2j/yC3Uxmp7E8chkqpLBOKIMDf+fnU578CKuzcDfAvoCmBm7+jVysA=="',
		'uid' : '"ZEkXyXgSVkAPNZvq3t1D1PAirs3A3wL6ApgZu/o1crA="',
		}

	def start_requests(self):
		'''
			查询公司所有员工
		'''
		for item in KEY_WORDS.items():
			url = self.cid_url + item[0] + self.company_url + item[1] + self.end_url
			yield scrapy.Request(url, cookies=self.cookies, callback=self.parse)

	def parse(self, response):
		'''
			解析个人员工url
		'''
		print '========================================'
		print response.body
		print '========================================'

	def get_info(self, response):
		pass
