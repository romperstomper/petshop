

def rev(n):
  res = ''
  c = len(n)
  result = [0] * c
  for index, char in enumerate(n):
    result[c - index - 1] = char
  return result



