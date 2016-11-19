#!/usr/bin/python3

import random
import sys

line_min = None

for line in sys.stdin:
	random_num = random.uniform(0, 1)

	if not line_min or random_num < line_min[1]:
		line_min = (line.strip(), random_num)

print('{}\t{:.50f}'.format(line_min[0], line_min[1]))
