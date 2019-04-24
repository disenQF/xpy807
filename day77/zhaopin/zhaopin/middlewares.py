# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.webdriver import Chrome
from selenium.webdriver.support import ui, expected_conditions as ec
from selenium.webdriver.common.by import By


class ZhaopinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhaopinDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # [重点]
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumDownloader(object):
    """
    自定义selenium的下载中间件
    实现网页请求由selenium 下载，不经过scrapy的下载器（Downloader）
    """

    def __init__(self):
        # 创建selenium的浏览器对象
        # window->   d:/drivers/chromedriver.exe
        # linux->    /home/xxxx/drivers/chromedriver
        self.browser = Chrome('/Users/apple/drivers/chromedriver')  # mac
        self.close_ok = False  # 第一次弹出 窗口，需要点击『我知道了』关闭窗口

    def process_request(self, request, spider):
        # 将会由selenium的chrome浏览器来请求
        self.browser.get(request.url)

        if not self.close_ok:
            # 关闭
            ok_btn = self.browser.find_element_by_class_name('risk-warning__content').find_element_by_tag_name('button')
            ok_btn.click()

            self.close_ok = True

        #  等待网页中soupager可以选择（可见）
        ui.WebDriverWait(self.browser, 60).until(
            ec.visibility_of_all_elements_located((By.CLASS_NAME, 'soupager')))

        # 获取页面标签的高度
        soupager = self.browser.find_element_by_class_name('soupager')
        soupager_height = soupager.location['y']

        time.sleep(1)

        # 向下滚动
        # 滚动屏幕到底部
        current_height = 0
        for i in range(20):
            current_height = (i + 1) * 1000
            if current_height >= soupager_height:
                break

            self.browser.execute_script('var q = document.documentElement.scrollTop=%s' % current_height)
            time.sleep(0.5)



        # 获取网页数据
        html = self.browser.page_source

        return HtmlResponse(url=request.url,
                            body=html.encode(encoding='utf-8'),
                            encoding='utf-8')


def __del__(self):
    self.browser.quit()
