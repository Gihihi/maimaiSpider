# -*- coding: utf-8 -*-
import scrapy


class MaimaiSpider(scrapy.Spider):
    name = 'maimai'
    allowed_domains = ['maimai.cn']
    start_urls = ['http://maimai.cn/']

    def parse(self, response):
        pass
