# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse


class GndySpider(scrapy.Spider):
    name = 'gndy'
    #  域名列表-> hostname列表
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response: HtmlResponse):
        # pip install pywin32
        # response : scrapy.http.response.html.HtmlResponse
        # response是特殊的响应类对象，
        # 可以通过xpath()或select()两种方式提取数据
        # 也可以直接使用css()
        # response.xpath()
        # response.text  # 文本信息
        # response.body  # 字节数据
        # response.url   #  请求的url
        # response.encoding  # 编码字符集
        # response.headers  # 响应头
        # response.status  # 状态码
        # response.request  # 响应的请求对象
        # response.meta   # 响应的媒体数据，包含特定的数据（request传送数据时使用）
        # //div[@class="co_content8"]//tbody//a/text()
        table_nodes = response.xpath('//div[@class="co_content8"]//table')
        # print(response.text)
        for table in table_nodes: # table_nodes -> list[<Selector>, <Selector>, ..]
            a = table.xpath('.//a')[0]  # Selector 对象

            href = a.xpath('./@href').extract()[0]  # extract提取后，就list[str, ..]对象
            title = a.xpath('./text()').extract()[0]

            # 如果查询没有元素的时候，返回None,
            # 有可能会出现 None 没有extract()函数异常
            summary = table.xpath('./tr[last()]/td/text()').extract()[0]

            yield {
                'href': href,
                'title': title,
                'summary': summary
            }

        # 获取下一页的连接
        try:
            next_href = response.xpath('//div[@class="x"]//a[last()-1]/@href').extract()[0]
            print('----next href---->', next_href)

            next_href = 'https://www.dytt8.net/html/gndy/dyzz/'+next_href

            # 发起一个新的请求
            # 请求类 --> 响应类
            # scrapy.Request -> scrapy.http.response.HtmlResponse
            yield Request(next_href, callback=self.parse )
        except:
            pass


