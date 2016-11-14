#!/usr/bin/python

from __future__ import print_function
import sys
import xml.etree.ElementTree as ET

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def postIsAnswer(post):
	return post['PostTypeId'] == '2'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

for line in sys.stdin:
	post = ET.fromstring(line).attrib

	if postIsAnswer(post):
		print(post['OwnerUserId'], post['ParentId'], sep='\t')
