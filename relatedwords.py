from collections import defaultdict
import re

def relatedwords(a):
  allwords = []
  with open(a) as fh:
    for line in fh:
      allwords.append(line.strip())

  result = defaultdict(list)
  for i in allwords[:10]:  # limit to first 10 words as this is cubic 
    for j in allwords:
      if len(j) != len(i): continue
      if i == j: continue
      for k, char in enumerate(j):
        pat = j[:k] + '.' + j[k+1:]
        if re.search(pat, i):
          result[i].append(j)
  return result


# Sanity check
print relatedwords('words.txt')

