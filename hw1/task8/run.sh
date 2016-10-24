#!/bin/bash

## 1st job ##

hdfs dfs -rm -r /user/$USER/assignment1/task8-temp

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 8 (Pt. 1) - s1683857" \
  -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
  -D stream.map.output.field.separator="   " \
  -D stream.num.map.output.key.fields=4 \
  -D mapreduce.map.output.key.field.separator="   " \
  -D mapreduce.partition.keypartitioner.options="-k2,2n" \
  -D mapreduce.partition.keycomparator.options="-k2,2n -k1,1r" \
  -files reducer.py \
 -input  /data/assignments/ex1/uniSmall.txt \
 -output /user/$USER/assignment1/task8-temp \
 -mapper  cat \
 -reducer reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

## 2nd job ##

hdfs dfs -rm -r /user/$USER/assignment1/task8

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 8 (Pt. 2) - s1683857" \
  -D mapreduce.job.reduces=1 \
  -files reducer2.py \
 -input  /user/$USER/assignment1/task8-temp/part-* \
 -output /user/$USER/assignment1/task8 \
 -mapper  cat \
 -reducer reducer2.py \

hdfs dfs -cat /user/$USER/assignment1/task8/part-* | head -20 > output.out
