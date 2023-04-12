#!/usr/bin/python 

import re
import sys

#map: k=(player), v=(zone, (result, 1))  
  #where result is 0 or 1

pat = re.compile('(?P<clock>\d+\.\d),\d,\d\.\d,(?P<sh_dist>\d+\.\d),\d,(?P<hit>m\w+),"\w+,\s\w+",\d+,(?P<B_dist>\d+\.\d),\d,\d,(?P<A>\w+\s\w+),\d+')
  
for line in sys.stdin:
  match = pat.search(line)
  if match:
    if match.group('hit')=='made':
      hit=1
    else:
      hit=0
    print('%s\t%s' % ((match.group('A') + ': ' + (match.group('sh_dist')+' '+match.group('B_dist')+' '+match.group('clock'))), (hit,1)))
