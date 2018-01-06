#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from urlparse import urlparse
from bs4 import BeautifulSoup
import argparse
from argparse import RawTextHelpFormatter
from urllib2 import urlopen
from contextlib import closing
import json
#define vars
bing_dork=["site:","-site:","language:","domain:","ip:"]

delete_bing=["microsoft","msn","bing","hostinet"]

""" FUNCTION SENDEQUEST """
#Use Bing to obtain all domains contained in an IP
def SendRequest(ip,num,initial):
	iteration = 0
	count_bing=9
	url_th4sd0m = []
	url_temp = []
	try:
		while (iteration < num):
			iteration = iteration +1
			if initial==True:
				print "\nSearching domains hosted in this IP...\n"
				initial = False
				#First search in Bing
				SearchBing = "https://www.bing.com/search?q="+bing_dork[4]+ip
			else:
				#Bring the next Bing results - 50 in each page
				SearchBing = "https://www.bing.com/search?q="+bing_dork[4]+ip+"&first="+str(count_bing)+"&FORM=PORE"
				count_bing=count_bing+50
				#Use requests to do the search
				response=requests.get(SearchBing,allow_redirects=True)
				url_temp = parser_html(response.text)	
				[url_th4sd0m.append(i) for i in url_temp if not i in url_th4sd0m] 

	except Exception as e:
		print e
		pass

	finally:
		return url_th4sd0m
#********************************************************#
""" FUNCTION PARSER_HTML"""
def parser_html(content):
	urls = []
	urls_clean = []
	urls_final =[]
	i = 0;
	soup = BeautifulSoup(content, 'html.parser')
	#try:
	for link in soup.find_all('a'):
		try:
			if (urlparse(link.get('href'))!='' and urlparse(link.get('href'))[1].strip()!=''):
				urls.append(urlparse(link.get('href'))[1])
		except Exception as e:
			#print(e)
			pass	
	try:
		#Delete duplicates
		[urls_clean.append(i) for i in urls if not i in urls_clean] 
	except:
		pass
	try:
		#Delete not domains belongs to target
		for value in urls_clean:
			if (value.find(delete_bing[0])  == -1):
				#Delete Bing's domains
				if (value.find(delete_bing[1])  == -1):
					if (value.find(delete_bing[2])  == -1):
						urls_final.append(value)
	except:
		pass
	#except Exception as e:
	#	print e,"Failed in parser_HTML of th4sd0m"
	return urls_final