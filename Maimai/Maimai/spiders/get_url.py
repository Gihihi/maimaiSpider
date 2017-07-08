# -*- coding: utf-8 -*-
import scrapy
import json
import MySQLdb
from Maimai.items import SimpleItem
from keywords import KEYWORDS
from Maimai.settings import MYSQL_CONFIG

#数据库配置
MYSQL_HOST = MYSQL_CONFIG['MYSQL_HOST']
MYSQL_USER = MYSQL_CONFIG['MYSQL_USER']
MYSQL_PASSWD = MYSQL_CONFIG['MYSQL_PASSWD']
MYSQL_PORT = MYSQL_CONFIG['MYSQL_PORT']
MYSQL_DB = MYSQL_CONFIG['MYSQL_DB']

cnx = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWD, host=MYSQL_HOST, db=MYSQL_DB, port=MYSQL_PORT, charset='utf8')
cur = cnx.cursor()

#根据关键字删除数据
sql = 'delete from simpleitem where cid in '
cid_list = "('" + "','".join(KEYWORDS) + "')"
delete_sql = sql + cid_list
cur.execute(delete_sql)
cnx.commit()
cur.close

class GetUrlSpider(scrapy.Spider):
	name = 'get_url'
	allowed_domains = ['maimai.cn']
	start_urls = ['http://maimai.cn/']

	json_url = '&jsononly=1'

	cookies = {
		'token' : 'rR+0sYDAG7n4eTd50dDOoG8UZ5EGUWQao1D88xnXRC87egJdXL/riMlMlHuQj+gM8CKuzcDfAvoCmBm7+jVysA=="',
		'uid' : '"arurl0Eq1zCBSULJBihAPPAirs3A3wL6ApgZu/o1crA="',
		}
    
	def start_requests(self):
		'''
			搜索关键字
		'''
		for query in KEYWORDS:
			url =  'https://maimai.cn/search/contacts?count=20000&query=' + query +  self.json_url
			yield scrapy.Request(url, cookies=self.cookies, callback=self.parse, meta={'query' : query})
	
	
	def parse(self, response):
		'''
			解析个人url
		'''
		
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
