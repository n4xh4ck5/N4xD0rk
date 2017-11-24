#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import socket
# IP -> True
#Domain -> False
def VerifyTarget(target):

	match = False

	try:

		if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', target):

			match = True

		elif re.match(r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\.[a-zA-Z]{2,3})$', target):

			match = False

		else:

			match = None

	except Exception:
		pass

	finally:

		return match