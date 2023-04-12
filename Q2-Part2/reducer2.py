#!/usr/bin/python 

#Reducer 2, to be used in getting only zones for desired players based on hit rate

from operator import itemgetter
import sys
import random as rand
import math

###euc
def euclidean(x, y): 
  dist=0
  for i in range(1,len(x)): 
    dist+=((float(x[i])-float(y[i]))**2)

  dist=math.sqrt(dist)
  return dist
#####

zone_dict={}
final_zone_dict={}
final_c_hit_dict={}
wanted_players=['james harden', 'chris paul', 'stephen curry', 'lebron james']

for line in sys.stdin:
  line = line.strip()
  players, xyz_hits = line.split(':')
  if players in wanted_players:

    xyz, hits = xyz_hits.split('\t')      
    xyz=xyz[1:]
    x,y,z=xyz.split(' ')

    hits=hits[1:-1]
    hit, count=hits.split(',')
    count=count[1:]

    try:
        x,y,z=float(x),float(y),float(z) 

        if zone_dict.get(players) is None:
          zone_dict[players]=[]
        zone_dict[players].append([[x,y,z],[hit,count]])

    except ValueError:
        pass
    
  
 
  #kmeans here
for player in zone_dict.keys():
  zone_list=zone_dict[player] 

  #initializing random centroids
  indexes_list=rand.sample(range(0, len(zone_list)), 4)

  c1=zone_list[indexes_list[0]][0]
  c2=zone_list[indexes_list[1]][0]
  c3=zone_list[indexes_list[2]][0]
  c4=zone_list[indexes_list[3]][0]

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
        distance=euclidean(zone[0],c_dict[c])
        dist_dict[c]=distance
      assignment=min(dist_dict, key = dist_dict.get)
      c_assignment_dict[assignment].append(zone)       #so this will give the zone and hits

    #then, calc new mean for each centroid
    new_c_dict={} #reemptying
    c_hit_dict={} #keeping track of hit rate

    for centroid in c_assignment_dict:
      N=len(c_assignment_dict[centroid]) #len list
      new=[0,0,0] #initializing value of new centroid, mutable

      for z in c_assignment_dict[centroid]: #should be iterable
        new[0]+=z[0][0]
        new[1]+=z[0][1]
        new[2]+=z[0][2]

        #append hits for later
        if c_hit_dict.get(centroid) is None:
          c_hit_dict[centroid]=[]
        c_hit_dict[centroid].append(z[1])

      try:
        new[0],new[1],new[2]=round(new[0]/N,1),round(new[1]/N,1),round(new[2]/N,1) #giving the avg
      except ZeroDivisionError:
        pass
      new_c_dict[centroid]=new

  #at this point, we've broken out of the while loop
  final_zone_dict[player]=list(new_c_dict.values())
  final_c_hit_dict[player]=c_hit_dict


#here give hit rate for each centroid
  zone_hit_dict={}
  for player in final_c_hit_dict:
    for c in final_c_hit_dict[player]:
      hit_count=0
      total_count=0
      index=int(c[1])-1
      for i in range(len(final_c_hit_dict[player][c])):
        result=final_c_hit_dict[player][c][i]
        hit_count+=int(result[0])
        total_count+=int(result[1])
      hit_rate=round(hit_count/total_count, 2)

      if zone_hit_dict.get(player) is None:
        zone_hit_dict[player]=[]
      zone_hit_dict[player].append([final_zone_dict[player][index], hit_rate])
        

for player in zone_hit_dict:
  zone_rate_list=list(zone_hit_dict[player])
  sorted_zone_rate_list=zone_rate_list.sort(key = lambda x: x[1], reverse=True)

  print('%s\t%s' % (player, zone_rate_list[0][0]))
