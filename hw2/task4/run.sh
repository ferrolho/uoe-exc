#!/bin/bash

## 1st job ##

hdfs dfs -rm -r /user/$USER/assignment2/task4-temp1

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 4 (Pt. 1) - s1683857" \
  -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
  -D stream.num.map.output.key.fields=2 \
  -D mapreduce.partition.keypartitioner.options="-k1,1n" \
  -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2n" \
  -files mapper.py,reducer.py \
 -input  /data/assignments/ex2/part2/stackLarge.txt \
 -output /user/$USER/assignment2/task4-temp1 \
 -mapper   mapper.py \
 -reducer  reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

## 2nd job ##

hdfs dfs -rm -r /user/$USER/assignment2/task4-temp2

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 4 (Pt. 2) - s1683857" \
  -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
  -D stream.num.map.output.key.fields=2 \
  -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2n" \
  -files reducer2.py \
 -input  /user/$USER/assignment2/task4-temp1/part-* \
 -output /user/$USER/assignment2/task4-temp2 \
 -mapper  cat \
 -reducer reducer2.py

## 3rd job ##

hdfs dfs -rm -r /user/$USER/assignment2/task4

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 4 (Pt. 3) - s1683857" \
  -D mapreduce.job.reduces=1 \
  -files reducer3.py \
 -input  /user/$USER/assignment2/task4-temp2/part-* \
 -output /user/$USER/assignment2/task4 \
 -mapper  cat \
 -reducer reducer3.py

## Create output.out ##

hdfs dfs -cat /user/$USER/assignment2/task4/part-* | head -20 > output.out
