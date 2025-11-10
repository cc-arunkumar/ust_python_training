# Queue

class Queue:
    
    def __init__(self):
        self.queue=[]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            print("Queue is empty")
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
    
    def search(self, item):
        if not self.is_empty():
            if item in self.queue:
                return True
            else:
                return False
        else:
            print("queue is empty")
            return False
            
daily_task=Queue()

print("Is queue empty= ",daily_task.is_empty())
print("Length of queue = ",daily_task.size())
daily_task.enqueue(10)
print("Search an element 10 is there or not=",daily_task.search(10))
print("Length of queue = ",daily_task.size())
daily_task.enqueue(20)
print("Length of queue = ",daily_task.size())
daily_task.enqueue(30)
print("Length of queue = ",daily_task.size())
print("Removing the element=",daily_task.dequeue())
print("Length of queue = ",daily_task.size())
print("Removing the element=",daily_task.dequeue())
print("Length of queue = ",daily_task.size())
print("Removing the element=",daily_task.dequeue())
print("Length of queue = ",daily_task.size())

print("Searching for 200 : ",daily_task.search(200))

# Sample output

# Is queue empty=  True
# Length of queue =  0
# Search an element 10 is there or not= True
# Length of queue =  1
# Length of queue =  2
# Length of queue =  3
# Removing the element= 10
# Length of queue =  2
# Removing the element= 20
# Length of queue =  1
# Removing the element= 30
# Length of queue =  0
# queue is empty
# Searching for 200 :  False