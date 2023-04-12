#!/bin/sh
../start.sh

#test test test
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../shot_logs.csv /Part1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Part1/mapper1.py -mapper ../Part1/mapper1.py \
-file ../Part1/reducer1.py -reducer ../Part1/reducer1.py \
-input /Part1/input/* -output /Part1/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Part1/mapper2.py -mapper ../Part1/mapper2.py \
-file ../Part1/reducer2.py -reducer ../Part1/reducer2.py \
-input /Part1/output/part-00000 -output /Part1/output2/

#/usr/local/hadoop/bin/hdfs dfs -cat /Part1/output/part-00000

/usr/local/hadoop/bin/hdfs dfs -cat /Part1/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1/output2/
../stop.sh
