from scrapy import Spider
from scrapy import FormRequest

class LogSpider(Spider):

    name = 'log'
    allow_domains = ['localhost',
                     '10.12.152.218']

    def start_requests(self):
        yield FormRequest('http://10.12.152.218:5000/log/',
                          formdata={
                              'name': 'disen',
                              'levelname': 'INFO',
                              'message': 'hi, formrequest'
                          },
                          callback=self.parse)

    def parse(self, response):
        print(response.url)
        print(response.text)