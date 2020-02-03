# -*- coding: utf-8 -*-
import scrapy


class TrumpTSpider(scrapy.Spider):
    name = 'trump_t'
    allowed_domains = ['https://twitter.com/realDonaldTrump/status/1222655839573565440']
    start_urls = ['http://https://twitter.com/realDonaldTrump/status/1222655839573565440/']

    def parse(self, response):
        pass
