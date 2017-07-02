#######################
###  bs sample.py   ###
#######################

# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs




def mysoup(filepath):
	f = open(filepath, 'r')
	soup = bs(f, 'html.parser')
	print(soup.prettify())
	return soup

if __name__ == '__main__':
	soup = mysoup('output.html')