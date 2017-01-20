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

## Task 1. Find the mean:
mapper's code
```
def mapper():
  dsfdsf
  sdfsd
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
