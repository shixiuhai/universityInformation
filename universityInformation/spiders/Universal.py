import scrapy
from gne import GeneralNewsExtractor
from urllib.parse import urlparse
# 导入学校信息
from universityInformation.utils import get_university_information
# 导入实体类
cont=0
from universityInformation.items import UniversityinformationItem
class UniversalSpider(scrapy.Spider):
    name = 'Universal'

    # allowed_domains = ['ustc.edu.cn']
    # start_urls = ['https://ustc.edu.cn']
    allowed_domains = []
    start_urls = []
    # 进行从文档中读取
    domainList=get_university_information("schoolDomainName")
    for domain in domainList:
        allowed_domains.append(domain)
        # 添加到url里 所有的domain都添加上http，为了子域名考虑
        start_urls.append("http://"+domain)
    print(allowed_domains,start_urls)

    # scrapy 默认调用的提取函数
    def parse(self, response):
        global cont
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
        yield item
        # 提取所有可以访问的链接
        # 提取selector对象里字符串
        # allLink=response.xpath('//li//a/@href')
        allLink=response.xpath('//a/@href')
        # 对可访问的链接进行处理
        allLink=self.parse_link(self.get_httpDomain(response.url),allLink.extract())
        # 遍历网页中获取的所有链接
        print("提取的新页面链接是%s"%len(allLink))
        for link in allLink:
            cont=cont+1
            # 通过scrapy引擎对每个链接发起请求
            yield scrapy.Request(link, callback=self.parse)
        print("爬取的总页面是%s"%cont)

    
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
            elif '' in link or '.png' in link or '.jpg' in link or 'js' in link:
                pass
            else:
                outList.append(self.get_httpDomain(url)+'/'+link)
                print("拼接的链接是---------")
                print(self.get_httpDomain(url)+'/'+link)
                print("拼接的链接是---------")

                
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
