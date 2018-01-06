#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib2 import urlopen
from contextlib import closing
import json

"""FUNCTION WhoISMYIP"""
def WhoismyIP(ip):
	url =""
	url = 'http://freegeoip.net/json/'+ip
	try:
	    with closing(urlopen(url)) as response:
	        location = json.loads(response.read())
        	print "\n\t-Direction IP:", location['ip']
        	print "\n\t-Country_code:",location['country_code']
        	print "\n\t-Country name:",location['country_name']
        	print "\n\t-Region code:",location['region_code']
        	print "\n\t-Region name:",location['region_name']
        	print "\n\t-City:",location['city']
        	print "\n\t-Zip code:",location['zip_code']
        	print "\n\t-Time zone:",location['time_zone']
        	print "\n\t-Latitude:",location['latitude']
        	print "\n\t-Longitude:",location['longitude']
	except Exception as e:
		#print e
		print "Don't find any information about IP in Whois"
		pass