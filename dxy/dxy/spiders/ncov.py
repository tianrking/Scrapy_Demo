# -*- coding: utf-8 -*-
import scrapy


class NcovSpider(scrapy.Spider):
    name = 'ncov'
    allowed_domains = ['ncov.dxy.cn']
    start_urls = ['https://ncov.dxy.cn/ncovh5/view/pneumonia']

    def parse(self, response):
        for x in response.css('div.fold___xVOZX'):
            oo=x.xpath('//p/@text()').extract_first()
            yield{
                "oo":oo,
            }
        pass
