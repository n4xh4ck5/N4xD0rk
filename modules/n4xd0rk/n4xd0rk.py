#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from urlparse import urlparse
from bs4 import BeautifulSoup
import argparse
from argparse import RawTextHelpFormatter
import json
import xlsxwriter
import socket
from urllib2 import urlopen
from contextlib import closing

#define vars
bing_dork=["site:","-site:","language:","domain:","ip:"]
delete_bing=["microsoft","msn","bing","hostinet"]

""" FUNCTION SENDREQUEST"""
def SendRequest (target,num,option,initial,language):
	count_bing= 9
	iteration = 0
	url_final_temp= []
	url_final_n4xd0rk = []
	response =""
	try:
		while (iteration < num):
			iteration += 1
			if initial == True:
				initial = False
				#First search in Bing
				if option == 1:
					SearchBing = "https://www.bing.com/search?q="+bing_dork[3]+target+"+"+bing_dork[2]+language+"+"+bing_dork[1]+"www."+target
				else:
					SearchBing = "https://www.bing.com/search?q="+bing_dork[4]+target+"&go=Buscar"
			else:
				if option == 1:
					SearchBing = "https://www.bing.com/search?q="+bing_dork[3]+target+"+"+bing_dork[2]+language+"+"+bing_dork[1]+"www."+target+"&first="+str(count_bing)+"&FORM=PORE"
				else:
					SearchBing = "https://www.bing.com/search?q="+bing_dork[4]+target+"&first="+str(count_bing)+"&FORM=PORE"
				count_bing=count_bing+50

			#Requests
			response=requests.get(SearchBing,allow_redirects=True)
			url_final_temp= parser_html(response.text)
			[url_final_n4xd0rk.append(i) for i in url_final_temp if not i in url_final_n4xd0rk] 

	except Exception as e:
		print str(e)
		pass

	finally:
		return url_final_n4xd0rk

"""FUNCTION PARSER_HTML"""
def parser_html(content):
	urls = []
	urls_clean = []
	urls_final =[]
	i = 0;
	soup = BeautifulSoup(content, 'html.parser')
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
						if (value.find(delete_bing[3])  == -1):
							urls_final.append(value)
	except:
		pass
	return  urls_final