#!/usr/bin/python

oldPost = None
AnsLen = 0
AnsCnt = 0
QueLen = 0

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:
	continue
    
    thisPost = data[0].strip()
    post_type = data[1].strip()
    post_length = int(data[2])
    
    if oldPost and oldPost != thisPost:
	if AnsCnt == 0:
	    print oldPost, '\t', QueLen, '\t', 0
	elif AnsCnt > 0:
	    print oldPost, '\t', QueLen, '\t', float(AnsLen)/AnsCnt
	oldPost = thisPost
	AnsLen = 0
	AnsCnt = 0
	QueLen = 0
    
    oldPost = thisPost
    if post_type == "question":
	QueLen = post_length
    elif post_type == "answer":
	AnsLen += post_length
	AnsCnt += 1

if oldPost != None:
    if AnsCnt == 0:
	print oldPost, '\t', QueLen, '\t', 0
    elif AnsCnt > 0:
	print oldPost, '\t', QueLen, '\t', float(AnsLen)/AnsCnt
