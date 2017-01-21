# Analyzing the Forum Data with Hadoop/MapReduce:

## 1. Data:
The data used for this analysis comes from the Udacity course forum posts, and here is a sample content:

> 10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202

> 10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209

> 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 9157

> 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

> 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/reset.css HTTP/1.1" 200 1014

> 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/960.css HTTP/1.1" 200 6206

> 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/the-associates.css HTTP/1.1" 200 15779

> 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/the-associates.js HTTP/1.1" 200 4492

> 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lightbox.js HTTP/1.1" 200 25960

> 10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/search-button.gif HTTP/1.1" 200 168

The format follows the pattern:

## Task 1. Find the most active hour of a student:

In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines.

mapper's code:

```
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
```

reducer's code:

```
#!/usr/bin/python

active_hours = [0] * 24
oldStudent = None

import sys
#from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue
    thisStudent = data[0]
    post_time = int(data[1])
    
    if oldStudent and oldStudent != thisStudent:	
	for i in range(24):
	    if active_hours[i] == max(active_hours):
		print oldStudent, '\t', i+1
	oldStudent = thisStudent
	active_hours = [0] * 24
    
    oldStudent = thisStudent
    index = post_time - 1
    active_hours[index] += 1

if oldStudent != None:
    for i in range(24):
	if active_hours[i] == max(active_hours):
	    print oldStudent, '\t', i+1
```

Result:

>100000000  	9

>100000002  	4

>100000003  	5

>100000005  	1

>100000007  	3

>100000008  	16

>100000009  	20

>100000011  	3

>100000014  	4

>100000016  	23

>100000017  	5

>100000017  	22

>100000018  	2

>100000018  	3

>100000018  	11

>100000018  	16

>100000018  	19

>100000019  	5

>100000020  	5

>100000022  	17
