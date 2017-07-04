#-*- coding: utf-8 -*-
#博客來書局文學小說爬蟲(書名，作者，優惠價)
'''
*
* Author: Paul (bowenduan618@gmail.com)
* Modified: 5/2, 2017
*
'''

import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.books.com.tw/web/books_topm_01/?loc=P_017_001')
soup = BeautifulSoup(res.text)
for BDList in soup.select('.box'):
    print(BDList.text)
    