#Queue Basics
class Queue:
    def __init__(self):
        self.queue = []
    
    def isempty(self):
        return len(self.queue)==0
    
    def size(self):
        return f"Length of the Stack: {len(self.queue)}"
        
    def push(self,element):
        self.queue.append(element)
        return f"Adding {element} in the Queue"
        
    def pop(self):
        if not self.isempty():
            pop_ele = self.queue[0]
            self.queue.remove(pop_ele)
            return f"Popped Element: {pop_ele}"
        return "Queue is Empty"
    
    def front(self):
        if not self.isempty():
            return f"Front Element: {self.queue[0]}"
        return "No Elements in Queue"
    
    def rear(self):
        if not self.isempty():
            return f"Rear Element {self.queue[-1]}"
        return "No Elements in Queue"
    
            
q=Queue()
print(q.size())
print("Is Queue Empty:",q.isempty())
print(q.push(2))
print(q.push(4))
print(q.push(6))
print(q.push(7))
print(q.pop())
print(q.size())
print(q.front())
print(q.rear())
print("Queue:",q.queue)

#Sample Output
# Length of the Stack: 0
# Is Queue Empty: True
# Adding 2 in the Queue
# Adding 4 in the Queue
# Adding 6 in the Queue
# Adding 7 in the Queue
# Popped Element: 2
# Length of the Stack: 3
# Front Element: 4
# Rear Element 7
# Queue: [4, 6, 7]