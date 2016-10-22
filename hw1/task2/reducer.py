#!/usr/bin/python3

import sys

prev_line = ""
line = ""
line_occurrences = 1

for line in sys.stdin:
	line = line.strip()

	if prev_line == line:
		line_occurrences += 1
	else:
		if prev_line and line_occurrences == 1:
			print(prev_line)

		line_occurrences = 1
		prev_line = line

# Don't forget the last line
if prev_line == line and line_occurrences == 1:
	print(prev_line)
