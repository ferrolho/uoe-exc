#!/usr/bin/python3

import random
import sys

min_line = None

for line in sys.stdin:
	random_num = random.uniform(0, 1)

	if not min_line or random_num < min_line[0]:
		min_line = (random_num, line.strip())

print('{:.50f}\t{}'.format(min_line[0], min_line[1]))
