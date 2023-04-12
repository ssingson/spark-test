#!/usr/bin/python
# --*-- coding:utf-8 --*--

#Map 1
import re
import sys

pat = re.compile('(?P<hit>m\w+),"(?P<B>\w+,\s\w+)",\d+,\d+\.\d,\d,\d,(?P<A>\w+\s\w+),\d+')
  
for line in sys.stdin:
  match = pat.search(line)
  if match:
    if match.group('hit')=='made':
      hit=1
    else:
      hit=0
    print('%s\t%s' % ((match.group('A') + '; ' + match.group('B')), hit))
