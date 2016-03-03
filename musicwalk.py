import os
import sys
from timerdecorator import mytimer
from collections import defaultdict

#@mytimer
def walker(p, filestore):
  if os.path.isdir(p) == False:
    raise
  c = 0
  for root, dirs, files in os.walk(p):
    for fil in files:
      #if os.path.isfile(fil):
        #if not fil.startswith('.'):
      filepath = root + '/' + fil
      filestore[fil].append((filepath, os.stat(filepath).st_size))

def dups(target, filestore):
  walker(target, filestore)
  to_sort = [x for x in filestore.values() if len(x) > 1]
  result = sorted(to_sort, key=lambda x: x[1])
  return result

def deletedups(lists):
  for sublist in lists:
    for elem in sublist[1:]:
      os.remove(elem[0])

def main():
  filestore = defaultdict(list)
  for filename in sys.argv[1:]:
    print 'filename is %s' % filename 
    res = dups(filename, filestore)
  if res:
    print 'about to delete duplicates\n'
    deletedups(res)
    print res, '\n', len(res)

if __name__ == '__main__':
  main()
