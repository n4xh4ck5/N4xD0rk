# -*- coding: utf-8 -*-
#!/usr/bin/env python
from selenium import webdriver
import requests
import os

def screen(array):
	for dom in array:
		try:
			doAll(str(dom.encode("utf-8")))
		except Exception as e:
			print "{0} Failed: {1}".format(dom, e)
			continue
def __snapshot__(url):
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true']) # or add to your PATH
	driver.set_page_load_timeout(10)
	driver.set_window_size(1024, 768) # optional
	try:
		driver.get('https://{0}'.format(url)) 
	except:
		driver.get('http://{0}'.format(url))
	driver.save_screenshot('{0}/{0}-image.png'.format(url,url))
	return

def __createDir__(url):
	if not os.path.exists(url):
		os.mkdir(url)
	return

def doAll(url):
	__createDir__(url)
	__snapshot__(url)
	return
