#!/usr/bin/python3

from collections import defaultdict
import sys

term = None
prev_term = None
docToFreq = defaultdict(int)

def indexToString(index):
	string = ""

	for i, doc in enumerate(sorted(index)):
		if i > 0: string += ', '
		string += '({}, {})'.format(doc, index[doc])

	return '{' + string + '}'

for line in sys.stdin:
	term, doc, freq = line.strip().split('\t')
	freq = int(freq)

	if prev_term == term:
		docToFreq[doc] += freq
	else:
		if prev_term:
			print(prev_term, len(docToFreq), indexToString(docToFreq), sep=' : ')

		docToFreq.clear()
		docToFreq[doc] = freq
		prev_term = term

# Don't forget the last line
if prev_term == term:
	print(prev_term, len(docToFreq), indexToString(docToFreq), sep=' : ')
