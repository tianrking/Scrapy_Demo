# import scrapy

# class TrumpSpider(scrapy.Spider):

#     name="Trump"

#     start_urls=["https://www.youtube.com/watch?v=IOPRJy71TEQ/"]

#     def parse(self,response):

#         for trump_ in response.css('ytd-comment-renderer.comment'):

#             name=trump_.xpath('//a[@id="author-text"]/span/text()')
#             ##price=book.css('p.price_color::text').extract_first()

#             yield{
#                 'name': name,
#                 #'price': price,
#             }

#         # next_url=response.css('ul.pager li.next a::attr(href)').extract_first()
#         # if next_url:
#         #     next_url= response.urljoin(next_url)
#         #     yield scrapy.Request(next_url,callback=self.parse)

import scrapy

class BookSpider(scrapy.Spider):

    name="trump"

    start_urls=["http://books.toscrape.com/"]

    def parse(self,response):

        for book in response.css('article.product_pod'):

            name=book.xpath('./div[@class="image_container"]/a/img/@alt').extract_first()
           # name=book.xpath('./h3/a/@title').extract_first()
            price=book.css('p.price_color::text').extract_first()

            yield{
                'name': name,
                'price': price,
            }

        # next_url=response.css('ul.pager li.next a::attr(href)').extract_first()
        # if next_url:
        #     next_url= response.urljoin(next_url)
        #     yield scrapy.Request(next_url,callback=self.parse)