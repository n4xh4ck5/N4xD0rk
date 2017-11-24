#!/usr/bin/env python
import socket
"""FUNCTION WHOIP
Obtain the reverse IP about a domain
"""
def WhoIP(domain):
	ip=""
	try:
		ip = socket.gethostbyname(domain)
	except Exception as e:
		#print e
		print "It can't obtain the reverse IP"
		ip = "0.0.0.0"
	return ip