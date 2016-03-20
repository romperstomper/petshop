
import sys


time = raw_input().strip()
newtime =time[:2]
print 'time [-2]: %s' % time[-2]
if time[-2] == 'P' and int(time[:2]) != 12:
    print 'first'
    newtime=str(int(time[:2]) + 12)
    print 'newtime %s' % newtime
if time[-2] == 'A' and time[:2] == '12':
    print 'second'
    newtime='00'
    print 'newtime %s' % newtime
print newtime+time[2:-2]
print 'newtime %s, time[2:-2] %s' % (newtime, time[2:-2])
