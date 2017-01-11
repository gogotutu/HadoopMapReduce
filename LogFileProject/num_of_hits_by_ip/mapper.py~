#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
	ip = data[0]
	web = data[6].replace("http://www.the-associates.co.uk","")
	print "{0}\t{1}".format(web,ip)
