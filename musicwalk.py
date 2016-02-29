import os

for root, dirs, files in os.walk("."):
  path = root.split('/')
  for fil in files:
    pass
