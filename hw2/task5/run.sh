#!/bin/bash

## 1st job ##

hdfs dfs -rm -r /user/$USER/assignment2/task5

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 5 - s1683857" \
  -D mapreduce.job.reduces=1 \
  -files mapper.py,reducer.py \
 -input  /data/assignments/ex2/part3/webLarge.txt \
 -output /user/$USER/assignment2/task5 \
 -mapper   mapper.py \
 -reducer  reducer.py

## Create output.out ##

hdfs dfs -cat /user/$USER/assignment2/task5/part-* | head -20 > output.out
