#Queue
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

#Output
# Is Queue Empty : True
# Adding element : 10
# Length of Queue : 1
# Adding element : 20
# Length of Queue : 2
# Adding element : 30
# Length of Queue : 3
# Peek element : 30
# Removing element 10
# Length of Queue : 2
# Peek element : 30
# Is Queue Empty : False
# Entire Queue : [20, 30]
# Found 20 at position 1