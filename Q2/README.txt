Part1 of NBA shot logs used 2 rounds of map and reduce and this folder includes a test.sh file that runs both rounds. 
In testing the python code on the cloud, the start and stop.sh files as well as the shot_logs.csv file (and all other setup files) were located 1 folder back from the test.sh file.

Part2 of NBA shot logs used only 1 round for both subquestions. 
The k-means algorithm was implemented entirely in 1 reduce. 
There are 2 test.sh files for this part, one giving the comfortable zones for all players, and the other giving the best zone for the players explicitly requested in the problem.  
Both test.sh files must be run to yield results for both subquestions. 
Again, the start and stop.sh files and data were originally located only 1 folder back from test.sh and test2.sh when testing on the cloud.
