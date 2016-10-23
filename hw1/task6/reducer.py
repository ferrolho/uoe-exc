#!/usr/bin/python3

from math import log2
import sys

def parseSequence(seq):
	delimiter = ' '
	groups = seq.split(delimiter)
	return delimiter.join(groups[:2]), delimiter.join(groups[2:])

def printResults():
	for i in range(len(pwcList)):
		pwc = pwcList[i] / count_total
		pwcList[i] = - pwc * log2(pwc)

	entropy = sum(pwcList)
	print(prev_context, entropy)

context = ""
prev_context = ""
count_total = 0
pwcList = []

for line in sys.stdin:
	seq, count = line.strip().split('\t')
	context, follower = parseSequence(seq)
	count = int(count)

	if prev_context == context:
		count_total += count
		pwcList.append(count)
	else:
		if prev_context:
			printResults()

		prev_context = context
		count_total = count
		pwcList = [count]

if prev_context == context:
	printResults()
