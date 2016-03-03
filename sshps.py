import os
import subprocess
import sys

FNULL=open(os.devnull, 'w')

def sshtohost(host):
  # Note we can use Popen or check_output here depending on how much customizing
  # is neeeded.
  p = subprocess.check_output(
      ['/usr/bin/ssh', '-l', 'osmc', '{}'.format(host), 'pidof init'], stderr=subprocess.PIPE)
  return p
  
def main():
  result = sshtohost(sys.argv[1])
  print 'result is %s\n' % result
if __name__ == '__main__':
  main()
