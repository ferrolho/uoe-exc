#!/usr/bin/python3

import sys

top20 = dict()

def addToTop20(key, value):
	top20[key] = value

	while (len(top20) > 20):
		del top20[min(top20, key=top20.get)]

for line in sys.stdin:
	key, value = line.strip().split('\t')
	value = int(value)
	addToTop20(key, value)

for k, v in top20.items():
	print(k, v, sep='\t')
