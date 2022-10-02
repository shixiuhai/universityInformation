import scrapy


class UniversalSpider(scrapy.Spider):
    name = 'Universal'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('----')
        print(response)
        print('----')

        
        pass
