

fibcache = {}
def memoize(n):
  if fibcache.get(n):
    return fibcache.get(n)
  else:
    fibcache[n] = n if n < 2 else memoize(n-1) + memoize(n-2)
  return fibcache.get(n)


def mydecorator(func):
  cache = {}
  def wrapped_func(*args):
    if args in cache:
      return cache[args]
    else:
      cache[args] = func(*args)
      return cache[args]
  return wrapped_func

@mydecorator
def fib(n):
  return n if n < 2 else fib(n-1) + fib(n-2)



