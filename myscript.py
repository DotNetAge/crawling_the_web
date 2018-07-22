#!bin/python
from bs4 import BeautifulSoup
from urllib import urlopen

html = BeautifulSoup(urlopen('http://www.baidu.com'),"lxml")
print html.title