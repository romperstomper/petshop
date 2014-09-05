"""
1.1 Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
import string

def uniquestr(a):
  if len(a) > 26:
    return False
  resdict = {}
  for char in a:
    if char in resdict:
      return False
    else:
      resdict[char] = 1
  return True

print uniquestr('canonical')



def uniquestr2(a):
  if len(a) > 26:
    return False
  chars = string.ascii_lowercase
  array = [False] * 26
  i = 0
  while i < len(a):
    pos = chars.index(a[i])
    if array[pos] is True:
      return False
    array[pos] = True
    i += 1 

  return True


print uniquestr('canomidul')



