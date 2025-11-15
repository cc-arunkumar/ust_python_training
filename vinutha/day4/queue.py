# Queue

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
        # Add an item to the end of the queue (enqueue operation)
        self.queue.append(item)

    def peek(self):  
        # Return the front element without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def deque(self):  
        # Remove and return the front element of the queue (dequeue operation)
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"


# Create a Queue object
q = Queue()

# Initially, queue is empty
print("Is Queue Empty:", q.is_empty())   # Output: True

# Add elements to the queue
q.enque(10)
q.enque(20)
q.enque(30)

# Peek → shows the front element (10) without removing it
print("Front element:", q.peek())        # Output: 10

# Dequeue → removes the front element (10)
print("Removed element:", q.deque())     # Output: 10

# Print queue after removing the front element
print("Queue after pop:", q.queue)       # Output: [20, 30]

# # output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/queue.py
# Is Queue Empty: True
# Front element: 10
# Removed element: 10
# Queue after pop: [20, 30]
# PS C:\Users\303379\day4_training>