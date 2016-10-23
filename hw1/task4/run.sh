#!/bin/bash

hdfs dfs -rm -r /user/$USER/assignment1/task4

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.name="Task 4 - s1683857" \
 -files mapper.py,reducer.py \
 -input  /user/$USER/assignment1/task2/part-* \
 -output /user/$USER/assignment1/task4 \
 -mapper mapper.py \
 -combiner reducer.py \
 -reducer reducer.py

#
# Note:
#   Running a combiner might make things slower for small inputs.
#   But it is better for much larger inputs.
#
