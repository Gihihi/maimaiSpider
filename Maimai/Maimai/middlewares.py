# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
from useragent import USER_AGENTS
from proxy import PROXIES

class IPPOOLS(object):
	
	def process_request(self, request, spider):
		
		proxy = random.choice(PROXIES)
		
		#对账户密码进行base64编码转换
		base64_userpasswd = base64.b64encode(proxy['user_passwd'])
		
		#对应到代理服务器的信令格式里
		request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
		request.meta['proxy'] = 'http://' + proxy['ip_port']

class UAPOOLS(object):
	
	def process_request(self, request, spider):
		
		ua = random.choice(USER_AGENTS)

		request.headers.setdefault('User-Agent', ua)
