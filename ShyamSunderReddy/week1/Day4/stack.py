class Stack:
    def __init__(self):
        self.stack=[]
    
    def size(self):
        return len(self.stack)
    
    def isempty(self):
        return len(self.stack)==0
    
    def push(self,element):
        self.stack.append(element)
        return element
    
    def pop(self):
        if not self.isempty():
            x=self.stack[-1]
            self.stack.remove(x)
            return  x
        return "is empty"
        
    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        return "Empty"
    
    def search(self,element):
        if not self.isempty():
            return element in self.stack
        return "is Empty"
            

mystack=Stack()
print("is stack empty: ",mystack.isempty())
print("Adding element: ",mystack.push(40))
print("Length of stack: ",mystack.size())
print("Adding element: ",mystack.push(50))
print("Length of stack: ",mystack.size())
print("Adding element: ",mystack.push(60))
print("Length of stack: ",mystack.size())
print("Adding element: ",mystack.push(70))
print("Length of stack: ",mystack.size())
print("Peek element: ",mystack.peek())
print("Popped element: ",mystack.pop())
print("Length of stack: ",mystack.size())
print("is stack empty: ",mystack.isempty())
print("Search in stack: ",mystack.search(50))
print("Search in stack: ",mystack.search(100))

#Sample output
# is stack empty:  True
# Adding element:  40
# Length of stack:  1
# Adding element:  50
# Length of stack:  2
# Adding element:  60
# Length of stack:  3
# Adding element:  70
# Length of stack:  4
# Peek element:  70
# Popped element:  70
# Length of stack:  3
# is stack empty:  False
# Search in stack:  True
# Search in stack:  False