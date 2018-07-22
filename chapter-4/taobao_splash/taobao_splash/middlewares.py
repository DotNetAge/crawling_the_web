# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy_splash import SplashRequest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger

class TaobaoSplashSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    lua_source = """
         function wait_for_element(splash, css, maxwait)
           -- Wait until a selector matches an element
           -- in the page. Return an error if waited more
           -- than maxwait seconds.
           if maxwait == nil then
               maxwait = 10
           end
           return splash:wait_for_resume(string.format([[
             function main(splash) {
               var selector = '%s';
               var maxwait = %s;
               var end = Date.now() + maxwait*1000;

               function check() {
                 if(document.querySelector(selector)) {
                   splash.resume('Element found');
                 } else if(Date.now() >= end) {
                   var err = 'Timeout waiting for element';
                   splash.error(err + " " + selector);
                 } else {
                   setTimeout(check, 200);
                 }
               }
               check();
             }
           ]], css, maxwait))
     end

    function main(splash, args)
       splash:go(args.url)
       wait_for_element(splash, "#mainsrp-itemlist")
       return splash:html()
    end
 """

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
            yield SplashRequest(r.url,
                                r.callback,
                                endpoint='execute',
                                meta=dict(r.meta),
                                args={
                                    'lua_source': self.lua_source,
                                    'wait': 3}
                                )

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumMiddleware():

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))

    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)  # 打开日志
        self.timeout = timeout
        self.browser = webdriver.PhantomJS(service_args=service_args)
        self.browser.set_window_size(1400, 700) # 设置浏览窗口
        self.browser.set_page_load_timeout(self.timeout) # 设置浏览器加载网页的超时时间
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close() # 释构时关闭浏览器实例

    def process_request(self, request, spider):
        """
        用PhantomJS抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        self.logger.debug(u'启动PhantomJS...')
        # page = request.meta.get('sn', 1)

        try:
            self.browser.get(request.url)

            # 等待页面的宝贝全部加载完成
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))

            return HtmlResponse(url=request.url,
                body=self.browser.page_source,
                request=request,
                encoding='utf-8',
                status=200)

        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request) # 超时抛出异常