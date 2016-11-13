#!/bin/bash

hdfs dfs -rm -r /user/$USER/assignment2/task1

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 1 - s1683857" \
  -files mapper.py,combiner.py,reducer.py \
 -input  /data/assignments/ex2/part1/large/* \
 -output /user/$USER/assignment2/task1 \
 -mapper   mapper.py \
 -combiner combiner.py \
 -reducer  reducer.py

hdfs dfs -cat /user/$USER/assignment2/task1/part-* | head -20 > output.out
