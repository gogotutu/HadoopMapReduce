#!/usr/bin/python

from datetime import datetime
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)
