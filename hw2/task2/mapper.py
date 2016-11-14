#!/usr/bin/python

from __future__ import print_function
from heapq import heappush, heappushpop
import sys
import xml.etree.ElementTree as ET

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def postIsQuestion(post):
	return post['PostTypeId'] == '1'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

top10 = []

for line in sys.stdin:
	post = ET.fromstring(line).attrib

	if postIsQuestion(post):
		count = int(post['ViewCount'])

		if len(top10) < 10:
			heappush(top10, (count, post['Id']))
		else:
			heappushpop(top10, (count, post['Id']))

for count, id in top10:
	print(count, id, sep='\t')
