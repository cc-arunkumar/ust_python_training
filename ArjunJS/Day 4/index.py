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

class Queue:
    def __init__(self):
        self.queue = []
        
    def size(self):
        return len(self.queue)
    
    def isempty(self):
        return len(self.queue)==0
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def peek(self):
        if not self.isempty():
            return self.queue[-1]
        else:
            print("Queue is Empty!!")
            
    def dequeue(self):
        if not self.isempty():
            return self.queue.pop(0)
        else:
            print("Queue Underflow!!")
            
    def display(self):
        return self.queue

    def search(self,item):
        if not self.isempty():
            return f"Found {item} at position {self.queue.index(item)+1}" if item in self.queue else "Not found"
        else:
            print("Queue is Empty!!")
            
            
a=Stack()
b=Queue()
print(f"Is Queue Empty : {b.isempty()}")
b.enqueue(10)
print(f"Adding element : 10")
print(f"Length of Queue : {b.size()}")
b.enqueue(20)
print(f"Adding element : 20")
print(f"Length of Queue : {b.size()}")
b.enqueue(30)
print(f"Adding element : 30")
print(f"Length of Queue : {b.size()}")
print(f"Peek element : {b.peek()}")
print(f"Removing element {b.dequeue()}")
print(f"Length of Queue : {b.size()}")
print(f"Peek element : {b.peek()}")
print(f"Is Queue Empty : { b.isempty() }")
print(f"Entire Queue : {b.display()}")
print(b.search(20))
# print(f"Is Stack Empty {a.isempty()}")
# a.push(10)
# print(f"Adding element : 10")
# print(f"Length of Stack : {a.size()}")
# a.push(20)
# print(f"Adding element : 20")
# print(f"Length of Stack : {a.size()}")
# a.push(30)
# print(f"Adding element : 30")
# print(f"Length of Stack : {a.size()}")
# print(f"Peek element {a.peek()}")
# print(f"Removing element {a.pop()}")
# print(f"Length of Stack : {a.size()}")
# print(f"Peek element {a.peek()}")
# print(f"Is Stack Empty { a.isempty() }")