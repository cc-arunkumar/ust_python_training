# Queue

class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def enque(self, item): 
        self.queue.append(item)

    def peek(self):  
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def deque(self):  
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"


q = Queue()
print("Is Queue Empty:", q.is_empty())
q.enque(10)
q.enque(20)
q.enque(30)
print("Front element:", q.peek())       
print("Removed element:", q.deque())    
print("Queue after pop:", q.queue)

# # output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/queue.py
# Is Queue Empty: True
# Front element: 10
# Removed element: 10
# Queue after pop: [20, 30]
# PS C:\Users\303379\day4_training>