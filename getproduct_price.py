from bs4 import BeautifulSoup


html = BeautifulSoup(open('index.html').read(),'lxml')
products = []

for ele in html.select("article"):
    _name = ele.header.text
    # _value =int(ele.find("p", class_="price").find("span").find_next("span").text)
    _value =int(ele.select_one('p.price > span:nth-of-type(2)').text)
    products.append((_name,_value))

print products