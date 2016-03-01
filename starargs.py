def func(*args):
  print 'inside func, args len(args)', args, len(args), type(args)

def starfunc(*args):
  func(*args)


def nostarfunc(*args):
  func(args)
func(5,6,7)
starfunc(1,2,3)
nostarfunc(7,8,9)

