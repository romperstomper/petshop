"""
Cracking the Coding Interview, exercise 1.4
Write a method to replace all spaces in a string with'%20'. You may assume
that the string has sufficient space at the end of the string to hold the
additional characters, and that you are given the "true" length of the string.
(Note: if imple- menting in Java, please use a character array so that you can
perform this operation in place.
EXAMPLE
Input: "Mr John Smith    "
Output: "Mr%20Dohn%20Smith"
"""
def modifyarray(a, b):
  """Takes an string and modifies it.

  Args:
    a: (str) string representing the array
    b: (int) initial occupied spaces in the array
  Returns:
    array: (list) modified array
  """
  oldstr=' '
  newstr='02%'
  array = [i for i in a]
  i = 0
  indexes = []
  while True:
    try:
      indexes.append(a.index(' ', i, b-1))
      i = indexes[-1] + 1
    except ValueError:
      break
  newpos = len(a)-1
  oldpos = b-1
  while indexes:
    if  oldpos != indexes[-1]:
      array[newpos] = array[oldpos]
      newpos -= 1
      oldpos -= 1
    elif oldpos == indexes[-1]:
      indexes.pop()
      for elem in newstr:
        array[newpos] = elem
        newpos -= 1
      oldpos -= 1
    print array, newpos, oldpos

  return ''.join(array)


# Sanity check
print modifyarray('Mr John Smith    ', 13)
print modifyarray('Mr John Joe Smith      ', 17)


