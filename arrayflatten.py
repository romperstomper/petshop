"""Q2. Write some code, that will flatten an array of arbitrarily nested arrays
   of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].
"""
def flatten(a):
  for elem in a:
    if isinstance(elem, (list, tuple)):
      for nested in flatten(elem):
        yield nested
    else:
      yield elem

def nested(mylist):
  return [x for x in flatten(mylist)]


mylist = [1, 2, 3, [4, 5, [6]]]
print nested(mylist)


