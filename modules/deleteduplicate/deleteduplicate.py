#!/usr/bin/env python
# -*- coding: utf-8 -*-

def DeleteDuplicate(data1,data2):
	#va's local
	ss=[]
	fs=[]
	urls_union=[]
	#Use the function set to work with arrays
	try:
		ss=set(data1)
		fs=set (data2)
		#Select the only values in both arrays
		urls_union = ss.union(fs)
	except Exception as e:
		print e

	finally:
		return urls_union