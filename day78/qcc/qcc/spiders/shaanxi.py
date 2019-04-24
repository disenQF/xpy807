# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ShaanxiSpider(scrapy.Spider):
    name = 'shaanxi'
    allowed_domains = ['www.qichacha.com']
    start_urls = ['https://www.qichacha.com/g_SAX.html']

    def parse(self, response):
        sections = response.xpath('//section[@id="searchlist"]')

        for section in sections:
            company_href = section.xpath('./a/@href').extract_first()
            company_href = 'https://www.qichacha.com'+company_href
            yield Request(company_href, callback=self.parse_detail)

        # 下一页
        next_url = response.xpath('//a[@class="next"]/@href').extract_first()
        next_url = 'https://www.qichacha.com'+next_url
        yield Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        company_name = response.xpath('//div[@class="content"]//h1/text()').extract_first()
        company_phone = response.xpath('//span[@class="cvlu"]/span/text()').extract_first()

        item = locals()
        del item['response']
        del item['self']

        yield item
