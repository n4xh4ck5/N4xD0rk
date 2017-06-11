#!/usr/bin/env python
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
urls = []
urls_clean = []
urls_final =[]
delete_bing=["microsoft","msn","bing"]
direction_ip=[]

""" FUNCTION SENDREQUEST"""
def SendRequest (target,num,option,initial):
	count_bing= 9
	iteration = 0
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
				#SearchBing= SearchBing+"&first="+str(count_bing)+"&FORM=PORE"
					SearchBing = "https://www.bing.com/search?q="+bing_dork[3]+target+"+"+bing_dork[2]+language+"+"+bing_dork[1]+"www."+target+"&first="+str(count_bing)+"&FORM=PORE"
				else:
					SearchBing = "https://www.bing.com/search?q="+bing_dork[4]+target+"&first="+str(count_bing)+"&FORM=PORE"
				count_bing=count_bing+50

			#Requests
			response=requests.get(SearchBing,allow_redirects=True)
			parser_html(response.text)
	except Exception as e:
		print str(e)
		pass

"""FUNCTION PARSER_HTML"""
def parser_html(content):
	i = 0;
	soup = BeautifulSoup(content, 'html.parser')
	for link in soup.find_all('a'):
		try:
			if (urlparse(link.get('href'))!='' and urlparse(link.get('href'))[1].strip()!=''):
				urls.append(urlparse(link.get('href'))[1])
				#print str(urlparse(link.get('href'))[1])
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

"""FUNCTION WHO IS MY IP"""
def WhoismyIP(domain,option):
	ip=""
	url =""
	try:

		if option == 1:
			ip = socket.gethostbyname(domain)
			direction_ip.append(ip)
			return ip
		else:
			url = 'http://freegeoip.net/json/'+domain
			try:
			    with closing(urlopen(url)) as response:
			        location = json.loads(response.read())
			        print location
			        location_city = location['city']
			        location_state = location['region_name']
			        location_country = location['country_name']
			        location_zip = location['zipcode']
			except:
				pass
	except Exception as e:
		print e
		pass

""" FUNCTION SHOW RESULTS """
def ShowResults(target, option):
	newlist=[]
	ip = ""
	if option == 1:
		print "\nSubdomains "+target+" are:"
		#Read the list to print the value in a line
		for i in urls_final:
			if i not in newlist:
				ip=WhoismyIP(i,option)
				newlist.append(i)
				print "\n"
				print "\t- " + i+ " ["+ip+"]"
	else:
		print "Information about the IP",target+"\n"
		WhoismyIP(target,option)
		print "\nDomains contained in the IP "+target+" are:"
		#Read the list to print the value in a line
		for i in urls_final:
			if i not in newlist:
				newlist.append(i)
				print "\n"
				print "\t- " + i
	return newlist

"""FUNCTION EXPORT RESULTS"""
def ExportResults(data,output):
	# Start from the first cell. Rows and columns are zero indexed.
	row = 0
	col = 0
	if output == "js": 
		#Export the results in json format
		print "Exporting the results in an json"
		with open ('output.json','w') as f:
			json.dump(data,f)
	elif (output == "xl"):
		#Export the results in excel format
		print "\nExporting the results in an excel"
		# Create a workbook and add a worksheet.
		workbook = xlsxwriter.Workbook('output.xlsx')
		worksheet = workbook.add_worksheet()
		worksheet.write(row, col, "Domain")
		worksheet.write(row, col+1, "IP")
		row +=1
		for domain in data:
			col = 0
			worksheet.write(row, col, domain)
			row += 1
		#update row
		row = 1
		for ip in direction_ip:
			col = 1
			worksheet.write(row, col, ip)
			row += 1
		#close the excel
		workbook.close()
	else:
		exit(1)
#MAIN
parser = argparse.ArgumentParser(description='This script searchs the subdomains about a domain using the results indexed of Bing search.', formatter_class=RawTextHelpFormatter)
parser.add_argument('-d','--domain', help="The domain which wants to search.",required=False)
parser.add_argument('-i','--ip', help="The IP which to kown the domains to contain.",required=False)
parser.add_argument('-o','--option', help="Select an option:\n\t1. Searching the subdomains about a domain using the results indexed.\n\t2. Searching the domains belong to an IP.",required=True)
parser.add_argument('-n','--search', help="Indicate the number of the search which you want to do.",required=True)
parser.add_argument('-e','--export', help="Export the results to a json file (Y/N)\n Format available:\n\t1.json\n\t2.xlsx", required=False)
parser.add_argument('-l','--language', help="Indicate the language of the search\n\t(es)-Spanish(default)\n\t(en)-English", required=False)
args = parser.parse_args()
print "  _   _ _  _        _____   ___       _"  
print " | \ | | || |      |  __ \ / _ \     | |"
print " |  \| | || |___  _| |  | | | | |_ __| | __"
print " | . ` |__   _\ \/ / |  | | | | | '__| |/ /"
print " | |\  |  | |  >  <| |__| | |_| | |  |   < "
print " |_| \_|  |_| /_/\_\_____/ \___/|_|  |_|\_\ "
print "\n"
print """** Tool to search the subdomains about a domain using the results indexed of Bing search
    ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
    ** DISCLAMER This tool was developed for educational goals. 
    ** The author is not responsible for using to others goals.
    ** A high power, carries a high responsibility!
    ** Version 1.2"""
#Asignation from arguments to variables.
#convertion to int the argument
N = int (args.search)
option = int (args.option)
target=args.domain
ip = args.ip
output=args.export
export = ""
newlist =[]
initial = True
if ((option != 1) and (option != 2)):
	print "The option is incorrect"
	exit(1)
if option == 1:
	#Analyze if domain has got a domain
	if target is None:
		print "You don't enter a value to domain parameter to option 1"
		exit (1)
elif option == 2:
	if ip is None:
		print "You don't enter a value to ip parameter to option 2"
		exit (1)
if output is None:
	output = 'N'
if ((output == 'y') or (output == 'Y')):
	print "Select the output format:"
	print "\n\t(js).json"
	print "\n\t(xl).xlsx"
	export = raw_input ()
	if ((export != "js") and (export != "xl")):
		print "Incorrect output format selected."
		exit(1)
language= args.language
if language is None:
	language="es"
if ((language != "es") and (language !="en")):
	print "The language is not valid"
	exit(1)
try:
	if option ==1:
		content = SendRequest(target,N,option,initial)	
		newlist = ShowResults (target,option)
	else:
	# option == 2:
		content = SendRequest(ip,N,option,initial)
		newlist = ShowResults (ip,option)
except:
	pass
#verify if the user wants to export results
if ((output == 'Y') or (output =='y')):
		#Only it can enter if -e is put in the execution
	ExportResults(newlist,export)