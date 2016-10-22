#!/bin/bash
hdfs dfs -rm -r /user/$USER/assignment1/task3
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.name="Task 3 - s1683857" \
 -D mapreduce.job.reduces=1 \
 -files mapper.py,reducer.py \
 -input  /user/$USER/assignment1/task2/part-* \
 -output /user/$USER/assignment1/task3 \
 -mapper mapper.py \
 -combiner reducer.py \
 -reducer reducer.py
