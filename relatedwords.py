from collections import defaultdict
import re

def relatedwords(a):
  allwords = []
  with open(a) as fh:
    for line in fh:
      allwords.append(line.strip())

  result = defaultdict(list)
  for word in allwords[:100]:  # limit to first 10 words as this is cubic 
    for i, char in enumerate(word):
      pat = word[:i] + '.' + word[i+1:]
      result[pat].append(word)
  for word in allwords[:100]:  # limit to first 10 words as this is cubic 
    if 
  return result

# Naive way

def distance(word1, word2):
    difference = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            difference += 1
    return difference

def getchildren(word, wordlist):
    return [ w for w in wordlist if distance(word, w) == 1 ]

# Sanity check
print relatedwords('/usr/share/dict/words')

