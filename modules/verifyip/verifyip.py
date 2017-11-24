#!/usr/bin/env python
#-*- coding:utf-8 -*-

from IPy import IP

def VerifyIp(ip):

	ip_type = None

	try:

		ip_type = IP(ip).iptype()

		if ip_type is not "PUBLIC":

			ip_type = 'Private'

		else:

			ip_type = 'Public'

	except Exception:
		
		pass

	finally:

		return ip_type