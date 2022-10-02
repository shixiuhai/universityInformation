import scrapy


class UniversalSpider(scrapy.Spider):
    name = 'Universal'
    allowed_domains = ['test.com']
    start_urls = ['http://test.com/']

    def parse(self, response):
        pass
