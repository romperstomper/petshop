from collections import defaultdict

def checkanagram(a, b):
  base = defaultdict(int)
  target = defaultdict(int)
  for char in a:
    base[char]+=1
  for char in b:
    target[char]+=1
  return base == target

