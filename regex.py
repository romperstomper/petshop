import re
import sys

def reg(a, b):
  """function that returns the number of OVERLAPPING occurences of substring 
  a in string b."""
  pat = '(?=(' + a + '))'
  return len(re.findall(pat, b))

if __name__=='__main__':
  print reg(sys.argv[1], sys.argv[2])
