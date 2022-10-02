import scrapy
from gne import GeneralNewsExtractor
from urllib.parse import urlparse
# 导入实体类
from universityInformation.items import UniversityinformationItem
class UniversalSpider(scrapy.Spider):
    name = 'Universal'
    # http://www.hfut.edu.cn
    # allowed_domains = ['ustc.edu.cn']
    # start_urls = ['https://ustc.edu.cn']
    allowed_domains = ['www.hfut.edu.cn']
    start_urls = ['http://www.hfut.edu.cn']

    # scrapy 默认调用的提取函数
    def parse(self, response):
        # 实例化实体类对象
        item=UniversityinformationItem()
        # 获取访问链接
        item['visitLink']=response.url
        # 获取网页源代码
        item['pageSoure']=response.text
        # 同时提取 标题 时间 正文内容
        titleTimeContent=self.parse_article(response.text)
        # 获取网页发布文章标题
        item['contentTitle']=titleTimeContent['title']
        # 获取网页发布文章时间
        item['contentPublishTime']=titleTimeContent['publish_time']
        # 获取网页发布文章正文内容
        item['content']=titleTimeContent['content']
        # 提取所有可以访问的链接
        # 提取selector对象里字符串
        allLink=response.xpath('//li//a/@href')
        # 对可访问的链接进行处理
        allLink=self.parse_link(self.get_httpDomain(response.url),allLink.extract())
        # 遍历网页中获取的所有链接
        for link in allLink:
            # 通过scrapy引擎对每个链接发起请求
            yield scrapy.Request(link, callback=self.parse)

    
    # 定义一个提取网页标题，发布时间，正文内容的函数
    def parse_article(self,pageSource:str)->dict:
        # {"title": "xxxx", "publish_time": "2019-09-10 11:12:13", "author": "yyy", "content": "zzzz", "images": ["/xxx.jpg", "/yyy.png"]}
        html=pageSource
        extractor = GeneralNewsExtractor()
        return extractor.extract(html, noise_node_list=['//div[@class="comment-list"]'])
    
    # 定义一个通用链接处理函数
    def parse_link(self,url,linkList:list)->list:
        outList=[]
        for link in linkList:
            if 'http' in link:
                outList.append(link)
            elif '' in link:
                pass
            else:
                outList.append(self.get_httpDomain(url)+'/'+link)
        return outList
            

    # 定义一个获取域名的函数
    def get_domain(self,url:str)->str:
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        # print(domain)
        return domain
    # 定义一个获取域名前缀加域名的函数
    def get_httpDomain(self,url:str)->str:
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return domain
