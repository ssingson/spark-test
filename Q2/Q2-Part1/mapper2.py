#!/usr/bin/python

#Map 2

from operator import itemgetter
import sys

for line in sys.stdin:
  line = line.strip().split('\t')
  players, rate = line

  A, B = players.split('; ')
  #print(hr)

  rate=rate[1:-1]
  rate=rate.split(',')
  rate, shots = rate
  if int(shots)>3:
    print('%s\t%s' % (A, (B, rate, shots)))
