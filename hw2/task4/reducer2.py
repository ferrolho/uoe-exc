#!/usr/bin/python3

import sys

best_userId = None
best_answerIds = None
best_answerIdsLength = 0

prev_userId = None
answerIds = set()

for line in sys.stdin:
	userId, ansId = line.strip().split('\t')
	ansId = int(ansId)

	if userId == prev_userId:
		answerIds.add(ansId)
	else:
		if prev_userId:
			if len(answerIds) > best_answerIdsLength:
				best_userId = prev_userId
				best_answerIds = set(answerIds)
				best_answerIdsLength = len(answerIds)

		answerIds.clear()
		answerIds.add(ansId)
		prev_userId = userId

# Don't forget the last line
if userId == prev_userId:
	if len(answerIds) > best_answerIdsLength:
		best_userId = prev_userId
		best_answerIds = set(answerIds)
		best_answerIdsLength = len(answerIds)

print(best_userId, str(sorted(best_answerIds)).strip('[]'), sep='\t')
