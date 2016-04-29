#!/usr/bin/python
import os
from subprocess import call
import time
import random

files = os.listdir('/home/gary/xkcd') 
random.shuffle(files)
for i in files:
  phile = '/home/gary/xkcd/' + i
  call(['feh', '--bg-center', phile])
  time.sleep(30)
