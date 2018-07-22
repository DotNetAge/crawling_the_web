from bs4 import UnicodeDammit

dammit = UnicodeDammit("\u4e2d\u56fd\u5c06\u8c03\u6574\u90e8\u5206\u6d88\u8d39\u54c1\u8fdb\u53e3\u5173\u7a0e 12\u67081\u65e5\u8d77\u5b9e\u65bd",['utf8'])
print(dammit.unicode_markup)
print(dammit.original_encoding)
