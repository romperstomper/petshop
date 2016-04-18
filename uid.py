


def finddups(n):
  d = {}
  with open('/tmp/uids') as fd:
    for line in fd:
      username = line.split(':')[0]
      uid = line.split(':')[2]
      d.setdefault(username, []).append(uid)
  return {k: v for k, v in d.iteritems() if len(v) > 1}

if __name__ == '__main__':
  print finddups('/tmp/uids')


