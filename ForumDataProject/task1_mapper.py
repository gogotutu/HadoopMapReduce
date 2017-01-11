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
    author_id = line[3]
    post_time = line[8]
    hour = datetime.strptime(post_time[:-2], "%Y-%m-%d %H:%M:%S.%f+").time().hour
    print author_id, '\t', hour
