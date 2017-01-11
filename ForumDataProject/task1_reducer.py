#!/usr/bin/python

active_hours = [0] * 24
oldStudent = None

import sys
#from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue
    thisStudent = data[0]
    post_time = int(data[1])
    
    if oldStudent and oldStudent != thisStudent:	
	for i in range(24):
	    if active_hours[i] == max(active_hours):
		print oldStudent, '\t', i+1
	oldStudent = thisStudent
	active_hours = [0] * 24
    
    oldStudent = thisStudent
    index = post_time - 1
    active_hours[index] += 1

if oldStudent != None:
    for i in range(24):
	if active_hours[i] == max(active_hours):
	    print oldStudent, '\t', i+1
