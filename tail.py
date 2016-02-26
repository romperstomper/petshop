import re

def tail(filename, numlines=10):
  chunksize = 1024
  lineterm = []
  pat = '\n'
  with open(filename) as fh:
    end = remaining = os.stat(filename).st_size
    while remaining:
      if chunksize > remaining:
        chunksize = remaining
        remaining = 0
      else:
        remaining -= chunksize
      fh.seek(remaining)
      chunk = fh.read(chunksize)
      for i, char in enumerate(chunk):
        if char == '\n':
          lineterm.append(remaining + i)
    tailbyte = lineterm.reverse()[-10:]
    fh.seek(tailbyte)
    return fh.read(tailbyte)

def main():
  for line in tail('petshop.py').split('\n'):
    print line


if __name__ == '__main__':
  main()
