# -*- coding: utf-8 -*-
import scrapy
from trump_say.items import TrumpSayItem

class SaySpider(scrapy.Spider):
    name = 'say'
    allowed_domains = ['twitter.com/realDonaldTrump']
    start_urls = ['https://twitter.com/realDonaldTrump/']

    def parse(self, response):
        
        ##for t in response.xpath('//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]'):
        for t in response.xpath('//span'):
            
            GG=TrumpSayItem()
            GG['name']= 1
            GG['text']= t.xpath('/text()').extract_first()
            yield GG
        
      
        
      