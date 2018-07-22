#!/bin/python
from urllib import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://www.baidu.com')
bs = BeautifulSoup(response.read(),"html.parser")
print bs.title