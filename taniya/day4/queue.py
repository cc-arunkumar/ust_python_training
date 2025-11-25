# Queue implementation using a Python list
class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []
        
    def size(self):
        # Print the current size of the queue
        length = len(self.queue)
        print("Length of queue is:", length)
        
    def is_empty(self):
        # Check if the queue is empty
        empty = len(self.queue) == 0
        print("Queue is empty:", empty)
        return empty   # return value added for peek/pop usage
        
    def push(self, item):
        # Add item to the end of the queue
        self.queue.append(item)
        print("Item pushed in Queue", item)
        s1.size()   # show size after push
        
    def peek(self):
        # Show the front item without removing it
        if not self.is_empty():
            print("Top item:", self.queue[0])
        else:
            print("Queue is empty")
            
    def pop(self):
        # Remove and return the front item
        if not self.is_empty():
            remove = self.queue.pop(0)
            print("Item removed", remove)
        else:
            print("Queue is empty") 
        
# ------------------ Testing the Queue ------------------
s1 = Queue()
s1.size()        # Initially empty
s1.is_empty()    # Check empty status
s1.push(10)      # Push 10
s1.push(20)      # Push 20
s1.push(30)      # Push 30
s1.pop()         # Remove front (10)
s1.size()        # Size after pop
s1.peek()        # Show front item
s1.pop()         # Remove front (20)
s1.size()        # Size after pop
s1.is_empty()    # Check empty status