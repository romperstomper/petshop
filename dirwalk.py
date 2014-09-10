import os

def gen_walkdirs(a):
  for elem in os.listdir(a):
    if os.path.isdir(elem):
      gen_walkdirs(a + '/' + elem)
#    elif not elem.endswith('.mp3'):
#      continue
    print 'elem is %s' % os.path.getsize(elem)
    yield os.path.getsize(elem)

p = '/usr/local/google/home/gboland'
print sum(i for i in gen_walkdirs(p))
