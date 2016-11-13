#!/usr/bin/python3

import sys

def parseRow(xml):
	result = dict()
	tokens = xml.strip().split()
	for token in tokens:
		key_value = token.split('=')
		if len(key_value) == 2:
			key, value = key_value
			if key and value:
				result[key] = value.strip('"')
	return result

for line in sys.stdin:
	row = parseRow(line)
	print(row)
