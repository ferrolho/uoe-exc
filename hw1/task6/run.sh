#!/bin/bash

hdfs dfs -rm -r /user/$USER/assignment1/task6

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 6 - s1683857" \
  -D mapreduce.map.output.key.field.separator=" " \
  -D num.key.fields.for.partition=2 \
  -files reducer.py \
 -input  /user/$USER/assignment1/task4/part-* \
 -output /user/$USER/assignment1/task6 \
 -mapper  cat \
 -reducer reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
