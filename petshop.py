"""
Cracking the Coding Interview, exercise 3.7
An animal shelter holds only dogs and cats, and operates on a strictly "first
in, first out" basis. People must adopt either the "Oldest" (based on arrival
time) or all the animals in the shelter, or they can select whether they would
prefer a dog or a cat (and will receive the oldest animal of that type). They
cannot select which specific animal they would like. Create the data structures
to maintain this system and implement operations such as enqueue, dequeue,
dequeueDog and dequeueCat. You use the built-in LinkedList data structure.
"""
import random
import time

class Node(object):
  """Doc string for a new Node Class."""

  def __init__(self, animal):
    "A simple container for a new Node."""
    self.animal = animal
    self.next = None
    self.age = time.ctime()

class LinkedList(object):
  """Doc string for a new LinkedList Class."""

  def __init__(self):
    """Initializes a new LinkedList."""
    self.start = None
    self.end = None

  def Enqueue(self, Node):
    """Adds a new Node to the end of the LinkedList."""
    if self.start == None:
      self.start = Node
    else:
      self.end.next = Node
    self.end = Node

  def Dequeue_any(self):
    """Removes the first node from the start of the LinkedList.

    Returns:
      node.animal: (str) type of animal that the node contained
    """
    node = self.start
    self.start = self.start.next
    return node.animal

  def Loop(self):
    node = self.start
    while node:
      print node.animal, node.age
      node = node.next

def OldestAnimal(catlist, doglist):
  """Checks the age of the animal at the start of two lists.

  Args:
    catlist: (LinkedList obj) first list object 
    doglist: (LinkedList obj) other list object

  Returns:
    result.animal: (str) String specifying the type of the oldest animal
  """

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


# Useful sanity checks can be quickly checked by importing the module in REPL
catlist = LinkedList()
doglist = LinkedList()
catlist.Enqueue(Node('cat1'))
doglist.Enqueue(Node('dog1'))
doglist.Enqueue(Node('dog2'))
catlist.Enqueue(Node('cat2'))
catlist.Loop()
doglist.Loop()
print OlddestAnimal(catlist, doglist)



