#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import re
reload(sys)  
sys.setdefaultencoding('utf8')
import urllib2

url = 'https://maria.deadbsd.org/api/random'
tmp = ""
while ("castor" not in tmp):
	try:
		response = urllib2.urlopen(url)
	except urllib2.URLError, e:
			print("There was an error: %r" % e)
			sys.exit(0)
	values = json.loads(response.read())
	try:
		tmp = values['message']['text']
	except:
		print("No results found")
		sys.exit(0)
	tmp = re.sub("homem","castor",tmp, flags=re.I)
	tmp = re.sub("senhoras ","castoras ",tmp, flags=re.I)
	tmp = re.sub("senhora ","castora ",tmp, flags=re.I)
	tmp = re.sub("senhoras","castoras",tmp, flags=re.I)
	tmp = re.sub("senhora","castora",tmp, flags=re.I)
	tmp = re.sub("mulheres ","castoras ",tmp, flags=re.I)
	tmp = re.sub("senhor ","castor ",tmp, flags=re.I)
	tmp = re.sub("jovem rapaz","jovem castor",tmp, flags=re.I)
	tmp = re.sub("rapaz","castor",tmp, flags=re.I)
	tmp = re.sub("cavalheiro","castor",tmp, flags=re.I)
	tmp = re.sub("jovem","castor",tmp, flags=re.I)
	tmp = re.sub("quarentao","castor",tmp, flags=re.I)
	tmp = re.sub("antonio","castor",tmp, flags=re.I)
	tmp = re.sub("paulo","castor",tmp, flags=re.I)
	tmp = re.sub("sou h","castor",tmp, flags=re.I)
	tmp = re.sub("rapariga","castora",tmp, flags=re.I)
	tmp = re.sub("mulher","castora",tmp, flags=re.I)
	tmp = re.sub("menina","castora",tmp, flags=re.I)
print("%s" % (tmp))