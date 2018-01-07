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
import sys
#imports
from modules.deleteduplicate import *
from modules.whoip import *
from modules.exportresults import *
from modules.showresults import *
from modules.th4sd0m import *
from modules.whois import *
from modules.n4xd0rk import *
from modules.dorkgoo import *
from modules.verifytarget import *
from modules.verifyip import *
from modules.screenshot import *
from modules.sh4d0m import *
""" FUNCTION BANNER """
def banner():
	print """
	   _   _ _  _        _____   ___       _ 
	  | \ | | || |      |  __ \ / _ \     | |
	  |  \| | || |___  _| |  | | | | |_ __| | __
	  | . ` |__   _\ \/ / |  | | | | | '__| |/ /
	  | |\  |  | |  >  <| |__| | |_| | |  |   < 
	  |_| \_|  |_| /_/\_\_____/ \___/|_|  |_|\_\  """
 	print"\n"
	print """
	** Tool to search the subdomains about a domain using the results indexed of Bing search
    ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
    ** DISCLAMER This tool was developed for educational goals. 
    ** The author is not responsible for using to others goals.
    ** A high power, carries a high responsibility!
    ** Version 2.1"""

"""FUNCTION HELP """
def help():
	print  """ \nThis script obtains the IP associated a domain

 			Example of usage: python n4xd0rk.py -d apple.com -n 5 """
def main (argv):
	parser = argparse.ArgumentParser(description='This script searchs the subdomains about a domain using the results indexed of Bing search.', formatter_class=RawTextHelpFormatter)
	parser.add_argument('-t','--target', help="The domain or IP which wants to search.",required=True)
	parser.add_argument('-n','--number', help="Indicate the number of the search which you want to do.",required=True)
	parser.add_argument('-e','--export', help="Export the results to a json file (Y/N)\n Format available:\n\t1.json\n\t2.xlsx", required=False)
	parser.add_argument('-l','--language', help="Indicate the language of the search\n\t(es)-Spanish(default)", required=False)
	parser.add_argument('-c','--capture', help="Indicate if you want to take a screenshot of each web (y/n)", required=False)
	args = parser.parse_args()
	#Asignation from arguments to variables.
	#convertion to int the argument
	N = int (args.number)
	target=args.target
	output= str(args.export)
	output = output.lower()
	capture = args.capture
	if capture is None:
		capture = 'n'
	capture = capture.lower()
	if capture != 'y' and capture != 'n':
		print "The capture is incorrect. Please, enter a valid capture."
		exit (1)
	language = args.language
	if language is None:
		language="es"
	#Local var's
	urls_target =[]
	urls_n4xd0rk = []
	urls_d0rkgo0 = []
	initial = 1 #by n4xd0rk
	option = None
	export = ""
	newlist =[]
	direction_ip = []
	initial = True
	flag = None
	banner()
	help()
	#Verify inputs
	if target == None:
		print "The target is empty. Please, enter a valid target"
	flag = verifytarget.VerifyTarget(target)
	if flag == False:
		option = 1
	if flag == True:
		flag_ip = verifyip.VerifyIp(target)
		if flag_ip == 'Public':
			option = 2
		else:
			print "The IP is not public or ipv4"
			exit(1)
	if output is None:
		output = 'n'
	if (output == 'y'):
		print "Select the output format:"
		print "\n\t(js).json"
		print "\n\t(xl).xlsx"
		export = raw_input ().lower()
		if ((export != "js") and (export != "xl")):
			print "Incorrect output format selected."
			exit(1)
	try:
		if option == 1:
			#BING
			urls_n4xd0rk = n4xd0rk.SendRequest(target,N,1,initial,language) 
			#GOOGLE
			urls_d0rkgo0 = dorkgoo.SearchGoogle(N,target,language)
			#Join Bing and Google and delete duplicate results
			urls_target = deleteduplicate.DeleteDuplicate(urls_n4xd0rk,urls_d0rkgo0)
			if capture == 'y':
				screenshot.screen(urls_target,target)
			for i in urls_target:
				ip = whoip.WhoIP(i)
				direction_ip.append(ip)
		else:
			print "Information about the IP",target+"\n"
			whois.WhoismyIP(target)
			sh4d0m.CreateShodan(target)
			urls_target = th4sd0m.SendRequest(target,N,True)
			if capture == 'y':
				screenshot.screen(urls_target,target)
			try:
				direction_ip.append(str(target))
			except Exception as e:
				#print e
				pass
		#Visuresults showresults
		showresults.ShowResults(urls_target,direction_ip,target,option)
		if (output == 'y'):
			exportresults.ExportResults(urls_target,direction_ip,export)
	except Exception as e:
		print e
		pass

if __name__ == "__main__":
   main(sys.argv[1:])
