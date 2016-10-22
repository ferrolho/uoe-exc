#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	tokens = line.split()

	for token in tokens:
		print(len(token), len(line))
