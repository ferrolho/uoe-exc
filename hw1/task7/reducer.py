#!/usr/bin/python3

import sys

last_studentId = None

for line in sys.stdin:
	tokens = line.strip().split()

	tag       = tokens[0]
	studentId = tokens[1]

	if last_studentId and studentId != last_studentId:
		print()
	last_studentId = studentId

	if tag == 'student':
		name = tokens[2]
		print(name, '-->', end='')
	else:
		courseId = tokens[2]
		mark     = tokens[3]
		print(' ({0}, {1}) '.format(courseId, mark), end='')

print()
