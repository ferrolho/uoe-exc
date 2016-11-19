#!/usr/bin/python3

from collections import defaultdict
import random
import sys

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def runResevoir():
	line_number = 0
	resevoir    = None
	
	f = open('input.in')
	for line in f:
		if random.randint(0, line_number) == 0:
			resevoir = line.strip()
		line_number += 1
	f.close()

	return resevoir

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

histogram = defaultdict(int)

jobs = 200000
for i in range(jobs):
	print(round(100 * i / jobs), end=' %\r')
	histogram[runResevoir()] += 1
print('Done.')

for k, v in sorted(histogram.items()):
	print(k, v)
