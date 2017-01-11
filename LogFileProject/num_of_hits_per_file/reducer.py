#!/usr/bin/python

import sys

Count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisIP = data_mapped

    if thisKey == "/assets/js/the-associates.js":
	Count += 1

print "The total number of hits to \"/assets/js/the-associates.js\": ", '\t', Count
