#!/usr/bin/python

import sys

totalSale = 0
Count = 0
oldDay = None

weekday = {"0":"Sunday", "1":"Monday", "2":"Tuesday", "3":"Wednesday", "4":"Thursday", "5":"Friday", "6":"Saturday"}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisDay, thisSale = data_mapped

    if oldDay and thisDay != oldDay:
        print "The average sale on {0} is {1}.".format(weekday[oldDay], float(totalSale)/Count)
        oldDay = thisDay;
        totalSale = 0
	Count = 0

    oldDay = thisDay
    totalSale += float(thisSale)
    Count += 1

if oldDay != None:
    print "The average sale on {0} is {1}.".format(weekday[oldDay], float(totalSale)/Count)
