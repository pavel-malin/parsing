import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for href in response.css('.product_pod a::attr(href)').extract():
            url = response.urljoin(href)
            print(url)
