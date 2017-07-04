#-*- coding: utf-8 -*-
#PTT棒球版爬蟲(標題，日期，作者)
'''
*
* Author: Paul (bowenduan618@gmail.com)
* Modified: 5/2, 2017
*
'''

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.ptt.cc/bbs/Baseball/index.html', verify = False)
soup = BeautifulSoup(res.text)
for entry in soup.select('.r-ent'):
    print(entry.select('.title')[0].text,entry.select('.date')[0].text,entry.select('.author')[0].text)