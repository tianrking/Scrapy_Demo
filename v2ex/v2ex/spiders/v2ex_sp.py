# -*- coding: utf-8 -*-
import scrapy
from v2ex.items import V2ExItem

class V2exSpSpider(scrapy.Spider):
    name = 'v2ex_sp'
    allowed_domains = ['v2ex.com']
    start_urls = ['https://v2ex.com']


    

    def parse(self, response):
        for t in response.xpath('//div[@class="cell item"]'):
        ##for t in response.css('div.cell item')
            ##GG=V2ExItem()
           # GG['name']= t.xpath('//span[@class]')
            ##GG['name']= "1"
            ##GG['topic']=t.xptah('/table/@width').extract_first()
            ##GG['topic']= t.xpath('//span[@class="item_title"]/a/text()]').extract_first()
            ##yield GG
            gg=t.xpath('//span[@class]')
            yield{
                "gg":gg
            }
      
