import sys

def sumnums():
  n = sum([int(x) for x in sys.argv[2:]])
  print "n is %s" % n


if __name__=='__main__':
  print 'sys argv is %s' % sys.argv
  sumnums()
