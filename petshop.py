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
import time

class Animal(object):
  """Doc string for a new Animal Class."""

  def __init__(self):
    """A simple container for a new Animal."""
    self.age = time.time()


class Dog(Animal):
  """Doc string for a new Dog Class."""
  pass


class Cat(Animal):
  """Doc string for a new Cat Class."""
  pass


class Shelter(object):
  """Doc string for a new Shelter Class."""

  def __init__(self):
    """Initializes a new Queue."""
    self.catqueue = Queue()
    self.dogqueue = Queue()

  def GiveAnimal(self, animal):
    """Adds a new animal to the Shelter.

    Args:
      animal: (obj) Cat or Dog
    """
    if isinstance(animal, Cat):
      self.catqueue.PutAnimal(animal)
    else:
      self.dogqueue.PutAnimal(animal)

  def GetAnyAnimal(self, animal):
    """Removies an animal from the Shelter.

    Args:
      animal: (str) string specifying a Cat or a Dog
    """
    if animal == 'cat':
      return self.catqueue.GetAnimal()
    else:
      return self.dogqueue.GetAnimal()

  def GetOldestAnimal(self):
    """Retrieve the oldest animal from either queue, regardless of type.

    Returns:
      (Cat or Dog obj) 
    """
    if self.catqueue.PeekAnimal() < self.dogqueue.PeekAnimal():
      return self.catqueue.GetAnimal()
    return self.dogqueue.GetAnimal()


class Queue(object):
  """Doc string for a new Queue Class."""

  def __init__(self):
    """Initializes a new Queue."""
    self.start = None
    self.end = None

  def PutAnimal(self, animal):
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
    if self.end is not self.start:
      self.start = self.start.next
    return animal

  def PeekAnimal(self):
    """Check the age of the first animal, but don't modify the queue.
    
    Returns:
      age: (str) age of the animal
    """
    return self.start.age

# Sanity Checks
shelter = Shelter()
c1 = Cat()
d1 = Dog()
time.sleep(0.1)
c2 = Cat()
d2 = Dog()
shelter.GiveAnimal(c1)
shelter.GiveAnimal(c2)
shelter.GiveAnimal(d1)
shelter.GiveAnimal(d2)
print shelter.GetOldestAnimal()
