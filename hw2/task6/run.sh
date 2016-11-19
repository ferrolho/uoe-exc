#!/bin/bash

./task6.py < /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt > output-temp.out

hdfs dfs -copyFromLocal output-temp.out /user/$USER/assignment2/task6/output.out

cat output-temp.out | head -20 > output.out

rm output-temp.out
