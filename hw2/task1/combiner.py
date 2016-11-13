#!/usr/bin/python3

import sys

term = None
prev_term = None
freq_total = 0

for line in sys.stdin:
	term, doc, freq = line.strip().split('\t')
	freq = int(freq)

	if prev_term == term:
		freq_total += freq
	else:
		if prev_term:
			print(prev_term, doc, freq_total, sep='\t')

		freq_total = freq
		prev_term = term

# Don't forget the last line
if prev_term == term:
	print(prev_term, doc, freq_total, sep='\t')
