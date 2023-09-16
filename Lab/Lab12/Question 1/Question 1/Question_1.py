import math
class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None
class BST:
  def __init__(self):
    self.root = None
    self.count = 0
  def insert(self, value):
    if self.root == None:
      self.root = Node(value)
      return
    else:
      temp = self.root
      while(temp != None):
        if(value < temp.data):
          if temp.left != None:
            temp = temp.left
            continue
          else:
            temp.left = Node(value)
            return
        elif(value >= temp.data):
          if temp.right != None:
            temp = temp.right
            continue
          else:
            temp.right = Node(value)
            return
  def InOrder(self, node):
    if node != None:
      self.count += 1
      self.InOrder(node.left)  
      self.InOrder(node.right)
tree = BST()
for i in range(int(input("Enter Number of Element: "))):
  tree.insert(input("Enter Element: "))
tree.InOrder(tree.root)
print(int(math.log2(tree.count)+1))
