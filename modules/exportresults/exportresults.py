#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlsxwriter
import json
def ExportResults(data,array_ip,output):
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
		for ip in array_ip:
			col = 1
			worksheet.write(row, col, ip)
			row += 1
		#close the excel
		workbook.close()
	else:
		exit(1)