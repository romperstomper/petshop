from concurrent import futures
import time
def sq(n):
  return n**2

def sqmany():
  finals = []
  tasks = range(10)
  maxworkers = 2
  workers = min(maxworkers, tasks)
  with futures.ProcessPoolExecutor(workers) as executor:
    todo = []
    for elem in sorted(tasks):
      future = executor.submit(sq, elem)
      todo.append(future)
      print('{}: {}'.format(elem, future))
    results = []
    for future in futures.as_completed(todo):
      res = future.result()
      print('{}: {}'.format(future, res))
      results.append(res)
  return len(results)

def main():
  t0 = time.time()
  sqmany()
  print (time.time() -t0)

if __name__ == '__main__':
  main()
