import time
from functools import wraps

def mydecorator(func):
  @wraps(func)
  def wrapper(*args):
    current = time.time()
    func(*args)
    elapsed = time.time() - current
    return func.__name__, elapsed
  return wrapper

@mydecorator
def moo():
  with open('/etc/passwd') as fd:
    pass

@mydecorator
def cow():
  with open('/etc/passwd') as fd:
    pass
def main():
  a, b = moo()
  print '{}: {}'.format(a, b)


if __name__=='__main__':
  main()

