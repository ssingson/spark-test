#!/usr/bin/python 

#Reduce 2

from operator import itemgetter
from collections import defaultdict
import sys

defs = defaultdict(list)

for line in sys.stdin:
  line = line.strip().split('\t')
  A, B_rate_count = line

  B, rate, count = B_rate_count.split('\',')
  B=B[2:]
  rate=rate[2:]
  count=count[2:-2]
  try:
    rate = float(rate)
    count=int(count)    
    defs[A].append([B, rate, count])

  except ValueError:
    pass 

for player in defs:
  top_n = sorted(defs[player], key=lambda v:(v[1], -v[2]))[0:1]
  print('%s\t%s' % (player, top_n[0][0]))
