#!/usr/bin/python 

#Reduce 1
#Outputs the 4 zone centroids

from operator import itemgetter
import sys
import random as rand
import math

###distance function###
def euclidean(x, y): 
  dist=0
  for i in range(1,len(x)): 
    dist+=((float(x[i])-float(y[i]))**2)

  dist=math.sqrt(dist)
  return dist
#######################

zone_dict={}
final_zone_dict={}

for line in sys.stdin:
  line = line.strip()
  players, xyz_hits = line.split(':')
  xyz, hits = xyz_hits.split('\t')

  xyz=xyz[1:]
  x,y,z=xyz.split(' ')

  try:
      x,y,z=float(x),float(y),float(z) 
      
      if zone_dict.get(players) is None:
        zone_dict[players]=[]
      zone_dict[players].append([x,y,z])
        
  except ValueError:
      pass
  
  
#kmeans here
for player in zone_dict.keys():
  zone_list=zone_dict[player] 

  #initializing random centroids
  indexes_list=rand.sample(range(0, len(zone_list)), 4)

  c1=zone_list[indexes_list[0]]
  c2=zone_list[indexes_list[1]]
  c3=zone_list[indexes_list[2]]
  c4=zone_list[indexes_list[3]]

  c_dict={'c1':c1,'c2':c2,'c3':c3,'c4':c4} #holds centroid values
  c_assignment_dict={'c1':[],'c2':[],'c3':[],'c4':[]} #where all assignments to each centroid will go
  new_c_dict={}


  while c_dict!=new_c_dict: #if what we start w/ is same as end result

    #assign new list to the old list so we work w/ updated centroids
    if new_c_dict != {}:
      c_dict=new_c_dict

    #give assignments for each "zone"
    for zone in zone_list:
      dist_dict={}
      for c in c_dict:
        distance=euclidean(zone,c_dict[c])
        dist_dict[c]=distance
      assignment=min(dist_dict, key = dist_dict.get)
      c_assignment_dict[assignment].append(zone)

    #then, calc new mean for each centroid
    new_c_dict={} #reemptying
    for centroid in c_assignment_dict:
      N=len(c_assignment_dict[centroid]) #len list
      new=[0,0,0] #initializing value of new centroid, mutable

      for z in c_assignment_dict[centroid]: #should be iterable since its a list
        new[0]+=z[0]
        new[1]+=z[1]
        new[2]+=z[2]
      try:
        new[0],new[1],new[2]=round(new[0]/N,1),round(new[1]/N,1),round(new[2]/N,1) #giving the avg
      except ZeroDivisionError:
        pass
      new_c_dict[centroid]=new

  #at this point, we've broken out of the loop
  final_zone_dict[player]=list(new_c_dict.values())


for player in final_zone_dict:
  print('%s\t%s' % (player, final_zone_dict[player]))
