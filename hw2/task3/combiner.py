#!/usr/bin/python3

import sys

prev_userId = None
prev_questionId = None

for line in sys.stdin:
	userId, questionId = line.strip().split()

	if userId != prev_userId or questionId != prev_questionId:
		print(userId, questionId, sep='\t')

	prev_userId = userId
	prev_questionId = questionId
