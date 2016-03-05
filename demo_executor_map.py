from time import sleep, strftime
from __future__ import print_function
from concurrent import futures
def display(*args):
  print(strftime('[%H:%M:%S:]'))
  print(args)

def loiter(n):
  msg = '{}loiter({}): waiting for {}s...'
  display(msg.format('\t'*n,n,n))
  sleep(n)
  msg = '{}loiter({}): done.'
  display(msg.format('\t'*n, n))
  return n * 10

def main():
  display('Script starting.')
  executor = futures.ThreadPoolExecutor(max_workers=3)
  results = executor.map(loiter, range(5))
  display('results:', results)
  display('waiting for individual results:')
  for i, result in enumerate(results):
    display('result {}: {}'.format(i, result))




