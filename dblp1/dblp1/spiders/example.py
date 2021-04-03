import scrapy
from dblp1.items import Dblp1Item

class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['example.com']
    #起始页
    # f_list = ['0', '1000', '2000', '3000']
    # h_list = ["999", "1999", "2999", "3706"]
    # for i in range(0,4):
    #     h=h_list[i]
    #     f=f_list[i]
    # 这个方法不知道为什么跑不出来，只能得到最后706条数据，决定手动跑四次试试
    #通过反复测试得出h和f值的规律，存在于表格中
    # 应为：
    # f_list = ['0', '1000', '1999', '2998']
    # h_list = ["1000", "2000", "2999", "3707"]
    start_urls = ['https://dblp.org/search/publ/inc?q=logistics&h=3707&f=2998&s=ydvspc']
    # start_urls = ["http://www.baidu.com"]

    def parse(self, response):
        # 分组，获取响应处理数据
        li_list = response.xpath('//li[contains(@class,"entry")]')
        # print(len(li_list))
        # return
        # i = 0
        #遍历拿到所有数据
        for li in li_list:
            # i=i+1
            # print(i)
            item=Dblp1Item()
            item["title"] = li.xpath('./cite[@class="data"]/span[@class="title"]/text()').extract_first()
            item["href"]=response.xpath('//li[contains(@class,"entry")]/nav/ul/li/div/a/@href').extract_first()
            item["author_name"] = li.xpath('./cite[@class="data"]/span[@itemprop="author"]//a/span/text()').extract()
            item["journal_list"]=li.xpath('./cite[@class="data"]/a/span[1]/span/text()').extract_first()
            item["publish_date"]=li.xpath('./cite[@class="data"]//span[@itemprop="datePublished"]/text()').extract()
            # print(item)
            yield item
            # yield scrapy.Request(url=item["href"], callback=self.parse_detail, meta={"item": item})
        # #翻页功能：
        # for i in range(124):
        #     # 一共3704篇文献，一个页面可以加载30篇文献，所以需要124次刷新页面
        #     next_url = 'https://dblp.uni-trier.de/search/publ/inc?q=logistics&s=ydvspc&h=30&b='+str(i)
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
    # def parse_detail(self,response):#处理详情页
    #     item = response.meta["item"]
    #     if item["journal_list"] == "IEEE Access":
    #         item["abstract"] =response.xpath('head/meta[@property="twitter:description"]/text()').extract_first()
    #     if item["journal_list"] == "Adv. Eng. Informatics":
    #         item["abstract"] = response.xpath('//p[@id="sp0010"]/text()').extract_first()
    #     else:
    #         item["abstract"] = None
    #     # item["author_keywords"]=
    #     # print(item)
    #     yield item
