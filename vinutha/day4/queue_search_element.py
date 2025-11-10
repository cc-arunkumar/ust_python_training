#Searching for a element in a Queue 
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

    def search(self, item):  
        if item in self.queue:
            return "Found"
        else:
            return "Not Found"


q = Queue()
print("Size:", q.size())
print("Is Queue Empty:", q.is_empty())

q.enque(10)
q.enque(20)
q.enque(30)

print("After adding elements:", q.queue)
print("Removed element:", q.deque())
print("Searching the element:", q.search(20))
print("Searching the element:", q.search(40))


# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/queue_search_element.py
# Size: 0
# Is Queue Empty: True
# After adding elements: [10, 20, 30]
# Removed element: 10
# Searching the element: Found
# Searching the element: Not Found
# PS C:\Users\303379\day4_training> 