import time
import functools

def clock(func):
  @functools.wraps(func)
  def clocked(*args, **kwargs):
    t0 = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - t0
    name = func.__name__
    print elapsed, name, result
    return result
  return clocked

