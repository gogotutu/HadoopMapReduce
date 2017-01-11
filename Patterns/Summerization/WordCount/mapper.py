#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter = '\t')
delimiters = ".",",","!","?",":",";","\"","(",")","<",">","[","]","#","$","=","-","/"," "
regexPattern = "|".join(map(re.escape,delimiters))
for line in reader:
    node_id = line[0].strip()
    body = line[4]
    if node_id == "id":
	continue
    words = re.split(regexPattern,body)
    for word in words:
	if len(word) > 0:
	    print node_id, '\t', word
