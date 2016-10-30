#!/usr/bin/python3

import sys

last_studentId = None
name           = None
running_avg    = 0.0
weight         = 0

for line in sys.stdin:
    tokens = line.strip().split()

    tag       = tokens[0]
    studentId = tokens[1]

    if studentId != last_studentId:
        if last_studentId:
            print(last_studentId, name, running_avg, weight, sep='\t')

        last_studentId = studentId
        running_avg    = 0.0
        weight         = 0

    if tag == 'student':
        name = tokens[2]
    else:
        mark         = tokens[3]
        running_avg += float(mark)
        weight      += 1

if last_studentId:
    print(last_studentId, name, running_avg, weight, sep='\t')
