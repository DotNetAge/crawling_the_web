# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import FormRequest


class LoginMiddleWare(object):

	def process_request(self,request, spider):
		return FormRequest(url="http://www.example.com/post/action", formdata={'username': 'ray', 'password': 'secret'})

	def process_response(self,request, response, spider):
      if "authentication failed" in response.body:
            return IgnoreRequest()

	def process_exception(self,request, exception, spider):
        self.log("Login failed", level=scrapy.log.ERROR)
