import sys
n = int(sys.argv[1])
print "arg is ", n

def decorator(func):
  cache = {}
  def wrapped_func(*args):
    if args not in cache:
      cache[args]=func(*args)
    return cache[args]
  #  if args in cache:
  #    return cache[args]
  #  else:
  #    cache[args] = func(*args)
  #    return cache[args]
  return wrapped_func

@decorator
def fib(n):
  return n if n < 2 else fib(n-2) + fib(n-1)

      
print fib(n)
