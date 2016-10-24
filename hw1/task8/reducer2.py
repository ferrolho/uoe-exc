#!/usr/bin/python3

import sys

best_avg = 0
best_name = None

for line in sys.stdin:
	name, avg = line.strip().split()
	avg = float(avg)

	if avg > best_avg:
		best_avg = avg
		best_name = name

print(best_name)
