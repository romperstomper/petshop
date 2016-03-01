import random
x = range(10)
random.shuffle(x)
print("randomnums is %s" % x)

def partition(seq):
  pi, seq = seq[0], seq[1:]
  lo = [x for x in seq if x <= pi]
  hi = [x for x in seq if x > pi]
  print "partition returns: ", lo, pi, hi
  return lo, pi, hi

def quicksort(seq):
  if len(seq) <= 1: return seq
  lo, pi, hi = partition(seq)
  print lo, pi, hi
  return partition(lo) + [pi] + partition(hi)

#print quicksort(x)





