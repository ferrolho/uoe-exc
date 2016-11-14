#!/bin/bash

## 1st job ##

hdfs dfs -rm -r /user/$USER/assignment2/task3-temp

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 3 (Pt. 1) - s1683857" \
  -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
  -D stream.num.map.output.key.fields=2 \
  -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2n" \
  -files mapper.py,combiner.py,reducer.py \
 -input  /data/assignments/ex2/part2/stackLarge.txt \
 -output /user/$USER/assignment2/task3-temp \
 -mapper   mapper.py \
 -combiner combiner.py \
 -reducer  reducer.py

## 2nd job ##

hdfs dfs -rm -r /user/$USER/assignment2/task3

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.name="Task 3 (Pt. 2) - s1683857" \
  -D mapreduce.job.reduces=1 \
  -files reducer2.py \
 -input  /user/$USER/assignment2/task3-temp/part-* \
 -output /user/$USER/assignment2/task3 \
 -mapper  cat \
 -reducer reducer2.py

hdfs dfs -cat /user/$USER/assignment2/task3/part-* | head -20 > output.out
