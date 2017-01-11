#!/usr/bin/python

oldTag = None
Count = 0
topTag = {}

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue
    
    thisTag = data[0]
    if oldTag and oldTag != thisTag:
	if len(topTag) < 10:
	    topTag[oldTag] = Count
	else:
	    least_count = min(topTag.values())
	    if Count > least_count:
		for tag in topTag.keys():
		    if topTag[tag] == least_count:
			del topTag[tag]
			continue
		topTag[oldTag] = Count

	oldTag = thisTag
	Count = 0
    
    oldTag = thisTag
    Count += 1

if oldTag != None:
    least_count = min(topTag.values())
    if Count > least_count:
	for tag in topTag.keys():
	    if topTag[tag] == least_count:
		del topTag[tag]
		continue
	topTag[oldTag] = Count

for tag in sorted(topTag, key = topTag.get, reverse = True):
    print tag, '\t', topTag[tag]
