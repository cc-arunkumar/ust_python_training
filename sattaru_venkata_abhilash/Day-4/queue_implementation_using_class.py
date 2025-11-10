# Task: Queue Implementation using Class
# Scenario:
# Implement a Queue with enqueue, dequeue, peek, isEmpty, size, and search functionalities.

class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty queue
   
    def enqueue(self, element):
        self.queue.append(element)  # Add element to the end of the queue
 
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)  # Remove and return the front element
 
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]  # Return the front element without removing it
 
    def isEmpty(self):
        return len(self.queue) == 0  # Check if the queue is empty
 
    def size(self):
        return len(self.queue)  # Return the number of elements in the queue
 
    def search(self, element):
        for i in range(len(self.queue)):
            if self.queue[i] == element:
                return f"Element '{element}' found at position {i}"  # 0-based index
        return f"Element '{element}' not found in the queue"


# Example Usage
myQueue = Queue()

myQueue.enqueue('Abhi')
myQueue.enqueue('Rahul')
myQueue.enqueue('Niranjan')

print("Queue:", myQueue.queue)
print("Peek:", myQueue.peek())
print("Dequeue:", myQueue.dequeue())
print("Queue after dequeue:", myQueue.queue)
print("IsEmpty:", myQueue.isEmpty())
print("Size:", myQueue.size())

element_to_search = "Rahul"
print(myQueue.search(element_to_search))


# Sample Output:
# Queue: ['Abhi', 'Rahul', 'Niranjan']
# Peek: Abhi
# Dequeue: Abhi
# Queue after dequeue: ['Rahul', 'Niranjan']
# IsEmpty: False
# Size: 2
# Element 'Rahul' found at position 0
