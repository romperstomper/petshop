import random
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

  def Enqueue(self, Node):
    if self.start == None:
      self.start = Node
    else:
      self.end.next = Node
    self.end = Node

  def Dequeue_any(self):
    animal = self.start
    self.start = self.start.next
    return animal

  def Loop(self):
    n = self.start
    while n:
      print n.animal, n.age
      n = n.next

def OlddestAnimal(catlist, doglist):
  if catlist.start.age < doglist.start.age:
    result = catlist.Dequeue_any()
    return result.animal
  elif catlist.start.age > doglist.start.age:
    result = doglist.Dequeue_any()
    return result.animal
  else:
    all_animals = [catlist, doglist]
    random_animal = random.choice(all_animals)
    result = random_animal.Dequeue_any()
    return result.animal

catlist = Linkedlist()
doglist = Linkedlist()
catlist.Enqueue(Node('cat1'))
doglist.Enqueue(Node('dog1'))
doglist.Enqueue(Node('dog2'))
catlist.Enqueue(Node('cat2'))
catlist.Loop() 
doglist.Loop() 
print OlddestAnimal(catlist, doglist)



