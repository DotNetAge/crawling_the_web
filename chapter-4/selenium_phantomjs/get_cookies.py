# coding=utf8

"""
你可以对任意网站（本例用的是 http://www.taobao.com）调用 webdriver 的 get_cookies()方法来查看 cookie：
"""

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get("http://www.taobao.com")
browser.implicitly_wait(1)

print browser.get_cookies()


