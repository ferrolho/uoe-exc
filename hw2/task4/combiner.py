#!/usr/bin/python3

import sys

prev_id = None

for line in sys.stdin:
	tokens = line.strip().split('\t')

	id = tokens[0]

	if id == prev_id:
		userId = tokens[1]
		print(id), print(id, userId, sep='\t')
	else:
		prev_id = id
