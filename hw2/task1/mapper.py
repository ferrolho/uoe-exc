#!/usr/bin/python3

import os
import sys

input_file_path = os.environ["mapreduce_map_input_file"]
doc = input_file_path.rsplit('/', 1)[-1]

for line in sys.stdin:
	terms = line.strip().split()
	
	for term in terms:
		print(term, doc, 1, sep='\t')
