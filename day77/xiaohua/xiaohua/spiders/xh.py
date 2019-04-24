# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse


class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['www.521609.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/list32.html']

    def parse(self, response: HtmlResponse):
        li_nodes = response.xpath('//div[starts-with(@class, "index_img")]/ul/li')
        for li_node in li_nodes:
            # xpath() -> list[<Selector>, ..]
            a = li_node.xpath('./a[1]')[0]  # -> Selector
            href = 'http://www.521609.com' + a.xpath('./@href').extract_first()
            img_src = 'http://www.521609.com' + a.xpath('./img/@src').extract_first()
            name = a.xpath('./img/@alt').extract_first()

            yield {
                'name': name,
                'info_url': href,
                'img_url': img_src
            }

        # 下一页
        next_url = response.xpath('//div[@class="listpage"]//li[last()-2]/a/@href').extract_first()
        next_url = 'http://www.521609.com/daxuexiaohua/' + next_url

        yield Request(next_url, callback=self.parse)
