from collections import defaultdict

def finddup(n):
  dups = defaultdict(list)
  with open(n) as fd:
    data = fd.readlines()
  for line in data:
    username = line.split(':')[0]
    uid = line.split(':')[2]
    dups[uid].append(username)

  res = []
  for k,v in dups.iteritems():
    if len(v) > 1:
      res.append((k,v))
  return res or 'None found!'

if __name__ == '__main__':
  print finddup('/etc/passwd')
