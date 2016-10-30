#!/usr/bin/python3

import sys

last_studentId = None
last_name      = None
name   = None
avg    = 0.0
weight = 0

for line in sys.stdin:
    studentId, name, running_avg, count = line.strip().split('\t')

    if studentId != last_studentId:
        if last_studentId and weight > 3:
            print(last_name, avg / weight, sep='\t')

        last_studentId = studentId
        last_name = name
        avg    = 0.0
        weight = 0

    avg    += float(running_avg)
    weight += int(count)

if last_studentId and weight > 3:
    print(last_name, avg / weight, sep='\t')
