
import os
def walkdirs(a, beenthere=[], result=[]):
  beenthere.append(a)
  for elem in os.listdir(a):
    if os.path.isdir(elem) and elem not in beenthere:
      walkdirs(a + '/' + elem)
#    elif not elem.endswith('.mp3'):
#      continue
    result.append(os.path.getsize(a + '/' + elem))

  print sum(result)/55000000.0 #128kbps is approx 55MB per hour





walkdirs('/usr/local/google/home/gboland')
