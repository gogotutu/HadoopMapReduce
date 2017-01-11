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
    post_id = line[0]
    post_length = len(line[4])
    post_type = line[5].strip()
    parent_id = line[6]

    if post_type == "question":
	print post_id, '\t', post_type, '\t', post_length
    elif post_type == "answer":
	print parent_id, '\t', post_type, '\t', post_length
