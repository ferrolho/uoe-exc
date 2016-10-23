#!/bin/bash

## 1st job ##

hdfs dfs -rm -r /user/$USER/assignment1/task3-temp

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.name="Task 3 (Pt. 1) - s1683857" \
 -files mapper.py,reducer.py \
 -input  /user/$USER/assignment1/task2/part-* \
 -output /user/$USER/assignment1/task3-temp \
 -mapper mapper.py \
 -combiner reducer.py \
 -reducer reducer.py

## 2nd job ##

hdfs dfs -rm -r /user/$USER/assignment1/task3

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.name="Task 3 (Pt. 2) - s1683857" \
 -D mapreduce.job.reduces=1 \
 -files reducer.py \
 -input  /user/$USER/assignment1/task3-temp/part-* \
 -output /user/$USER/assignment1/task3 \
 -mapper cat \
 -reducer reducer.py

#
# Note:
#   Running a combiner on the first part, and even making this a 2-job mapreduce solution,
#   might make things slower for small inputs. But it is better for much larger inputs.
#
