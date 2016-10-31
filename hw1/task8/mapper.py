#!/usr/bin/python3

import re
import sys

for line in sys.stdin:
    tokens = line.strip().split(' --> ')

    if len(tokens) > 1:
        name       = tokens[0]
        pairs_list = tokens[1].split('  ')

        avg = 0.0

        for pair in pairs_list:
            grade = re.search(',(.*)\)', pair).group(1)
            avg  += float(grade)

        if len(pairs_list) > 3:
            print(name, avg / len(pairs_list), sep='\t')
