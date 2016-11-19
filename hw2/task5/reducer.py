#!/usr/bin/python3

import random
import sys

line_min = None

for line in sys.stdin:
	line, val = line.strip().split('\t')
	val = float(val)

	if not line_min or val < line_min[1]:
		line_min = (line, val)

print(line_min[0])
