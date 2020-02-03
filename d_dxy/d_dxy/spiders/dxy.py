# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class DxySpider(scrapy.Spider):
    name = 'dxy'
    allowed_domains = ['ncov.dxy.cn']
    start_urls = ['https://ncov.dxy.cn/ncovh5/view/pneumonia']
  
    # def parse(self, response):
    #     pass
    def start_requests(self):
        # splash_args = {
        #     'wait': 0.5,
        # }
        # for url in self.start_urls:
        # #    yield SplashRequest(url, endpoint='render.html',
        #                         args=splash_args)
        for url in self.start_urls:
            yield SplashRequest(url,args={'images':0})

    def parse(self, response):
        # for oo in response.xpath('//body'):
        #     ooo=oo.xpath('//script[@id="getAreaStat"]/text()')
        #     yield {
        #         'ooo': ooo,
        #     }
        # for oo in response.css('p.subBlock2___E7-fW'):
        #     ooo=oo.xpath('./text()').extract_first()
        #     yield{
        #         "ooo":ooo,
        #     }
        #ooo=response.css('script.getAreaStat').extract_first()
        ooo=response.xpath('//script[@id="getAreaStat"]/text()').extract_first()
        #ooo=response.xpath('//title/text()').extract_first()
        yield{
            'oooo':ooo,
        }
       


        pass
        