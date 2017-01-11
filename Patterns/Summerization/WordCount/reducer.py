#!/usr/bin/python

import sys

Count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue
    node, word = data
    if word.lower() == "fantastic":
	Count += 1

print "The number of times of the word \"fantastic\" used on forums is: ", Count
