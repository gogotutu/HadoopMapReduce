#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19:
	continue
    if line[0] == "id":
	continue

    body = line[4]
    if "." not in body and "?" not in body and "!" not in body:
	writer.writerow(line)
	continue
    if body.count(".") + body.count("?") + body.count("!") == 1 and body[-1] in "?!.":
	writer.writerow(line)
	continue
