#!/usr/bin/python

import sys

Count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisIP = data_mapped[0]

    if thisIP == "10.99.99.186":
	Count += 1

print "The total number of hits by IP address \"10.99.99.186\": ", '\t', Count
