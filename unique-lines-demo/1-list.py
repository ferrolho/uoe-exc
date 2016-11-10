#!/usr/bin/python

import sys

seen = []

for line in sys.stdin:
	if line not in seen:
		seen.append(line)
		sys.stdout.write(line)
