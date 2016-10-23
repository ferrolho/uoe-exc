#!/bin/bash

hdfs dfs -rm -r /user/$USER/assignment1/task5

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.name="Task 5 - s1683857" \
 -D mapreduce.partition.keycomparator.options="-k4nr" \
 -files reducer.py \
 -input  /user/$USER/assignment1/task4/part-* \
 -output /user/$USER/assignment1/task5 \
 -mapper cat \
 -reducer cat
