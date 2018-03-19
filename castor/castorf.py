#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import re
reload(sys)  
sys.setdefaultencoding('utf8')
import urllib2

if (len(sys.argv) == 1):
	print("Usage .castorf <text>")
	sys.exit(0)
text = sys.argv[1]
try:
	pos = sys.argv[2]
except:
	pos = 0

tmp = ""
count = 0
while ("castor" not in tmp):
	pos = int(pos)+count
	url = 'https://maria.deadbsd.org/api/find?text={}&position={}'.format(text, pos)
	try:
		response = urllib2.urlopen(url)
	except urllib2.URLError, e:
			print("There was an error: %r" % e)
			sys.exit(0)
	values = json.loads(response.read())
	try:
		tmp = values['message']['text']
		datetime = values['message']['datetime']
		number = values['message']['number']
		total = values['total']
		nextfind = values['next']	
	except:
		print("No results found")
		sys.exit(0)
	tmp = re.sub("homem","castor",tmp, flags=re.I)
	tmp = re.sub("homen","castor",tmp, flags=re.I)
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
	tmp = re.sub("cinquentona","castora",tmp, flags=re.I)
	tmp = re.sub("antonio","castor",tmp, flags=re.I)
	tmp = re.sub("paulo","castor",tmp, flags=re.I)
	tmp = re.sub("sou h","castor",tmp, flags=re.I)
	tmp = re.sub("rapariga","castora",tmp, flags=re.I)
	tmp = re.sub("mulher","castora",tmp, flags=re.I)
	tmp = re.sub("menina","castora",tmp, flags=re.I)
	count += 1
print("%d found '.castorf %s %s' for the next one" % (total, text, nextfind))
print("%s - %s, %s " % (tmp, number, datetime))