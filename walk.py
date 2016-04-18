import sys
from pprint import pprint
import os
from collections import defaultdict

def walk(n):
  result = defaultdict(list)
  renamed = []
  for path, subdirs, files in os.walk(os.getcwd()):
    for fil in files:
      if fil.endswith('.html'):
        print 'file is %s' % fil
        newfil = fil[:-1]
        os.rename(os.path.join(path, fil), os.path.join(path, newfil))
        renamed.append(os.path.join(path, newfil))
  return renamed

if __name__=='__main__':
  pprint(walk(sys.argv[1]))

