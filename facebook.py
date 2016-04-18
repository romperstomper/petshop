from collections import defaultdict

def helper(a, b):
  return (a/b) + (a%b > 0) 

def stickers(n):
  base = defaultdict(int)
  target = defaultdict(int)
  for char in 'facebook':
    base[char] += 1
  n = n.replace(' ', '')
  for char in n:
    target[char] += 1
  res = []
  for key in target:
    res.append(helper(target[key], base[key]))
  return res, max(res)


