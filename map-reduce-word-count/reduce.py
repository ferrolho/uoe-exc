#!/usr/bin/python3
import fileinput

key, count = None, 0

for line in fileinput.input():
	key2, count2 = line.strip().split('\t')
	count2 = int(count2)

	if key2 != key:
		if key:
			print(key, count, sep='\t')
		key, count = key2, count2
	else:
		count += count2

if key:
	print(key, count, sep='\t')
