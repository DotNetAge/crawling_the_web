# coding=utf8

"""
本示例是模拟正常浏览器访问淘宝

1. 先打开首页获取淘宝的Cookie 和 Search的字段
    q - 搜索内容
    imgfile -  为空
    commend - all
    ssid - 动态读取
    search_type = item
    sourceId = tb.index
    spm = 动态读取
    ie=utf8
    initiative_id= 活动分页 要动态读出
2. 向 https://s.taobao.com/search 发起 GET 请求并按从Form读取的内容生成URL
3. 读取 Item
"""

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get("https://s.taobao.com/search?q=Vue2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306")
browser.implicitly_wait(1)


element = browser.find_element_by_id('q')
button = browser.find_element_by_css_selector('form button.btn-search')

print element.get_attribute('name')

