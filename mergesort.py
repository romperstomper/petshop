import random

x = range(20)
random.shuffle(x)
print("unsorted x is %s" %x)

def merge(left, right):
  result = []
  while left and right:
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  return result + (left or right)

def mergesort(seq):
  if len(seq) <= 1:
    return seq
  mid = len(seq)/2
  left = seq[:mid]
  right = seq[mid:]
  lhs = mergesort(left)
  rhs = mergesort(right)
  return merge(lhs, rhs) 

print mergesort(x)

