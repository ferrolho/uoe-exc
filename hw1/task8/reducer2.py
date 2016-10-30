#!/usr/bin/python3

import sys

best_avg = 0
best_names = []

for line in sys.stdin:
	name, avg = line.strip().split()
	avg = float(avg)

	if avg > best_avg:
		best_avg = avg
		del best_names[:]
		best_names.append(name)
	elif avg == best_avg:
		best_names.append(name)

for name in best_names:
	print(name)
