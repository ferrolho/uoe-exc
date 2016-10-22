#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	tokens = line.split()

	for i in range(0, len(tokens) - 2):
		print(tokens[i], tokens[i + 1], tokens[i + 2])
