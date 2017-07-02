#######################
###crawler sample.py###
#######################

# -*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup as bs

sample_url = "http://yibian.hopto.org/diag/ill/?illno=1"

def mycrawler(source):
	page = requests.get(source)
	page.encoding = 'big5'
	f = open('output.html', 'w')
	f.write(str(bs(page.content, 'html.parser')))
	f.close()

if __name__ == '__main__':
	mycrawler(sample_url)
