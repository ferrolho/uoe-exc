#!/usr/bin/python3

import re
import sys

for line in sys.stdin:
    name, pairs_list = line.strip().split(' --> ')
    pairs_list = pairs_list.split('  ');

    avg = 0.0

    for pair in pairs_list:
        grade = re.search(',(.*)\)', pair).group(1)
        avg  += float(grade)

    if len(pairs_list) > 3:
        print(name, avg / len(pairs_list), sep='\t')
