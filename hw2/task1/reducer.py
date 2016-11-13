#!/usr/bin/python3

import sys

term = None
prev_term = None
freq_total = 0
docToFreq = dict()

def indexToString(index):
	string = ""

	for i, doc in enumerate(sorted(index)):
		if i > 0: string += ', '
		string += '({}, {})'.format(doc, index[doc])

	return '{' + string + '}'

for line in sys.stdin:
	term, doc, freq = line.strip().split('\t')
	freq = int(freq)

	docToFreq.clear()
	docToFreq[doc] = freq

	if prev_term == term:
		freq_total += freq
	else:
		if prev_term:
			print(prev_term, len(docToFreq), indexToString(docToFreq), sep=' : ')

		freq_total = freq
		prev_term = term

# Don't forget the last line
if prev_term == term:
	print(prev_term, len(docToFreq), indexToString(docToFreq), sep=' : ')
