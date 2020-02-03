# -*- coding: utf-8 -*-
import scrapy


class HunanSpider(scrapy.Spider):
    name = 'hunan'

    start_urls = ['http://www.hunan.gov.cn/hnszf/hnyw/zwdt/szdt_sjpx.html/']

    def parse(self, response):
        for t in response.xpath('//li[@class="active"]'):
        ##for t in response.css('li.active'):
            gg=t.xpath('./a/@title').extract_first()
            yield{
                "gg":gg
            }
        pass
