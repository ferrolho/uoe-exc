#!/usr/bin/python

# Usage: ./shard.py mapper shards
import sys

shards = [open(str(p) + "-from-" + sys.argv[1], "w")
	for p in range(int(sys.argv[2]))]

for l in sys.stdin:
	key = l.split('\t')[0]
	shard = hash(key) % len(shards)
	shards[shard].write(l)
