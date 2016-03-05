import time
def multiply(a, b):
  return a*b

def square(a):
  return a**2

def main():
  t0 = time.time()
  [square(x) for x in range(10)]
  print (time.time() - t0)


if __name__ == '__main__':
  main()



