# Hadoop/MapReduce Projects

This repo contains the MapReduce codes for the projects from Udacity Intro to Hadoop and MapReduce course.
Course url: https://classroom.udacity.com/courses/ud617

Four projects are here:

1. Stores Sales Project:
  . Calculate the total sales for each store
  
  . Calculate the total sales for each category
  
  . Calculate the highest individual sale for each store
  
  . Calculate the total sales number and the total sales value for all stores.

### Useful Commands:

1. Put a file on to HDFS:

$hadoop fs -put [filename]

2. Run MapReduce job:

$hs mapper.py reducer.py input_file output_directory

3. get result:

$hadoop fs -get /output_directory/part-00000 local_filename

4. Test run:

$at testfile | ./mapper.py | sort | ./reducer.py
