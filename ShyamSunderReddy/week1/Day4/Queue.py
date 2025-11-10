class Queue:
    def __init__(self):
        self.queue=[]
    
    def size(self):
        return len(self.queue)
    
    def isempty(self):
        return len(self.queue)==0
    
    def front(self):
        if not self.isempty():
            return self.queue[0]
        return "is Empty"
    
    def rear(self):
        if not self.isempty():
            return self.queue[-1]
        return "is empty"
        
    def push(self,element):
        self.queue.append(element)
        return element
    
    def pop(self):
        if not self.isempty():
            return self.queue.pop(0)
        return "is empty"
    
    def search(self,element):
        if not self.isempty():
            return element in self.queue
        return "is Empty"
    
myq=Queue()
print("Is queue Empty: ",myq.isempty())
print("Size of the Queue: ",myq.size())
print("Pushed the Element: ",myq.push(10))
print("Size of the Queue: ",myq.size())
print("Pushed the Element: ",myq.push(20))
print("Size of the Queue: ",myq.size())
print("Pushed the Element: ",myq.push(30))
print("Size of the Queue: ",myq.size())
print("Pushed the Element: ",myq.push(40))
print("Size of the Queue: ",myq.size())
print("Front in Queue: ",myq.front())
print("Rear in Queue: ",myq.rear())
print("Removed element: ",myq.pop())
print("Size of the Queue: ",myq.size())
print("Searching in Queue: ",myq.search(20))

#Sample output
# Is queue Empty:  True
# Size of the Queue:  0
# Pushed the Element:  10
# Size of the Queue:  1
# Pushed the Element:  20
# Size of the Queue:  2
# Pushed the Element:  30
# Size of the Queue:  3
# Pushed the Element:  40
# Size of the Queue:  4
# Front in Queue:  10
# Rear in Queue:  40
# Removed element:  10
# Size of the Queue:  3
# Searching in Queue:  True

    
    
    
    