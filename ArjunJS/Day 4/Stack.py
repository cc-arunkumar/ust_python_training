#Stack
class Stack:
    def __init__(self):
        self.stack = []
        
    def size(self):
        return len(self.stack)
    
    def isempty(self):
        return len(self.stack)==0
    
    def push(self,item):
        self.stack.append(item)
        
    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        else:
            print("Stack is Empty!!")
            
    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            print("Stack Underflow!!")
            
    def display(self):
        return self.stack
    
    def search(self,item):
        if not self.isempty():
            return f"Found {item} at position {self.stack.index(item)+1}" if item in self.stack else "Not found"
        else:
            print("Stack is Empty!!")
a=Stack()

print(f"Is Stack Empty {a.isempty()}")
a.push(10)
print(f"Adding element : 10")
print(f"Length of Stack : {a.size()}")
a.push(20)
print(f"Adding element : 20")
print(f"Length of Stack : {a.size()}")
a.push(30)
print(f"Adding element : 30")
print(f"Length of Stack : {a.size()}")
print(f"Peek element {a.peek()}")
print(f"Removing element {a.pop()}")
print(f"Length of Stack : {a.size()}")
print(f"Peek element {a.peek()}")
print(f"Is Stack Empty { a.isempty() }")

#Output
# Is Stack Empty True
# Adding element : 10
# Length of Stack : 1
# Adding element : 20
# Length of Stack : 2
# Adding element : 30
# Length of Stack : 3
# Peek element 30
# Removing element 30
# Length of Stack : 2
# Peek element 20
# Is Stack Empty False
