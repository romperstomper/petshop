import time

class Node(object):
  def __init__(self, animal):
    self.animal = animal
    self.next = None
    self.age = time.ctime()

class Linkedlist(object):
  def __init__(self):
    self.start = None
    self.end = None

  def Addnode(self, Node):
    if self.start == None:
      self.start = Node
    else:
      self.end.next = Node
    self.end = Node

  def loop(self):
    n = self.start
    while n:
      print n.animal, n.age
      n = n.next

l = Linkedlist()
l.Addnode(Node('cat'))
l.Addnode(Node('dog'))
l.Addnode(Node('lion'))
l.Addnode(Node('tiger'))
l.loop()


