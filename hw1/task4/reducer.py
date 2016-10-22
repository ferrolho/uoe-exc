#!/usr/bin/python3

import sys

line = ""
prev_line = ""
count_total = 0

for line in sys.stdin:
	line, count = line.strip().split('\t')
	count = int(count)

	if prev_line == line:
		count_total += count
	else:
		if prev_line:
			print(prev_line, count_total, sep='\t')

		count_total = count
		prev_line = line

# Don't forget the last line
if prev_line == line:
	print(prev_line, count_total, sep='\t')
