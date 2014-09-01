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
def modifyarray(a='Mr John Smith    ', b=13):
  """steps:
  find location of occurances of the spaces
  multiply n * 2 to get offset to moveby
  for each space substition in order, add 2 to offset
  """

  old=' '
  new='%20'
  array = [i for i in a]
  i = 0
  indexes = []
  while True:
    try:
      indexes.append(a.index(' ', i))
      i = indexes[-1] + 1
    except ValueError:
      break




