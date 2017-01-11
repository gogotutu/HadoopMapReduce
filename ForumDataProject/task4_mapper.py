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
    post_id = line[0].strip()
    student_id = line[3].strip()
    post_type = line[5].strip()
    parent_id = line[6].strip()

    if post_type == "question":
	print post_id, '\t', student_id
    else:
	print parent_id, '\t', student_id
