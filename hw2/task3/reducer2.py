#!/usr/bin/python3

import sys

best_userId = None
best_userQuestionIds = None
best_userQuestionIdsLength = 0

prev_userId = None
userQuestionIds = set()

for line in sys.stdin:
	userId_userQuestionIds = line.strip().split('\t')

	if len(userId_userQuestionIds) == 2:
		userId, userQuestionIdsStr = userId_userQuestionIds

		if userId == prev_userId:
			userQuestionIds.update(list(map(int, userQuestionIdsStr.split(', '))))
		else:
			if prev_userId:
				if len(userQuestionIds) > best_userQuestionIdsLength:
					best_userId = prev_userId
					best_userQuestionIds = set(userQuestionIds)
					best_userQuestionIdsLength = len(userQuestionIds)

			userQuestionIds.clear()
			userQuestionIds.update(list(map(int, userQuestionIdsStr.split(', '))))
			prev_userId = userId

# Don't forget the last line
if userId == prev_userId:
	if len(userQuestionIds) > best_userQuestionIdsLength:
		best_userId = prev_userId
		best_userQuestionIds = set(userQuestionIds)
		best_userQuestionIdsLength = len(userQuestionIds)

print(best_userId, str(sorted(best_userQuestionIds)).strip('[]'), sep=' -> ')
