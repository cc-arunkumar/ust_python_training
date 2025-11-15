# Class representing a simple Queue
class queue:
    def __init__(self):
        self.a = []  # Initialize the queue as an empty list

    # Method to return the size of the queue
    def size(self):
        return len(self.a)
    
    # Method to check if the queue is empty
    def is_empty(self):
        return len(self.a) == 0
        
    # Method to add an item to the queue
    def push(self, item):
        self.a.append(item)

    # Method to get the item at the front of the queue without removing it
    def peek(self):
        if not self.is_empty():
            return self.a[-1]  # Return the last item (queue follows FIFO)
        return "Queue is empty"
        
    # Method to remove and return the item from the front of the queue
    def pop(self):
        if not self.is_empty():
            return self.a.pop(0)  # Remove the first item
        return "Queue is empty"

    # Method to search for an element in the queue
    def search(self, ele):
        if not self.is_empty():
            for i in self.a:
                if i == ele:
                    return "Present"
            return "Not present"
        return "Queue is empty"

# Create a queue object
obj = queue()

# Test the queue functionality
print("Is queue empty:", obj.is_empty())
print("Length of the queue:", obj.size())
obj.push(10)
print("Adding element:", obj.peek())
print("Length of the queue:", obj.size())
obj.push(20)
print("Adding element:", obj.peek())
print("Length of the queue:", obj.size())
obj.push(30)
print("Adding element:", obj.peek())
print("Length of the queue:", obj.size())
print("Removing element:", obj.pop())
print("Length of the queue:", obj.size())
print("Is queue empty:", obj.is_empty())

print("Is 30 present:", obj.search(30))  # Check if 30 is present in the queue




# Sample output

# Is queue empty: True
# Length of the queue: 0
# Adding element: 10
# Length of the queue: 1
# Adding element: 20
# Length of the queue: 2
# Adding element: 30
# Length of the queue: 3
# Removing element: 10
# Length of the queue: 2
# Is queue empty: False
# Is 30 present: Present