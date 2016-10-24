#!/usr/bin/python3

import sys

def processStudent():
	global best_avg, best_name

	if len(course_grades) > 3:
		avg = sum(course_grades) / len(course_grades)
		if avg > best_avg:
			best_avg = avg
			best_name = name

	del course_grades[:]

## Globals ##

last_studentId = None
name = None

best_avg  = 0
best_name = None

course_grades = []

for line in sys.stdin:
	tokens = line.strip().split()

	tag       = tokens[0]
	studentId = tokens[1]

	if last_studentId and studentId != last_studentId:
		processStudent()

	last_studentId = studentId

	if tag == 'student':
		name = tokens[2]
	else:
		mark = tokens[3]
		course_grades.append(int(mark))

processStudent()

print(best_name, best_avg)
