#!/usr/bin/python3

import os
import sys

for line in sys.stdin:
	line.upper()

print(os.environ["mapreduce_map_input_file"])
