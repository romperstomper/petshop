from collections import defaultdict

def palincheck(n):
  c = len(n)
  mid = c/2
  for char in n[:mid]:
    if char == n[c -1]:
      c -= 1
    else:
      return False
  return True

