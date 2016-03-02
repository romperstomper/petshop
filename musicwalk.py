import os
import sys
from timerdecorator import mytimer
from collections import defaultdict

#@mytimer
def walker(p):
  if os.path.isdir(p) == False:
    raise
  c = 0
  filestore = defaultdict(list)
  for root, dirs, files in os.walk(p):
    for fil in files:
      #if os.path.isfile(fil):
        #if not fil.startswith('.'):
      filepath = root + '/' + fil
      filestore[fil].append((filepath, os.stat(filepath).st_size))
  print sys.getsizeof(filestore), len(filestore)
  return filestore

def dups(target):
  filestore = walker(target)
  result = [x for x in filestore.values() if len(x) > 1]
  return result


if __name__ == '__main__':
  res = dups(sys.argv[1])
  print res, '\n', len(res)
