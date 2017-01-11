#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)

data = {}
for line in reader:
    if len(line) != 19:
	continue
    if line[0] == "id":
	continue

    body = line[4]
    data[len(body)] = line

for k  in data.keys()[-10:]:
    line = data[k]
    writer.writerow(line)
