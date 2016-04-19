import sys
from functools import wraps


def mydec(func):
  def wrapped_func(*args):
    myargs = list(args[0])
    for i, j in enumerate(myargs):
      myargs[i] =  '+91' + str(j[-10:])
    return func(myargs)
  return wrapped_func

@mydec
def sortnums(n):
  n.sort()
  for elem in n:
    print elem


if __name__ == '__main__':
  data = sys.stdin.read()
  nums = [x for x in data.split('\n') if len(x) >1]
  sortnums(nums)

