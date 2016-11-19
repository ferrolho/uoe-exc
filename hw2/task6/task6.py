#!/usr/bin/python3

import random
import sys

# No. of lines to be sampled - k < n
k = 100

# The reservoir
reservoir = []

# Fill initial reservoir
for i in range(k):
	reservoir.append(sys.stdin.readline().strip())

# Initialize no. of lines read so far
line_number = k

for line in sys.stdin:
	# Generate random no. between [0, no. of lines read so far]
	i = random.randint(0, line_number)

	# If the random no. is a valid index for the reservoir
	if i < k:
		# Save current line to that reservoir position
		reservoir[i] = line.strip()

	# Update no. of lines read so far
	line_number += 1

# Print samples (final reservoir)
for line in reservoir:
	print(line)
