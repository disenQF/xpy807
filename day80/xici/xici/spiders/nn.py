from scrapy_redis.spiders import RedisCrawlSpider

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class NnSpider(RedisCrawlSpider):

    name = 'nn'
    redis_key = 'nn:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super().__init__(*args, **kwargs)

    rules = [
        Rule(LinkExtractor(allow=r'/nn/\d+'), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        item = {}
        tr_list = response.css('#ip_list').xpath('./tr[position()>1]')
        for tr in tr_list:
            item['ip'] = tr.xpath('./td[2]/text()').get()
            item['port'] = tr.xpath('./td[3]/text()').get()
            item['type'] = tr.xpath('./td[6]/text()').get()

            yield item

