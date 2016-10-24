#!/bin/bash

## 1st job ##

hdfs dfs -rm -r /user/$USER/assignment1/task5-temp

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 5 (Pt. 1) - s1683857" \
 -input  /user/$USER/assignment1/task4/part-* \
 -output /user/$USER/assignment1/task5-temp \
 -mapper  cat \
 -reducer cat

## 2nd job ##

hdfs dfs -rm -r /user/$USER/assignment1/task5

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 5 (Pt. 2) - s1683857" \
  -D mapreduce.job.reduces=1 \
 -input  /user/$USER/assignment1/task5-temp/part-* \
 -output /user/$USER/assignment1/task5 \
 -mapper  cat \
 -reducer cat
