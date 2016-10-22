#!/usr/bin/python3

import sys

longest_word_len = 0
longest_line_len = 0

for line in sys.stdin:
	pair = line.split()

	word_len = int(pair[0])
	line_len = int(pair[1])

	if word_len > longest_word_len:
		longest_word_len = word_len

	if line_len > longest_line_len:
		longest_line_len = line_len

print(longest_word_len, longest_line_len, sep='\t')
