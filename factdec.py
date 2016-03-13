import clocked
import sys

@clocked.clock
def fact(n):
  return 1 if n < 2 else n*fact(n-1)

if __name__=='__main__':
  n = int(sys.argv[1])
  fact(n)


