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

class Animal(object):
  """Doc string for a new Animal Class."""

  def __init__(self):
    """A simple container for a new Animal."""
    self.age = time.ctime()

class Dog(Animal):
  """Doc string for a new Dog Class."""
  pass

class Cat(Animal):
  """Doc string for a new Cat Class."""
  pass

class ShelterQueue(object):
  """Doc string for a new Shelter Class."""

  def __init__(self):
    """Initializes a new LinkedList."""
    self.start = None
    self.end = None

  def GiveAnimal(self, animal):
    """Adds a new animal to the end of the ShelterQueue.

    Args:
      animal: (obj) Cat or Dog
    """
    if self.start == None:
      self.start = animal
    else:
      self.end.next = animal
    self.end = animal

  def GetAnimal(self):
    """Removes the first animal from the start of the ShelterQueue.

    Returns:
      animal: (obj) Cat or Dog
    """
    animal = self.start
    self.start = self.start.next
    return animal

  def ListAnimals(self):
    """Iterates through the queue of animals and prints animal type and age."""
    head = self.start
    while node:
      print head.animal, head.age
      node = head.next

  def PeekAnimal(self):
    """Look at the head of the queue, but don't modify the queue.
    
    Returns:
      head: (str) type of the animal
    """
    return self.start.__class__.__name__

# Sanity checks.
cats = ShelterQueue()
dogs = ShelterQueue()
a = Cat()
b = Dog()
cats.GiveAnimal(a)
print cats.PeekAnimal()
dogs.GiveAnimal(b)
print dogs.PeekAnimal()

