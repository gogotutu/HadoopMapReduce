#!/usr/bin/python

oldPost = None
StudentList = []

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue
    
    thisPost, thisStudent = data
    if oldPost and thisPost != oldPost:
	print oldPost, '\t', StudentList
	oldPost = thisPost
	StudentList = []

    oldPost = thisPost
    if thisStudent not in StudentList:
	StudentList.append(thisStudent)

if oldPost != None:
    print oldPost, '\t', StudentList
