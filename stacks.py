class Stack:
  def __init__(self):
    self.internalArray = []

  def push(self, item):
    self.internalArray.append(item)
    

  def pop(self):
    if len(self.internalArray)== 0 :
       print ("This list is empty")
    else:
      a = self.internalArray[-1]
      del self.internalArray[-1]
      return a 

  def __str__(self):
    return self.internalArray.__str__()


stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)
print(stack1)

a = stack1.pop()
print (a)
print(stack1)
stack1.push(a)
stack1.push(5)
print (stack1)
b = stack1.pop()
print (b)
print(stack1)
