#!/bin/sh
../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../shot_logs.csv /Part2/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Part2/mapper1.py -mapper ../Part2/mapper1.py \
-file ../Part2/reducer2.py -reducer ../Part2/reducer2.py \
-input /Part2/input/* -output /Part2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /Part2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part2/output/
../stop.sh
