#!/bin/python

import sys


t = int(raw_input().strip())

for a0 in xrange(t):
    n = int(raw_input().strip())
    c = 1
    for elem in xrange(n):
      if elem %2 == 0:
        c *= 2
      else:
        c +=1
    print c

