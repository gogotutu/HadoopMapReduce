#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
    if len(line) != 19:
	continue
    if line[0] == 'id':
	continue
    tags = line[2].split()
    post_type = line[5].strip()

    if post_type == "question":
	for tag in tags:
	    print tag, '\t', 1
