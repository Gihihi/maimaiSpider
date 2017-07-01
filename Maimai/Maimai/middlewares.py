# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
#from scrapy.downloadermiddlewares.httpproxy import HttpPorxyMiddleware
from useragent import USER_AGENTS


class UAPOOLS(UserAgentMiddleware):
	def __init__(self, user_agent = ''):
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
