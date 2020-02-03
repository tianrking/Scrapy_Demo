import scrapy

class BookSpider(scrapy.Spider):

    name="books"

    start_urls=["https://ncov.dxy.cn/ncovh5/view/pneumonia"]
    #start_urls=["http://books.toscrape.com/"]

    def parse(self,response):

        #for book in response.css('article.product_pod'):
        #for book in response.xpath('//article[@class="product_pod"]'):
        for  a in response.css('div.areaBlock2___27vn7'):
            #name=book.xpath('./h3/a/@title').extract_first()
            #price=book.css('p.price_color::text').extract_first()
            name = a.xpath('./p[@class="subBlock*]/text()')
            yield{
                'name': name,
                #'price': price,
            }

        # next_url=response.css('ul.pager li.next a::attr(href)').extract_first()
        # if next_url:
        #     next_url= response.urljoin(next_url)
        #     yield scrapy.Request(next_url,callback=self.parse)