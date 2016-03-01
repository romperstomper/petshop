import os
from timerdecorator import mytimer

@mytimer
def walker(p):
  c = 0
  for root, dirs, files in os.walk(p):
    path = root.split('/')
    for fil in files:
      c += 1
  return c

if __name__ == '__main__':
  print walker('/mnt/pi/')
