class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

  def link(self, otherNode):
    self.next = otherNode
    otherNode.prev = self

  def __str__(self):
    return self.data 


class LinkedList:
  def __init__(self):
    self.first = None
    self.last = None

#main program 
n1 = Node ("apple")
n2 = Node ("orange")
print (n1)
print (n2)

n1.link(n2)
print(n1.prev)
print (n1.next)
print (n2.prev)
print (n2.next)