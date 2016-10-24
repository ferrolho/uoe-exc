#!/usr/bin/python3

import sys

for i, line in enumerate(sys.stdin):
	if i < 20:
		k, v = line.strip().split('\t')
		print(v, k, sep='\t')
