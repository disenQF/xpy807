# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class XaPythonSpider(scrapy.Spider):
    name = 'xa_python'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['https://sou.zhaopin.com/?jl=854&kw=python&kt=3']

    page = 1

    def parse(self, response):
        with open('zhaopin.html', 'wb') as f:
            f.write(response.body)

        # 解析数据
        jobs_xpath = '//div[@class="contentpile__content__wrapper clearfix"]'
        job_nodes = response.xpath(jobs_xpath)

        print('--job count-->', len(job_nodes))

        for job_node in job_nodes:
            """
            job_a = job_node.select_one('a')
            job_href = job_a.attrs.get('href')
            job_name = job_a.select_one('.contentpile__content__wrapper__item__info__box__jobname__title').text

            company_a = job_a.select_one('.company_title')
            company_href = company_a.attrs.get('href')
            company_name = company_a.attrs.get('title')
            """

            job_a = job_node.xpath('.//a[1]')[0]
            job_href = job_a.xpath('./@href').extract_first()

            job_name_xpath = './/span[@class="contentpile__content__wrapper__item__info__box__jobname__title"]/text()'
            job_name = job_a.xpath(job_name_xpath).extract_first()

            yield {
                'job_href': job_href,
                'job_name': job_name
            }

    # # 请求下一页
    # if self.page < 10:
    #     self.page += 1
    #     next_url = response.url + '&p=%s' % self.page
    #
    #     yield Request(next_url, callback=self.parse)
