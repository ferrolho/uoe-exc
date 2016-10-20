#!/bin/bash
hdfs dfs -rm -r /user/$USER/assignment1/task1
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapred.job.name="Task 1 - s1683857" \
 -input /data/assignments/ex1/webLarge.txt \
 -output /user/$USER/assignment1/task1 \
 -mapper mapper.py \
 -file mapper.py
