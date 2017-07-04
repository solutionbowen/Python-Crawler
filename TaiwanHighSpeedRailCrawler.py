#-*- coding: utf-8 -*-
#台灣高鐵時刻表查詢爬蟲(以POST形式+pandas表格輸出)
'''
*
* Author: Paul (bowenduan618@gmail.com)
* Modified: 5/2, 2017
*
'''

import requests
import pandas
from bs4 import BeautifulSoup
payload = {
    'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
    'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
    'SearchDate':'2017/07/04',
    'SearchTime':'18:30',
    'SearchWay':'DepartureInMandarin',
    'RestTime':'',
    'EarlyOrLater':''}

res = requests.post('https://www.thsrc.com.tw/tw/TimeTable/SearchResult', data = payload)
soup = BeautifulSoup(res.text)
dfs = pandas.read_html(res.text)
print(dfs[0])
