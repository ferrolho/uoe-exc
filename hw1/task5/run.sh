#!/bin/bash

hdfs dfs -rm -r /user/$USER/assignment1/task5

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.name="Task 5 - s1683857" \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.partition.keycomparator.options="-k1,1nr" \
 -D mapreduce.job.reduces=1 \
 -files mapper.py,reducer.py \
 -input  /user/$USER/temp/input.in \
 -output /user/$USER/assignment1/task5 \
 -mapper mapper.py \
 -reducer cat
