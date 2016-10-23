#!/usr/bin/python3

import sys

for line in sys.stdin:
	value, key = line.strip().split('\t')

	print(key, value, sep='\t')
