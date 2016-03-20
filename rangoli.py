import sys

def matrix(n):
  row = (n-1) * ['-'] * 4 + ['-']
  m = []
  for elem in range(n*2-1):
    m.append(row)
  return m

def rangoli(n):
  result = []
  m = n/2
  base = range(0, (n-1)*4+1, 2)
  ks = range(n-1) + range(n-1, -1, -1)
  print 'ks is %s' % ks
  print 'base is %s' % base
  for k in ks:
    result.append(base[m-k:m+1+k])
  return result

if __name__=='__main__':
  print rangoli(int(sys.argv[1]))
