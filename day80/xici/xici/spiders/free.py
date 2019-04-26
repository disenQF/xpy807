from scrapy_redis.spiders import RedisCrawlSpider

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class NnSpider(RedisCrawlSpider):

    name = 'free'
    redis_key = 'free:start_urls'

    rules = [
        Rule(LinkExtractor(allow=r'/free/inha/\d+/'), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        item = {}
        tr_list = response.css('#list').xpath('.//tbody/tr')
        for tr in tr_list:
            item['ip'] = tr.xpath('./td[1]/text()').get()
            item['port'] = tr.xpath('./td[2]/text()').get()
            item['type'] = tr.xpath('./td[4]/text()').get()

            yield item

