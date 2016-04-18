class BinaryTree(object):
  def __init__(self, root):
    self.key = root
    self.left_child = None
    self.right_child = None

  def insert_left(self, new_node):
    """inserts a new node as left child."""
    if self.left_child == None:
      self.left_child= BinaryTree(new_node)
    else:
      # Insert a node and push the existing child down one level in the tree.
      t = BinaryTree(new_node)
      t.left_child = self.left_child
      self.left_child = t


