import sys
import string


def rangoli(n):
  result = []
  base = range(0, (n-1)*4+1, 2)
  m = len(base)/2
  chars = string.lowercase[:n][::-1] + string.lowercase[1:n]
  mid = len(chars)/2
  ks = range(n-1) + range(n-1, -1, -1)
  for k in ks:
    count = 0
    row = (n-1) * ['-'] * 4 + ['-']
    rowchars = chars[:k] + chars[-1-k:] 
    index = base[m-k:m+1+k]
    for i in index:
      row[i] = rowchars[count]
      count +=1
    result.append(''.join(row))
  return result

if __name__=='__main__':
  res = rangoli(int(sys.argv[1]))
  for elem in res:
    print elem
