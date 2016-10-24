#!/bin/bash

hdfs dfs -rm -r /user/$USER/assignment1/task1

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 1 - s1683857" \
  -files mapper.py \
 -input  /data/assignments/ex1/webLarge.txt \
 -output /user/$USER/assignment1/task1 \
 -mapper  mapper.py \
 -reducer NONE
