# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from useragent import USER_AGENTS
#from ip import IP_POOL

class UAPOOLS(UserAgentMiddleware):
	
	def __init__(self, user_agent = ''):
		'''
			初始化
		'''
		self.user_agent = user_agent

	def process_request(self, request, spider):
		'''
			使用代理UA，随机选用
		'''
		ua = random.choice(USER_AGENTS)

		try:
			request.headers.setdefault('User-Agent', ua)
		except Exception, e:
			print e

class IPPOOLS(HttpProxyMiddleware):
	
	def __init__(self, ip = ''):
		'''
			初始化
		'''
		self.ip = ip

	def process_request(self, request, spider):
		'''
			使用代理ip，随机选用
		'''
		ip = random.choice(self.ip_pool)#IP_POOL

		try:
			request.meta['proxy'] = 'https://' + ip['ip']
		except Exception, e:
			print e

	ip_pool = [
		{'ip' : '119.75.216.20'},
		]
