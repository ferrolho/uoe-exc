#!/usr/bin/python3

import sys

for i, line in enumerate(sys.stdin):
	if i < 10:
		count, id = line.strip().split('\t')
		print(count, id)
