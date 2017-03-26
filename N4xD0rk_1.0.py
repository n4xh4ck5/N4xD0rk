import requests
from urlparse import urlparse
from bs4 import BeautifulSoup
import argparse
from argparse import RawTextHelpFormatter
import json
#define vars
bing_dork=["site:","-site:","language:","domain:"]
urls = []
urls_clean = []
urls_final =[]
delete_bing=["microsoft","msn","bing"]
count_bing=9
iteration=0
initial=1

#********************************************************#
#Definition and treatment of the parameters
def parser_html():
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
						urls_final.append(value)
	except:
		pass
######FUNCTION EXPORT RESULTS #######
def ExportResults(data):
	#Export the results in json format
	with open ('output.json','w') as f:
		json.dump(data,f)
#MAIN
parser = argparse.ArgumentParser(description='This script searchs the subdominios about a domain using the results indexed of Bing search', formatter_class=RawTextHelpFormatter)
parser.add_argument('-d','--domain', help="The domain which it wants to search",required=False)
parser.add_argument('-n','--search', help="Indicate the number of the search which you want to do",required=True)
parser.add_argument('-e','--export', help='Export the results to a json file (Y/N)\n\n', required=False)
parser.add_argument('-l','--language', help='indiate the language of the search\n\n\t(es)-Spanish(default)\n\t(en)-English', required=False)
args = parser.parse_args()
print " _   _ _  _        _____   ___       _"  
print " | \ | | || |      |  __ \ / _ \     | |"
print " |  \| | || |___  _| |  | | | | |_ __| | __"
print " | . ` |__   _\ \/ / |  | | | | | '__| |/ /"
print " | |\  |  | |  >  <| |__| | |_| | |  |   < "
print " |_| \_|  |_| /_/\_\_____/ \___/|_|  |_|\_\ "
print "\n"
print """** Tool to search the subdominios about a domain using the results indexed of Bing search
    ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
    ** DISCLAMER This tool was developed for educational goals. 
    ** The author is not responsible for using to others goals.
    ** A high power, carries a high responsibility!"""
#Asignation from arguments to variables.
#convertion to int the argument
N = int (args.search)
target=args.domain
output=args.export
if ((output != 'Y') and (output != 'N')):
	print "The output option is not valid"
	exit(1)
language= args.language
if language is None:
	language="es"
if ((language != "es") and (language !="en")):
	print "The language is not valid"
	exit(1)
try:
	while (iteration < N):
		iteration = iteration +1
		if initial==1:
			print "\nSearching subdomains...\n"
			initial = 0
			#First search in Bing
			SearchBing = "https://www.bing.com/search?q="+bing_dork[3]+target+"+"+bing_dork[2]+language+"+"+bing_dork[1]+"www."+target+"&go=Buscar"
		else:
			#Bring the next Bing results - 50 in each page
			SearchBing= SearchBing+"&first="+str(count_bing)+"&FORM=PORE"
			count_bing=count_bing+50
		try:
			#Requests
			response=requests.get(SearchBing,allow_redirects=True)
				
		except:
			pass
		content = response.text
		#PARSER HTML
		#normalize a called with parameters
		parser_html()	
except:
	pass
newlist=[]
print "Subdomains "+target+" are:\n"
#Read the list to print the value in a line
for i in urls_final:
	if i not in newlist:
		newlist.append(i)
		print "\n"
		print i	
#verify if the user wants to export results
if output == 'Y':
		#Only it can enter if -j is put in the execution
	ExportResults(newlist)