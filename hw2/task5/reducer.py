#!/usr/bin/python3

import sys

for i, line in enumerate(sys.stdin):
	if i < 1:
		__, line = line.strip().split('\t')
		print(line)
