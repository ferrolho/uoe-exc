#!/usr/bin/python

from __future__ import print_function
from heapq import heappush, heappushpop
import sys

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def parsePost(xml):
	tokens = xml.strip().split()
	result = dict()

	for token in tokens:
		key_value = token.split('=')
		if len(key_value) == 2:
			key, value = key_value
			if key and value:
				result[key] = value.strip('"')

	return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def postIsQuestion(post):
	return post['PostTypeId'] == '1'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

top10 = []

for line in sys.stdin:
	post = parsePost(line)

	if postIsQuestion(post):
		count = int(post['ViewCount'])

		if len(top10) < 10:
			heappush(top10, (count, post['Id']))
		else:
			heappushpop(top10, (count, post['Id']))

for count, id in top10:
	print(count, id, sep='\t')
