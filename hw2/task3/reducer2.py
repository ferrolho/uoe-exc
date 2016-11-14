#!/usr/bin/python3

import sys

best_userId = None
best_userQuestionIds = None
best_userQuestionIdsLength = 0

for line in sys.stdin:
	userId_userQuestionIds = line.strip().split('\t')

	if len(userId_userQuestionIds) == 2:
		userId, userQuestionIds = userId_userQuestionIds

		if len(userQuestionIds.split(', ')) > best_userQuestionIdsLength:
			best_userId = userId
			best_userQuestionIds = userQuestionIds
			best_userQuestionIdsLength = len(userQuestionIds.split(', '))

print(best_userId, best_userQuestionIds, sep=' -> ')
