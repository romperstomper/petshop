#!/usr/bin/python

class Node(object):
  """ Tree node: left and right child + data which can be any object."""
  def __init__(self, data):
    """ Node constructor.
    @param data node data object.
    """
    self.left = None
    self.right = None
    self.data = data
    self.info = None

  def insert(self, data):
    """Insert new node with data.
    @param data node data object to insert.
    """    
    if data < self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.insert(data)

  def print_tree(self):
    """Print content in order."""
    if self.left:
      self.left.print_tree()
    print self.data,
    if self.right:
      self.right.print_tree()

root = Node(8)
root.insert(3)
root.insert(6)
root.insert(4)
root.insert(1)

print 'tree: '
root.print_tree()

