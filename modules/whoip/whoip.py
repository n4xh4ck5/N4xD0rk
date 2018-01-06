#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
"""FUNCTION WHOIP
Obtain the reverse IP about a domain
"""
def WhoIP(domain):
	ip=""
	try:
		ip = socket.gethostbyname(domain)
	except:
		#print "It can't obtain the reverse IP"
		ip = "0.0.0.0"

	finally:
		return ip