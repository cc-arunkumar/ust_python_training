#Stack Opertions
class Stack:
    def __init__(self):
      self.stack = []

    def size(self):
      return len(self.stack)

    def is_empty(self):
      return len(self.stack) == 0
    
    def push(self , item):
       self.stack.append(item)

    def peek(self):
       if not self.is_empty():
          return self.stack[-1]
       else:
          print("stack is empty")

    def pop(self):
       if not self.is_empty():
          return self.stack.pop()
       else:
          print("stack is empty")

    def display(self):
       print (self.stack)

    def search(self ,item):
        if not self.is_empty():
            for x in self.stack:
                if  x == item:
                    return True
                return False
        else: 
            print("Stack is empty")
s = Stack()

print("Is_empty?" , s.is_empty())

s.push(10)
s.push(11)
s.push(100)
s.push(200)

print("Removed element fron the stack :",s.pop())
print("last element in the stack :", s.peek())
print("the size is stack  :" , s.size())
print("The stack is :" )
s.display()

print("The element is searched : " , s.search(10))

# Is_empty? True
# Removed element fron the stack : 200
# last element in the stack : 100
# the size is stack  : 3
# The stack is :
# [10, 11, 100]
# The element is searched :  True