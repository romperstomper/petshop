import sys
from operator import itemgetter

def mydec(func):
  def inner(*args):
    nested = [x.split() for x in args[0].split('\n') if len(x)>1]
    nested.sort(key=itemgetter(2))
    return nested
  return inner
     
@mydec
def sortnames(names):
  return names


if __name__ == '__main__':
  names = sys.stdin.read()
  print sortnames(names)

