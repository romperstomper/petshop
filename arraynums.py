
def arrays(a, b):
  result = []
  for i,j in zip(a, b):
    result.append(i^j)
  return result

