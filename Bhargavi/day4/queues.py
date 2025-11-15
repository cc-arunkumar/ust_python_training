# Queue Operations using a class
# This program implements a Queue data structure using a Python class with basic operations.
# It supports enqueue, dequeue, peek, search, display, and checks for size or emptiness.

class Queue:
    def __init__(self):
        self.queue = []   # initialize an empty list to represent the queue
    
    def size(self):
        return len(self.queue)   # return number of elements in the queue
    
    def is_empty(self):
        return len(self.queue) == 0   # check if queue is empty
    
    def enqueue(self, item):
        self.queue.append(item)   # add item to the end of the queue

    def dequeue(self):   # removed 'item' parameter (not needed)
        if not self.is_empty():
            return self.queue.pop(0)   # remove and return first element
        else:
            print("Queue is empty")

    def peek(self):   # removed 'iteam' parameter (not needed)
        if not self.is_empty():
            return self.queue[0]   # return first element without removing
        else:
            print("Queue is empty")

    def display(self):
        print(self.queue)   # print the entire queue
    
    def search(self, item):
        if not self.is_empty():
            # check if item exists in queue
            return item in self.queue
        else:
            print("Queue is empty")
            return False


# Testing the Queue
q = Queue()

# Add elements
q.enqueue(123)
q.enqueue(345)
q.enqueue(6)
q.enqueue(7)

# Display size and status
print("The size of element:", q.size())
print("Is the queue empty:", q.is_empty())

# Search for an element
print("The searched element is:", q.search(34))

# Display queue contents
print("The queue is:")
q.display()

#  Output:

# The size of element 4
# Is the queue is empty : False
# The serached element is : False
# The queue is :
# [123, 345, 6, 7]

        
