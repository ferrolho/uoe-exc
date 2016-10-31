#!/usr/bin/python3

import sys

best_avg = None

for line in sys.stdin:
    name, avg = line.strip().split('\t')
    avg = float(avg)

    if not best_avg:
    	best_avg = avg
    
    if avg == best_avg:
    	print(name, avg, sep='\t')
