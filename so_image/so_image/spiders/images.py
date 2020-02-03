# -*- coding: utf-8 -*-
import scrapy

import json
from scrapy import Request
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from so_image.items import SoImageItem


class ImagesSpider(scrapy.Spider):
   
    # BASE_URL='http://image.so.com/zj?ch=art&sn=%s&listtype=nw&temp=1'
    # start_index=0

    # MAX_DOWNLOAD_NUM=200





    # name = 'images'
    # #allowed_domains = ['image.so.com']
    # #start_urls = ['http://image.so.com/']

    # start_urls=[BASE_URL % 0]
    
    
    # def parse(self, response):
        
    #     infos=json.loads(response.body.decode('utf-8'))

    #     yield{
    #         'image_urls':[info['qhimg_url'] for info in infos['list']]
    #     }

    #     self.start_index+=infos['count']

    #     if infos['count'] > 0 and self.start_index <self.MAX_DOWNLOAD_NUM:
    #         yield Request(self.BASE_URL % self.start_index)
    name = 'images'
   # allowed_domains = ['mzitu.com']
    start_urls = ['https://www.bingwallpaperhd.com/page/2']
    img_urls = []
    def parse_item(self, response):
        print(response.url)
