import sys

def makemat(n):
  h = int(n)
  width = h *3
  result = []
  msg = 'WELCOME'
  for i in xrange(1, h, 2):
    result.append('{0:{fill}^{unit}}'.format('.|.'*i, fill='-', unit=width))
  result.append('{0:{fill}^{unit}}'.format(msg, fill='-', unit=width))
  for i in xrange(h,0, -2):
    result.append('{0:{fill}^{unit}}'.format('.|.'*i, fill='-', unit=width))
  return result

if __name__=='__main__':
  print '\n'.join(makemat(sys.argv[1]))

