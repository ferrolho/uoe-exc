#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	tokens = line.split()

	for token in tokens:
		print("{0} {1}".format(len(token), len(line)))
