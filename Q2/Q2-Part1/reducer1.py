#!/usr/bin/python

#Reduce 1
from operator import itemgetter
import sys

dict_hit_rate = {}

for line in sys.stdin:
  line = line.strip()
  players, hit = line.split('\t')
  try:
      hit=int(hit)
      if dict_hit_rate.get(players) is None:
        dict_hit_rate[players]=(0,0)

      dict_hit_rate[players] = (dict_hit_rate.get(players)[0] + hit, dict_hit_rate.get(players)[1] + 1)


  except ValueError:
      pass

new_dict={}
for key in dict_hit_rate:
  new_dict[key]=dict_hit_rate[key][0]/dict_hit_rate[key][1]

sorted_dict_hit_rate = sorted(new_dict.items(), key=itemgetter(0))


for players, rate in sorted_dict_hit_rate:
  print('%s\t%s' % (players, (round(rate, 2), dict_hit_rate.get(players)[1])))
