# -*- coding: utf-8 -*-
import scrapy
import json
import MySQLdb
from Maimai.items import SimpleItem

#数据库配置
MYSQL_HOSTS = 'localhost'
MYSQL_USER = 'maimai'
MYSQL_PASSWORD = 'maimai'
MYSQL_PORT = 3306
MYSQL_DB = 'maimai'

KEY_WORDS = [
		'陌陌',
		#'豆瓣',
		#'脉脉',
		#'人人网',
		#'去哪儿',
		#'友盟',
		#'优酷',
		#'爱奇艺',
		#'搜狐',
		#'今日头条',
		#'微软',
		#'滴滴',
		#'雅虎',
		#'亚马逊',
		#'boss直聘',
		#'领英',
		#'谷歌',
		
	]

cnx = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWORD, host=MYSQL_HOSTS, db=MYSQL_DB, port=MYSQL_PORT, charset='utf8')
cur = cnx.cursor()

#根据关键字删除数据
sql = 'delete from simpleitem where cid in '
cid_list = "('" + "','".join(KEY_WORDS) + "')"
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
		for query in KEY_WORDS:
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
