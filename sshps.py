import os
import time
from concurrent import futures
import subprocess
import sys

FNULL=open(os.devnull, 'w')
MAX_WORKERS = 20

def mydecorator(func):
  counter = 0
  def mywarapper(*args, **kwargs):
    func(args, kwargs)
    counter += 1
  return func

def sshtohost(host):
  # Note we can use Popen or check_output here depending on how much customizing
  # is neeeded.
  p = subprocess.check_output(
      ['/usr/bin/ssh', '{}'.format(host), 'pidof init'],
      stderr=subprocess.PIPE)
  return host, p.strip()
  
def main():
  all_hosts = {}
  try:
    hosts = sys.argv[1:]
  except IndexError:
    print 'hostname must be supplied'
  workers = min(MAX_WORKERS, len(hosts))
  start = time.time()
  with futures.ThreadPoolExecutor(workers) as executor:
    todo = []
    for host in hosts:
      future = executor.submit(sshtohost, host)
      todo.append(future)
    
    results = []
    for future in futures.as_completed(todo):
      res = future.result()
      results.append(res)
  mydict = {k: v for k, v in results}
  print 'result is %s' % mydict, (time.time() -start)

if __name__ == '__main__':
  main()
