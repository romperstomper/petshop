import sys
from functools import wraps


def mydec(func):
  def wrapped_func(*args):
    for i, j in enumerate(args[0]):
      print i, j
  return wrapped_func

@mydec
def sortnums(n):
  pass


if __name__ == '__main__':
  data = sys.stdin.read()
  nums = [x for x in data.split('\n') if len(x) >1]
  sortnums(nums)
  for num in nums:
    print num

