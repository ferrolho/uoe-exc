#!/bin/bash

INPUT=/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt

./task7.py $(cat $INPUT | wc -l) < $INPUT > output-temp.out

hdfs dfs -rm /user/$USER/assignment2/task7/output.out

hdfs dfs -copyFromLocal output-temp.out /user/$USER/assignment2/task7/output.out

cat output-temp.out | head -20 > output.out

rm output-temp.out
