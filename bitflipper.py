nums = int(raw_input().strip())
for i in xrange(nums):
    a = int(raw_input().strip())
    binary = '{0:032b}'.format(a)
    rev = ['1' if x == '0' else '0' for x in binary]
    s = ''.join(rev)
    print long(s, 2)
