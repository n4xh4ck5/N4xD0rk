# -*- coding: utf-8 -*-
#!/usr/bin/env python

from selenium import webdriver
import requests
import os

def screen(array,target):
	dom =""
	createDir(target)
	try:
		for dom in array:
			snapshot(str(dom.encode("utf-8")))
		MoveCaptures(target)

	except Exception as e:
		print e

def snapshot(url):
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true']) # or add to your PATH
	driver.set_page_load_timeout(15)
	driver.set_window_size(1024, 768) # optional
	try:
		driver.get('https://{0}'.format(url)) 
	except:
		driver.get('http://{0}'.format(url))
	driver.save_screenshot(url+".png")
	return

def createDir(target):
	try:
		if not os.path.exists(target):
			os.mkdir(target)

	except Exception as e:
		print e

def MoveCaptures(target):
	os.system('mv *.png '+ str(target))