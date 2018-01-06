#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib2
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#Disable warning by SSL certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#Libraries to export results
import xlsxwriter
import json
from urlparse import urlparse
from bs4 import BeautifulSoup
import optparse
#Parser arguments
import argparse
from argparse import RawTextHelpFormatter
import socket
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re #Expression regular to parse Google with Beautifoul Soup
#define global vars
url_google =[]

""" FUNCTION DELETE DUPLICATES """

def DeleteDuplicate(data):
	urls_union = []
	for i in data:
		if i not in urls_union:
			urls_union.append(i)
	return urls_union

def SearchGoogle(num,target,language):
	start_page = 0
	nlink = ""
	user_agent = {'User-agent': 'Mozilla/5.0'}
	nlink_clean = ""
	response =""
	soup = ""
	raw_links = ""
	url_google_final =[]
	#Split the target in domain and extension
	domain = target.split(".")[0]
	extension = target.split(".")[1]
	
	print "\nLooking domains and subdomains of target",target
	for start in range(start_page, (start_page + num)):
		SearchGoogle = "https://www.google.com/search?q=(site:*."+target+"+OR+site:*"+target+"+OR+site:"+domain+"*."+extension+")+-site:www."+target+"&lr=lang_="+language+"&filter=&num=100"

	try:
		response = requests.get(SearchGoogle, headers = user_agent)
	except requests.exceptions.RequestException as e:
		print "\nError connection to server!" 
		pass	
	except requests.exceptions.ConnectTimeout as e:
		print "\nError Timeout" #,target
		pass
	try:
		#Parser HTML of BeautifulSoup
		soup = BeautifulSoup(response.text, "html.parser")
		if response.text.find("Our systems have detected unusual traffic") != -1:
			print "CAPTCHA detected - Plata or captcha !!!Maybe try form another IP..."
			return True
		#Parser url's throught regular expression
		raw_links = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
		#print raw_links
		for link in raw_links:
			#Cache Google
			if link["href"].find("webcache.googleusercontent.com") == -1:
				nlink = link["href"].replace("/url?q=","")
			#Parser links
			nlink = re.sub(r'&sa=.*', "", nlink)
			nlink = urllib2.unquote(nlink).decode('utf8')
			nlink_clean = nlink.split("//")[-1].split("/")[0]
			url_google.append(nlink_clean)
			url_google_final =DeleteDuplicate(url_google)
			return url_google_final
	except Exception as e:
		print e
	if len(raw_links) < 2:
		#Verify if Google's Captcha has caught us!
		print "No more results!!!"
		#captcha = True
		return True
	else:
		return False