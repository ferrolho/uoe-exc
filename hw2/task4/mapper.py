#!/usr/bin/python

from __future__ import print_function
import sys
import xml.etree.ElementTree as ET

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def postIsQuestionWithAcceptedAnswer(post):
	return post['PostTypeId'] == '1' and 'AcceptedAnswerId' in post

def postIsAnswer(post):
	return post['PostTypeId'] == '2'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

for line in sys.stdin:
	post = ET.fromstring(line).attrib

	if postIsQuestionWithAcceptedAnswer(post):
		print(post['Id'], post['PostTypeId'], post['AcceptedAnswerId'], sep='\t')
	elif postIsAnswer(post):
		print(post['ParentId'], post['PostTypeId'], post['Id'], post['OwnerUserId'], sep='\t')
