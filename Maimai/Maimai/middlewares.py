# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from useragent import USER_AGENTS
from useragent import MOBILE_USER_AGENTS

class Http_code_400(object):
	def process_response(self, request, response, spider):
		if response.status == 400:
			return request
		return response
	

class ProxyMiddleWare(object):
	def process_request(self, request, spider):
		proxy = self.get_random_proxy()
		print ('this is request ip:' + proxy)
		request.meta['proxy'] = proxy
	
	def process_response(self, request, response, spider):
		if response.status != 200:
			proxy = self.get_random_proxy()
			print ('this is request ip:' + proxy)
			request.meta['proxy'] = proxy
			return request
		return response

	def get_random_proxy(self):
		while True:
			with open('/home/python/GitHub/maimaiSpider/Maimai/Maimai/proxies.txt', 'r') as f:
				proxies = f.readlines()
			if proxies:
				break
		proxy = random.choice(proxies).strip()
		return proxy


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
		#手机
		#ua = random.choice(MOBILE_USER_AGENTS)
		#网页
		ua = random.choice(USER_AGENTS)

		try:
			request.headers.setdefault('User-Agent', ua)
		except Exception, e:
			print e
