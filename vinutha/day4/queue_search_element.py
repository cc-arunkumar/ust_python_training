#Searching for a element in a Queue 
# Define a Queue class
class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def size(self):
        # Return the number of elements in the queue
        return len(self.queue)

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def enque(self, item): 
        # Add an item to the end of the queue
        self.queue.append(item)

    def peek(self):  
        # Return the front element without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def deque(self):  
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def search(self, item):  
        # Search for an item in the queue
        if item in self.queue:
            return "Found"
        else:
            return "Not Found"


# Create a Queue object
q = Queue()

# Initially, queue is empty
print("Size:", q.size())              # Output: 0
print("Is Queue Empty:", q.is_empty()) # Output: True

# Add elements to the queue
q.enque(10)
q.enque(20)
q.enque(30)

print("After adding elements:", q.queue)  # Output: [10, 20, 30]

# Remove the front element (FIFO behavior)
print("Removed element:", q.deque())      # Output: 10

# Search for an element that exists
print("Searching the element:", q.search(20))  # Output: Found

# Search for an element that does not exist
print("Searching the element:", q.search(40))  # Output: Not Found


# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/queue_search_element.py
# Size: 0
# Is Queue Empty: True
# After adding elements: [10, 20, 30]
# Removed element: 10
# Searching the element: Found
# Searching the element: Not Found
# PS C:\Users\303379\day4_training> 