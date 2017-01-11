#!/usr/bin/python

import sys

node_list = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue
    node, word = data
    if word.lower() == "fantastically":
	node_list.append(node)

node_list.sort()
print "The word \"fantastically\" can be found in the following nodes: ", node_list
