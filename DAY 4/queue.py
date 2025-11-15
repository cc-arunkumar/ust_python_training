# Define a Queue class
class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.queue = []

    # Return the number of elements in the queue
    def size(self):
        return len(self.queue)
    
    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # Add an element to the end of the queue
    def push(self, element):
        self.queue.append(element)
    
    # Remove and return the element at the front of the queue
    def pop(self):
        if not self.is_empty():
            # pop(0) removes the first element (FIFO)
            return self.queue.pop(0)
        else:
            print("Queue is empty")
    
    # Return the element at the front without removing it
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

# Create a new Queue object
q = Queue()

# Check if the queue is empty
if q.is_empty():
    print("The Queue is empty")

# Add element 10 to the queue
print("Adding element 10")
q.push(10)
print("The length of the queue is", q.size())

# Add element 20 to the queue
print("Adding element 20")
q.push(20)
print("The length of the queue:", q.size())

# Check the front element
print("Front element is:", q.peek())

# Remove the front element
print("Popping element:", q.pop())
print("Queue size after pop:", q.size())



""""
SAMPLE OUTPUT

The Queue is empty
Adding element 10
The length of the queue is 1
Adding element 20
The length of the queue: 2
Front element is: 10
Popping element: 10
Queue size after pop: 1
"""