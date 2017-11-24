#!/usr/bin/env python
def ShowResults(urls,array_ip,target, option):
	newlist=[]
	ip = ""
	contador = 0
	try:
		if option == 1:
			print "\n Domains and subdomains of "+ str(target) + " are:"
			#Read the list to print the value in a line
			for i in urls:
				ip = array_ip[contador]
				print "\n"
				print "\t- " + i+ " ["+ip+"]"
				contador += 1
		if option == 2:
			print "\nDomains contained in the IP "+ str(target) + " are:"
			#print "\nDomains contained in the IP {} {} are:".format(target,target)
			#Read the list to print the value in a line
			for i in urls:
				if i not in newlist:
					newlist.append(i)
					print "\n"
					print "\t- " + i
	except Exception as e:
		print e
		pass