#!/usr/bin/python

import sys

seen = set()

for line in sys.stdin:
	if line not in seen:
		seen.add(line)
		sys.stdout.write(line)
