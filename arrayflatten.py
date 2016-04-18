"""Flatten an array of arbitrarily nested arrays.
Array elements will be integers and nested arrays. Result in a flat array.
E.g. [[1,2,[3]],4] -> [1,2,3,4]."""


def flatten(target_list):
  """Flattens a nested list.

  Args:
    target_list: (int|list|tuple) 

  Yields:
    (int) 

  Raises:
    TypeError: Error if target array contains a type that is not an int or a 
    nested array.
    
  """
  for elem in target_list:
    if isinstance(elem, (list, tuple)):
      for nested in flatten(elem):
        yield nested
    elif isinstance(elem, int):
        yield elem
    else:
      raise TypeError


def nested(mylist):
  """Thin wrapper around flatten."""
  return [x for x in flatten(mylist)]
