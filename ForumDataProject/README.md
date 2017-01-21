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

Result sample:

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

## Task 2. Is there correlation between the length of a post and the length of answers?
Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post.

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
    post_id = line[0]
    post_length = len(line[4])
    post_type = line[5].strip()
    parent_id = line[6]

    if post_type == "question":
	print post_id, '\t', post_type, '\t', post_length
    elif post_type == "answer":
	print parent_id, '\t', post_type, '\t', post_length
```

reducer's code:

```
#!/usr/bin/python

oldPost = None
AnsLen = 0
AnsCnt = 0
QueLen = 0

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:
	continue
    
    thisPost = data[0].strip()
    post_type = data[1].strip()
    post_length = int(data[2])
    
    if oldPost and oldPost != thisPost:
	if AnsCnt == 0:
	    print oldPost, '\t', QueLen, '\t', 0
	elif AnsCnt > 0:
	    print oldPost, '\t', QueLen, '\t', float(AnsLen)/AnsCnt
	oldPost = thisPost
	AnsLen = 0
	AnsCnt = 0
	QueLen = 0
    
    oldPost = thisPost
    if post_type == "question":
	QueLen = post_length
    elif post_type == "answer":
	AnsLen += post_length
	AnsCnt += 1

if oldPost != None:
    if AnsCnt == 0:
	print oldPost, '\t', QueLen, '\t', 0
    elif AnsCnt > 0:
	print oldPost, '\t', QueLen, '\t', float(AnsLen)/AnsCnt
```

Result sample:

>111 	35 	0

>15084 	237 	0

>2 	145 	0

>262 	50 	0

>26454 	101 	0

>3778 	69 	164.0

>6011204 	2651 	188.5

>6011936 	347 	442.5

>6012754 	369 	414.0

>6015491 	170 	189.0

>66193 	60 	208.0

>7185 	86 	0

## Task 3. Top tags used in posts

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in. Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.

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
    tags = line[2].split()
    post_type = line[5].strip()

    if post_type == "question":
	for tag in tags:
	    print tag, '\t', 1
```

reducer's code:

```
#!/usr/bin/python

oldTag = None
Count = 0
topTag = {}

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
	continue
    
    thisTag = data[0]
    if oldTag and oldTag != thisTag:
	if len(topTag) < 10:
	    topTag[oldTag] = Count
	else:
	    least_count = min(topTag.values())
	    if Count > least_count:
		for tag in topTag.keys():
		    if topTag[tag] == least_count:
			del topTag[tag]
			continue
		topTag[oldTag] = Count

	oldTag = thisTag
	Count = 0
    
    oldTag = thisTag
    Count += 1

if oldTag != None:
    least_count = min(topTag.values())
    if Count > least_count:
	for tag in topTag.keys():
	    if topTag[tag] == least_count:
		del topTag[tag]
		continue
	topTag[oldTag] = Count

for tag in sorted(topTag, key = topTag.get, reverse = True):
    print tag, '\t', topTag[tag]
```

Results:

>cs101  	8

>cs253  	5

>discussion  	5

>welcome  	3

>issues  	3

>meta  	2

>jobs  	2

>homework  	2

>lessons  	2

>nationalities  	2
