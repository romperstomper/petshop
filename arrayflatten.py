"""Flatten an array of arbitrarily nested arrays.
   Array elements will be integers and will should result in a flat array.
   E.g. [[1,2,[3]],4] -> [1,2,3,4].
"""


def flatten(a):
  """Flattens a list using a generator.
  for elem in a:
    if isinstance(elem, (list, tuple)):
      for nested in flatten(elem):
        yield nested
    else:
      yield elem

def nested(mylist):
  return [x for x in flatten(mylist)]

