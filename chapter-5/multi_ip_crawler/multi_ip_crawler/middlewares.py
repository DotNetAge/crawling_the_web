# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from stem import Signal
from stem.control import Controller

class TorProxyMiddleware(object):

    def __init__(self, http_proxy=None, tor_control_port=None, tor_password=None):

        if not http_proxy:
            raise Exception('http proxy setting should not be empty')

        if not tor_control_port:
            raise Exception('tor control port setting should not be empty')

        if not tor_password:
            raise Exception('tor password setting should not be empty')

        self.http_proxy = http_proxy
        self.tor_control_port = tor_control_port
        self.tor_password = tor_password
        self.count = 1
        self.times = 50

    @classmethod
    def from_crawler(cls, crawler):
        http_proxy = crawler.settings.get('HTTP_PROXY')
        tor_control_port = crawler.settings.get('TOR_CONTROL_PORT')
        tor_password = crawler.settings.get('TOR_PASSWORD')

        return cls(http_proxy, tor_control_port, tor_password)

    def process_request(self, request, spider):
        self.count = (self.count + 1) % self.times
        if not self.count:
            # access tor ControlPort to signal tor get a new IP
            with Controller.from_port(port=self.tor_control_port) as controller:
                controller.authenticate(password=self.tor_password)
                controller.signal(Signal.NEWNYM)

        # scrapy support http proxy
        request.meta['proxy'] = self.http_proxy
