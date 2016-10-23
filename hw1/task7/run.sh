#!/bin/bash
hdfs dfs -rm -r /user/$USER/assignment1/task7
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.name="Task 7 - s1683857" \
 -files reducer.py \
 -input  /data/assignments/ex1/uniSmall.txt \
 -output /user/$USER/assignment1/task7 \
 -mapper  cat \
 -reducer cat
