import time
from functools import wraps

def mytimer(func):
  @wraps(func)
  def wrapper(*args):
    current = time.time()
    res = func(*args)
    elapsed = time.time() - current
    return func.__name__, elapsed, res
  return wrapper

@mytimer
def moo():
  with open('/etc/passwd') as fd:
    pass

@mytimer
def cow():
  with open('/etc/passwd') as fd:
    pass
def main():
  a, b = moo()
  print '{}: {}'.format(a, b)


if __name__=='__main__':
  main()

