#!/usr/bin/python3

from bitarray import bitarray
import math
import sys

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# False positive rate
FPR = 0.01

# Globals
filter = None
k = None
m = None

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def doubleHash(i, key, m):
	return (hash(key) + i * hash(key)) % m

def filterPos(i, key):
	return doubleHash(i, key, m)

# Adds key to the set
def insert(key):
	for i in range(k):
		filter[filterPos(i, key)] = 1

# If key is *definitely not* in the set, return 'False'.
# Returning 'True' means it *may be* or not in the set - do costly check.
def query(key):
	for i in range(k):
		if not filter[filterPos(i, key)]:
			return False
	return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if len(sys.argv) < 2:

	eprint('Error: not enough arguments')
	eprint('Usage:', sys.argv[0], 'N')
	eprint('  N - Total number of lines in the input file')

else:

	# Elements to be inserted in the filter
	n = int(sys.argv[1])

	# Bits per key
	bitsPerKey = math.ceil(- math.log2(FPR) / math.log(2))

	# Bits in filter
	m = n * bitsPerKey

	# Create the bitarray
	filter = bitarray(m)
	filter.setall(0)

	# Optimal no. of hashing functions
	k = math.ceil((m / n) * math.log(2))

	# Print stats (not to stdout)
	eprint('FPR:', FPR)
	eprint('Elems to be inserted:', n)
	eprint('Bits per key:', bitsPerKey)
	eprint('Bits in filter (filter size):', m)
	eprint('No. hash functions:', k)

	# Approximately de-duplicate lines in input file
	for line in sys.stdin:
		line = line.strip().encode()

		if not query(line):
			insert(line)
			print(line)
