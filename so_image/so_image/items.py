# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SoImageItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    url = scrapy.Field()
    pass
 
