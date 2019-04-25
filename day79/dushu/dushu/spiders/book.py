# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['www.dushu.com']
    start_urls = ['http://www.dushu.com/book/']

    rules = (
        # 提取图书的所有分类规则， 如果没有指定callback, 默认由parse解析
        Rule(LinkExtractor(restrict_css='.sub-catalog'), follow=True),

        # 提取当前分类下的所有页规则
        Rule(LinkExtractor(restrict_css='.pages'), follow=True),

        # 提取详情页面的规则
        Rule(LinkExtractor(allow=r'/book/\d+/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        item['name'] = response.css('.book-title').xpath('./h1/text()').get()
        item['price'] = response.css('.num').xpath('./text()').get()[1:]
        item['author'] = response.css('.book-details-left').xpath('.//tr[1]//a/text()').get()
        item['publisher'] = response.css('.book-details-left').xpath('.//tr[2]//a/text()').get()

        bdr = response.css('.book-details')

        item['isbn'] = bdr.xpath('./table//tr[1]/td[2]/text()').get()
        item['publish_date'] = bdr.xpath('./table//tr[1]/td[4]/text()').get()

        # 通过当前爬虫的日志记录器（book） 记录提到的数据item
        self.logger.info(json.dumps(item))

        return item
